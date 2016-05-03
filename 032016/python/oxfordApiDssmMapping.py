# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 10:07:52 2016

@author: agoswami
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'E:\hackerreborn\032016\_resources\crowdflower2\train_map_oxfordapi_dssm.csv')
maplabels = {0: 0, 1: 0, 2: 1, 2:1, 3:1}
df['binarylabels'] = df['judgeRating'].map(maplabels)
df.to_csv(r'E:\hackerreborn\032016\_resources\crowdflower2\train_map_oxfordapi_dssm_binary_noindex.csv', index=False)


#lambda operator
f = lambda x,y : x + y

print f(1,1)

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)

temp = (36.5, 37, 37.5,39)

#map
F = map(fahrenheit, temp)
C = map(celsius, F)
print F
print C
print map(lambda x : x * 2, [1,2,3])

#filter
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2 == 0, fib)
print result

#reduce
print reduce(lambda x,y: x+y, [47,11,42,13])

#apply, applymap and map for pandas
frame = pd.DataFrame(np.random.randn(4, 3), 
                    columns=list('bde'), 
                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])

#apply works on a row / column basis of a DataFrame
f1 = lambda x: x.max() - x.min()
print frame.apply(f1)

#applymap works element-wise on a DataFrame
f2 = lambda x: '%.2f' % x
print frame.applymap(f2)

#map works element-wise on a Series.
print frame['e'].map(f2)


#another example of adding an additional column to dataframe
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
mask = df1.applymap(lambda x: x <-0.7)
df1 = df1[-mask.any(axis=1)]
sLength = len(df1['a'])
df1['e'] = pd.Series(np.random.randn(sLength), index=df1.index)



