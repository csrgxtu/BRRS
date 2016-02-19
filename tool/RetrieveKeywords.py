#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: RetrieveKeywords.py
# Desc: NLP task, retrieve keywords from book Data
#
# Usage: ./RetrieveKeywords.py inputfile outputfile
# Produced By BR
import sys
import unicodecsv as csv
import jieba.analyse

if len(sys.argv) != 3:
    print 'Usage: ./RetrieveKeywords.py inputfile outputfile'
    sys.exit(1)

inputfile = sys.argv[1]
outputfile = sys.argv[2]

InFile = open(inputfile, 'rt')
OutFile = open(outputfile, 'wt')
try:
    reader = csv.reader(InFile)
    writer = csv.writer(OutFile)
    for row in reader:
        # print row[0]
        content = row[1] + row[2] + row[3] + row[4]
        tags = jieba.analyse.textrank(content, topK=50)
        writer.writerow((row[0], ",".join(tags)))
        print(row[0] + ", " + ",".join(tags))
finally:
    InFile.close()
    OutFile.close()
