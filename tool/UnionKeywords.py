#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: UnionKeywords.py
# Desc: union all book keywords to get a library of the keywords
#
# Usage: ./UnionKeywords.py inputfile outputfile
# Produced By BR
import sys
import unicodecsv as csv

if len(sys.argv) != 3:
    print 'Usage: ./UnionKeywords.py inputfile outputfile'
    sys.exit(1)

inputfile = sys.argv[1]
outputfile = sys.argv[2]

keywords = []
InFile = open(inputfile, 'rt')
OutFile = open(outputfile, 'wt')
try:
    reader = csv.reader(InFile)
    writer = csv.writer(OutFile)
    for row in reader:
        # print row[1].split(',')
        # print row[1]
        keywords.extend(row[1].split(','))
        # print keywords
        # break

    print len(keywords)
    print len(set(keywords))
    writer.writerow(set(keywords))

finally:
    InFile.close()
    OutFile.close()
