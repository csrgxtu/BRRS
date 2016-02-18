#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: RetrieveBookData.py
# Desc: RetrieveBookData will retrieve book text data from 200.20's bookshelf.bookful
#       catalog, summary, title, tags will be retrieved and put into a csv file.
# Usage: ./RetrieveBookData.py 0 50000 ../data/50000.csv
# Date: 18/Feb/2016
# Produced By BR
import sys
from pymongo import MongoClient
import unicodecsv as csv

if len(sys.argv) != 4:
    print 'Usage: RetrieveBookData skip limit outputfile'
    sys.exit(1)

skip = int(sys.argv[1])
limit = int(sys.argv[2])
outputfile = sys.argv[3]

client = MongoClient('mongodb://linyy:rioreader@192.168.200.20/bookshelf')
db = client['bookshelf']
collection = db['bookful']

records = collection.find().skip(skip).limit(limit)
f = open(outputfile, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('isbn', 'catalog', 'summary', 'title', 'tags') )

    for rec in records:
        if not rec.has_key(u'isbn13'):
            # isbn = ''
            continue
        else:
            isbn = rec[u'isbn13']

        if not rec.has_key(u'catalog'):
            catalog = ''
        else:
            catalog = rec[u'catalog']

        if not rec.has_key(u'summary'):
            summary = ''
        else:
            summary = rec[u'summary']

        if not rec.has_key(u'title'):
            title = ''
        else:
            title = rec[u'title']

        if not rec.has_key(u'tags'):
            tags = ''
        else:
            if len(rec[u'tags']) != 0:
                for tag in rec[u'tags']:
                    tags = tags + tag[u'name'].replace('\n', '')
            else:
                tags = ''

        writer.writerow((isbn, catalog.replace('\n', ''), summary.replace('\n', ''), title.replace('\n', ''), tags))
finally:
    f.close()
