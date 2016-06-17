# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:43:05 2016

@author: agoswami
"""

import csv

filename = r'E:\hackerreborn\2016\062016\_resources\TrDataExtendedSchema\JoinedInputBrandon.tsv'

columns = ['time', 'camp_id', 'offer_id', 'lp_id', 'click_lead', 'click_leadvalue']
print '\t'.join(columns)

with open(filename, 'rb') as f:    
    csvreader = csv.reader(f, delimiter = '\t')
    
    header = csvreader.next()
    progress = 0    
    for row in csvreader:
        progress += 1
            
#        insert items into the dictionary
        itembag = {}
        for i, titleheader in enumerate(header):
            itembag[titleheader] = row[i]
        
        if (itembag['bucket']=='rr') and (itembag['offer_id'] != '0'):
            selecteditems = []
            
            for key in columns:
                selecteditems.append(itembag[key])
                
            print '\t'.join(selecteditems)
