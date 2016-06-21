# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:08:40 2016

@author: agoswami
"""

import csv

filename = r'E:\hackerreborn\2016\062016\python\tr_cb\cb_filtered_subsetcol.tsv'

with open(filename, 'rb') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    header = csvreader.next()
    
    for row in csvreader:
        time, cid, oid, lpid, cl, clv = row
        
        rev = float(cl) * float(clv)
        cost = -1 * rev
    
