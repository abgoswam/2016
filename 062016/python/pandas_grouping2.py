# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:53:22 2016

@author: agoswami
"""

import pandas as pd
import numpy as np

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])

#group_regiment_company = df.groupby(['regiment', 'company'])
group_regiment_company = df.groupby(['regiment', 'company'], as_index=False)

a = group_regiment_company.sum()
b = group_regiment_company.aggregate(np.sum)
c = group_regiment_company.aggregate([np.sum, np.mean])


r = group_regiment_company.size()
s = pd.DataFrame({'count' : r}).reset_index()
t = group_regiment_company.aggregate(np.size)


p = group_regiment_company.mean()
q = group_regiment_company.aggregate(np.mean)

#u = group_regiment_company.count()
#v = group_regiment_company.aggregate(np.count)

#-------------------

#df1 = pd.DataFrame( { 
#    "Name" : ["Alice", "Bob", "Mallory", "Mallory", "Bob" , "Mallory"] , 
#    "City" : ["Seattle", "Seattle", "Portland", "Seattle", "Seattle", "Portland"] } )
#    
#print df1.groupby(["Name", "City"], as_index=False ).count()
#print df1.groupby(["Name", "City"]).count()