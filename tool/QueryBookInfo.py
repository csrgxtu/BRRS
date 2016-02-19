#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: QueryBookInfo.py
# Desc: query the book information according to the isbn
#
# Usage: ./QueryBookInfo.py isbn
# Produced By BR
import sys
from pymongo import MongoClient

if len(sys.argv) != 2:
    print "Usage: ./QueryBookInfo.py isbn"
    sys.exit(1)

isbn = sys.argv[1]

client = MongoClient('mongodb://linyy:rioreader@192.168.200.20/bookshelf')
db = client['bookshelf']
collection = db['bookful']

record = collection.find_one({'isbn13': isbn})
print record
client.close()
