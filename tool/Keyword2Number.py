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

    for row in bkreader:
        print 'Info: ', row[0],
        nrow = []
        nrow.append(row[0])

        tmpLst = [ item.encode('utf8') for item in row[1].split(',')]
        for keyword in KeywordLib:
            try:
                if tmpLst.index(keyword.encode('utf8')) >= 0:
                    print keyword.encode('utf8'),
                    nrow.append(1)
                else:
                    nrow.append(0)
            except ValueError:
                nrow.append(0)
                pass

        # for keyword in KeywordLib:
        #     if keyword.encode('utf8') == row[1].split(',')[0].encode('utf8'):
        #         print "Debug: ", keyword.encode('utf8')
        #         nrow.append(1)
        #     else:
        #         nrow.append(0)
        writer.writerow(nrow)
        print '.'
        # break

finally:
    BKFile.close()
    UKFile.close()
    OutFile.close()
