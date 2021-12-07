"""Setup at app startup"""
from flask import Flask


app = Flask(__name__)
from app import routes