# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:56:06 2016

@author: abgoswam
"""
import numpy as np
import pandas as pd

df2 = pd.DataFrame({ 'A' : 1.,
'B' : pd.Timestamp('20130102'),
'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),
'F' : 'foo' })

for i in range(10):
    print(i)
    
print(df2)