from sys import displayhook
from flask import render_template, request, jsonify, redirect
from app import app
from app import __init__
import math
import sys
import time
import metapy
import pytoml

def load_ranker():
    return metapy.index.OkapiBM25(1.5,0.75,3.25)

@app.route("/recommend", methods = ['GET'])
def recommend():
    results = []
    return render_template("index.html", results = results)

@app.route("/search", methods = ['GET'])
def search():
    search_string = request.args.get('query')
    cfg = 'config.toml'
    lessons = 'lessonsInOrder.txt'
    
    print('Building or loading index...')
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker()
    query = metapy.index.Document()

    print('Running queries')
    query.content(search_string.strip())
    results = ranker.score(idx, query, 10)
    print(results)
    lesson_list = []

    with open(lessons) as f:
        lines = f.readlines()
        for i, _ in results:
            split = lines[i].index(' ')
            lesson_list.append({'Week': lines[i][:split], 'Lecture': lines[i][split + 1:], 'URL': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
    print('Finished Queries')

    return render_template("index.html", results = lesson_list)

@app.route("/")
def homepage():
    results = []
    return render_template("index.html", results = results)
