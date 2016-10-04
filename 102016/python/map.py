# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 08:40:37 2016

@author: agoswami
"""

#------PYTHON---------
#https://bradmontgomery.net/blog/pythons-zip-map-and-lambda/
#Problem : that you've got two collections of values and you need to keep the largest (or smallest) from each. These could be metrics from two different systems, stock quotes from two different services, or just about anything. 

a = [1, 2, 3, 4, 5]
b = [2, 2, 9, 0, 9]

#Approach 1.
maxval = []
for i in range(len(a)):
    if a[i] >= b[i]:
        maxval.append(a[i])
    else:
        maxval.append(b[i])
        
#Approach 2.
print map(lambda pair: max(pair), zip(a,b))


#---------PANDAS----------
#http://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=list('bde'), index=['Seattle', 'Utah', 'Ohio', 'Texas', 'Oregon'])

#1. Using DataFrame 'apply'
#applying a function on 1D arrays to each column or row. 
f = lambda x: x.max() - x.min()
df.apply(f)

#2. Using DataFrame 'applymap'
#Element-wise Python functions can be used, too. Suppose you wanted to compute a formatted string from each floating point value in frame. You can do this with applymap
formatf = lambda x: '%.2f' % x
df.applymap(formatf)

#3. Using Series 'map'
formatf = lambda x: '%.2f' % x
df['f'] = df['e'].map(formatf)

#Summing up, apply works on a row / column basis of a DataFrame, applymap works element-wise on a DataFrame, and map works element-wise on a Series