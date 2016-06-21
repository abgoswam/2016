# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:22:56 2016

@author: agoswami
"""

import numpy as np
import pandas as pd

mydict = {
    'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C' : np.random.randn(8),
    'D' : np.random.randn(8)}
    
df = pd.DataFrame(mydict)

print df.groupby('A').sum()
print df.groupby(['A','B']).sum()


#my2dlist = [
#    ['bar', 'bar', 'baz', 'baz','foo', 'foo', 'qux', 'qux'],
#    ['one', 'two', 'one', 'two','one', 'two', 'one', 'two']]
#
#my2dlistzip = zip(*my2dlist)
#my2dlistziptuples = list(my2dlistzip)
#index = pd.MultiIndex.from_tuples(my2dlistziptuples, names=['first', 'second'])
#
#df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])