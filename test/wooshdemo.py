#!/usr/bin/env python
# coding=utf8
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
from whoosh.qparser import QueryParser

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(analyzer=ChineseAnalyzer()))
ix = create_in("indexdir", schema)
writer = ix.writer()
# writer.add_document(title=u"First document", path=u"/a", content=u"This is the first document we've added!")
# writer.add_document(title=u"Second document", path=u"/b", content=u"The second one is even more interesting!")
writer.add_document(title=u"third document", path=u"/c", content=u"《智能Web算法》涵盖了五类重要的智能算法：搜索、推荐、聚类、分类和分类器组合，并结合具体的案例讨论了它们在Web 应用中的角色及要注意的问题。除了第1 章的概要性介绍以及第7 章对所有技术的整合应用外，第2～6 章以代码示例的形式分别对这五类算法进行了介绍。")
writer.add_document(title=u"fourth document", path=u"/d", content=u"面向的是广大普通读者，特别是对算法感兴趣的工程师与学生，所以对于读者的知识背景并没有过多的要求。")


writer.commit()

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse(u"智能")
    results = searcher.search(query)
    print results[0]
