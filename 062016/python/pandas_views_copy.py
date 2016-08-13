# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:51:16 2016

@author: agoswami
"""

import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print df

dff = df #this does not create a copy of the dataframe
dff['dummy'] = 1

dff = df[df.A > 0] #this creates an implicit copy of the dataframe. Should see warning.
#dff = df[df.A > 0].copy() #this creates a explicit copy of the dataframe. No more warnings

dff['C_cumsum'] = dff['C'].cumsum()

dff.loc[:, 'A'] = 100
dff['A_B_C'] = dff['A'] + dff['B'] + dff['C']

print df
print dff