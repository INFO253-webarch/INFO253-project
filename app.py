#!/usr/bin/env python
import shelve
from subprocess import check_output
import flask
from flask import request, Flask, render_template, jsonify, abort, redirect
from os import environ

import os
import sys
import json
import hashlib

app = flask.Flask(__name__)
app.debug = True

# Database/Dictionary to save shortened URLs
db = shelve.open("shorten.db")

@app.route('/')
def index():
    """
    Builds a template based on a GET request, with some default
    arguments
    """

    return flask.render_template('index.html')

###
# Now we'd like to do this generally:
# <short> will match any word and put it into the variable =short= Your task is
# to store the POST information in =db=, and then later redirect a GET request
# for that same word to the URL provided.  If there is no association between a
# =short= word and a URL, then return a 404
###

@app.route("/create", methods=['POST'])
def create():
    """
    This POST request creates an association between a short url and a full url
    and saves it in the database (the dictionary db)
    """
    raise NotImplementedError     

@app.route("/short/<short>", methods=['GET'])
def redirect(short):
    """
    Redirect the request to the URL associated =short=, otherwise return 404
    NOT FOUND
    """
    raise NotImplementedError 

if __name__ == "__main__":
    app.run()
