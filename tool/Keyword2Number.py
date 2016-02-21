#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: Keyword2Number.py
# Desc: Turn keyword into number from keyword file based on union
#       keyword file
#
# Usage: ./Keyword2Number.py bookkeywordfile unionkeyword outputfile
# Produced By BR
import sys
import unicodecsv as csv

if len(sys.argv) != 4:
    print 'Usage: ./Keyword2Number.py bookkeywordfile unionkeyword outputfile'
    sys.exit(1)

bkfile = sys.argv[1]
ukfile = sys.argv[2]
outfile = sys.argv[3]

KeywordLib = []
BKFile = open(bkfile, 'rt')
UKFile = open(ukfile, 'rt')
OutFile = open(outfile, 'wt')
try:
    bkreader = csv.reader(BKFile)
    ukreader = csv.reader(UKFile)
    writer = csv.writer(OutFile)
    for row in ukreader:
        KeywordLib.extend(row)
    # print KeywordLib

    for row in bkreader:
        # print row[1].split(',')
        nrow = []
        nrow.append(row[0])
        bkeywords = row[1].split(',')
        for keyword in KeywordLib:
            # if keyword in bkeyword:
            # print keyword
            # print type(keyword)
            # print bkeyword[0]
            # print type(bkeyword)
            for bkeyword in bkeywords:
                if keyword == bkeyword:
                    nrow.append(1)
                else:
                    nrow.append(0)
            # if bkeyword.index(keyword) >= 0:
            #     nrow.append(1)
            # else:
            #     nrow.append(0)
        writer.writerow(nrow)
finally:
    BKFile.close()
    UKFile.close()
    OutFile.close()
