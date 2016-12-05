# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:42:27 2016

@author: abgoswam
"""

import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({
    'A' : 1.,
    'B' : pd.Timestamp('20130102'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })

print df2

for i in range(10):
    print i+1

print "abhishek"
