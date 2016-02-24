#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: Searcher.py
# Desc: use woosh to search keyword in the results of Indexer
#
# Usage: ./Searcher.py indexdir keyword
# Produced By BR
# from whoosh.index import create_in
from whoosh.index import open_dir
# from whoosh.fields import *
# from jieba.analyse import ChineseAnalyzer
from whoosh.qparser import QueryParser
from whoosh import scoring
import sys

if len(sys.argv) != 3:
    print 'Usage: ./Seracher.py indexdir keyword'
    sys.exit(1)

indexdir = sys.argv[1]
keyword = sys.argv[2]

# schema = Schema(isbn=TEXT(stored=True), content=TEXT(stored=True, analyzer=ChineseAnalyzer()))
# ix = create_in(indexdir, schema)
ix = open_dir(indexdir)

# scoring.
with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
    query = QueryParser("content", ix.schema).parse(unicode(keyword, 'utf-8'))
    results = searcher.search(query)
    print len(results)
    print results[0]
    print results.score(0)

    print results[1]
    print results.score(1)
