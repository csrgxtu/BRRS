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

if len(sys) != 2:
    print "Usage: ./QueryBookInfo.py isbn"
    sys.exit(1)
