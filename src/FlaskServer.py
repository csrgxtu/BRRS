#!/usr/bin/env python
# coding=utf8
# Author: Archer Reilly
# File: FlaskServer.py
# Desc: The Main Http server by flask framework
#
# Usage: python FlaskServer.py
# Produced By BR
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<keyword>')
def search(keyword):
    return 'search: ' + keyword

if __name__ == '__main__':
    app.debug = True
    app.run()
