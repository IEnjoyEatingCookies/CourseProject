from sys import displayhook
from flask import render_template, request, jsonify, redirect
from app import app
from app import __init__
import math
import sys
import time
import metapy
import pytoml

def load_ranker(cfg_file):
    """
    Use this function to return the Ranker object to evaluate, 
    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index.
    """
    return metapy.index.OkapiBM25(1.5,0.75,3.25)

@app.route("/search", methods = ['GET'])
def search():
    query = request.args.get("query")
    # call ranker.score here from ranker file

    # array of objects with Week #, Lecture #, and URL to Lecture
    cfg = "../config.toml"
    print('Building or loading index...')
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker(cfg)




    query = metapy.index.Document()


    print('Running queries')
    input_str = "Vector Space Model"
    query.content(input_str.strip())
    results = ranker.score(idx, query, 10)
    lesson_list = []
    fp = open("file")
    for i, line in enumerate(fp):
        for res_val in results:
            if (i == res_val):
                lesson_list.append(line)
                break
    



    

    return render_template("index.html", results = lesson_list)

@app.route("/")
def homepage():
    results = []
    return render_template("index.html", results = results)
