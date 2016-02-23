#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 23/Feb/2016
# Desc: use kmeans clustering the books
# Usage: ./kmeans.py inputfile
#
# Produced By BR
import sys
from sklearn.cluster import KMeans

if len(sys.argv) != 2:
    print 'Usage: ./kmeans.py inputfile'
    sys.exit(1)

inputfile = sys.argv[1]

num_clusters = 120  # douban's book have 120 categories

# km = KMeans(n_clusters=num_clusters)
# km.fit(tfidf_matrix)
# clusters = km.labels_.tolist()
# print clusters
