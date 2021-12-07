from sys import displayhook
from flask import render_template, request, jsonify, redirect
from app import app
from app import __init__

@app.route("/search", methods = ['GET'])
def search():
    query = request.args.get("query")
    # call ranker.score here from ranker file

    # array of objects with Week #, Lecture #, and URL to Lecture
    results = []
    return render_template("index.html", results = results)

@app.route("/")
def homepage():
    results = []
    return render_template("index.html", results = results)
