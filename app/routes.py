from sys import displayhook
from flask import render_template, request, jsonify, redirect
from app import app
from app import __init__
import math
import sys
import time
import metapy
import pytoml
import json
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import random

import requests
from bs4 import BeautifulSoup

def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] 

ps = PorterStemmer()
config_file = 'config.toml'
title_file = 'lessons_file.txt'
query_history_file = 'query_history.txt'
query_max_size = 500

def load_ranker():
    return metapy.index.OkapiBM25(1.5,0.75,3.25)

def search_engine(query, size=10):
    print('Building or loading index...')
    idx = metapy.index.make_inverted_index(config_file)
    ranker = load_ranker()
    document = metapy.index.Document()

    print('Running query')
    document.content(query.strip())
    results = ranker.score(idx, document, size)
    lesson_list = []

    with open(title_file) as f:
        title = json.load(f)
        for result, _ in results:
            lesson_list.append(title[result])
    print('Finished Queries')
    return lesson_list

def get_past_queries():
    with open(query_history_file) as f:
        return json.load(f)

def append_past_queries(query):
    with open(query_history_file, 'r') as f:
        data = json.load(f)
        if query in data:
            return
        if len(data) > query_max_size:
            del data[0]
        data.append(query)
    with open(query_history_file, 'w') as f:
        json.dump(data, f)

def minDistance(word1, word2):
    dp=[[0]*(1+len(word2)) for _ in range(1+len(word1))]
    for i in range(1+len(word1)):
        dp[i][len(word2)]=len(word1)-i
    for j in range(1+len(word2)):
        dp[len(word1)][j]=len(word2)-j
    for i in range(len(word1)-1,-1,-1):
        for j in range(len(word2)-1,-1,-1):
            if word1[i]==word2[j]:
                dp[i][j]=dp[i+1][j+1]
            else:
                dp[i][j]=1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
    return dp[0][0]

def rec_query(query):
    past_queries = get_past_queries()
    query.lower()

    qs = [word for word in query.split(' ')]
    cinnamon_graph = [ps.stem(syn) for word in qs for synonym in synonyms(word) for syn in synonym.split(' ') if syn != '']
    cinnamon_graph.extend([ps.stem(word) for word in qs if word != ''])
    q = [ps.stem(word) for word in qs]

    max_score = -1
    returns = []
    for p_query in past_queries:
        p_query.lower()
        p = p_query.split(" ")

        if minDistance(p_query, query) <= 4:
            continue

        cur_score = 0
        for word in p:
            if ps.stem(word) in cinnamon_graph:
                cur_score += 1

        if cur_score > max_score:
            max_score = cur_score
            returns = []
        if cur_score == max_score:
            returns.append(p_query)

    print(returns)
    return random.choice(returns)



@app.route("/search", methods = ['GET'])
def search():
    query = request.args.get('query')
    if query == '':
        return render_template("index.html", results=[], txt='Give a query')
    if request.args.get('rank') is not None:
        append_past_queries(query)
        return render_template("index.html", results=search_engine(query), txt='')
    elif request.args.get('recommend') is not None:
        print('Recommending things...')
        recommended = rec_query(query)
        print(recommended)
        return render_template("index.html", results=search_engine(recommended), txt='Recommended: ' + recommended)
    return render_template("index.html", results=[], txt='')

@app.route("/")
def homepage():
    return render_template("index.html", results=[])
