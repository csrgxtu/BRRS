#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: Indexer.py
# Desc: use woosh index the book content in the csv format
#
# Usage: ./Index.py inputfile indexdir
# Produced By BR
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
from whoosh.qparser import QueryParser
import unicodecsv as csv
import sys

if len(sys.argv) != 3:
    print 'Usage: ./Indexer.py inputfile indexdir'
    sys.exit(1)

inputfile = sys.argv[1]
indexdir = sys.argv[2]

InFile = open(inputfile, 'rt')
try:
    schema = Schema(isbn=TEXT(stored=True), content=TEXT(stored=True, analyzer=ChineseAnalyzer()))
    ix = create_in(indexdir, schema)
    writer = ix.writer()


    reader = csv.reader(InFile)
    for row in reader:
        print 'Index: ' + row[0]
        print type(row[1])
        content = row[1] + row[2] + row[3] + row[4]
        # print content
        writer.add_document(isbn=row[0],  content=content)

finally:
    InFile.close()
    writer.commit()

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse(u'思想')
    results = searcher.search(query)
    print len(results)
    print results[0]
