#!/usr/bin/env python
# coding=utf8
# Author: Archer Reilly
# File: FlaskServer.py
# Desc: The Main Http server by flask framework
#
# Usage: python FlaskServer.py
# Produced By BR
from flask import Flask, render_template, jsonify
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
from pymongo import MongoClient


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<keyword>')
def search(keyword):
    isbns = searchHelper(keyword)
    # print len(isbns)
    results = queryBookInfos(list(set(isbns)))
    # print len(results)
    # print isbns[0 : 10]
    # return 'search: ' + keyword
    return jsonify(results=results)

def searchHelper(keyword):
    #ix = open_dir('/home/archer/Documents/Python/BRRS/data/5windexdir/')
    ix = open_dir('../data/1kindexdir/')

    with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
        query = QueryParser("content", ix.schema).parse(keyword)
        results = searcher.search(query, limit=128) # limit here temporary
        print len(results)
        for result in results:
            print result
        # print results[0]['isbn']
        return [result['isbn'] for result in results]

def queryBookInfos(isbns):
    client = MongoClient('mongodb://linyy:rioreader@192.168.200.20/bookshelf')
    # client = MongoClient('mongodb://192.168.100.2/bookshelf')
    db = client['bookshelf']
    collection = db['bookful']

    data = []
    for isbn in isbns:
        record = collection.find_one({'isbn13': isbn})
        # print record[u'isbn13'], record[u'title'], record[u'image']
        data.append([record[u'isbn13'], record[u'title'], record[u'images'][u'large']])

    client.close()
    return data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
