# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 07:04:52 2016

@author: agoswami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'F:\aghackerreborn\datasets\MLdatasets\titanic_train.csv', header=0)

#print df.head(3)
#print type(df)
#print df.dtypes
#print df.info()
#print df.describe()
#print df['Age'][0:10]
#print type(df['Age'])
#print "mean Age : {0}".format(df['Age'].mean())
#print "median Age : {0}".format(df['Age'].median())
#print df[df['Age'] > 60]
#print df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]
#print df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

for i in range(1,4):
    print i, len(df[(df['Sex'] == 'male') & (df['Pclass'] == i)])
    
plt.hist(df['Age'].dropna(), bins=16, range=(0,80), alpha = .5)
plt.show()

df['Gender'] = df['Sex'].map({'female' : 0, 'male' : 1}).astype(int)

median_ages = np.zeros((2,3))

for i in range(0,2):
    for j in range(0,3):
        median_ages[i, j] = df[(df['Gender'] == i) & (df['Pclass'] == (j+1))]['Age'].dropna().median()
        
print median_ages
        
df['AgeFill'] = df['Age']
print df.head()

print df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill']].head(10)

for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'AgeFill'] = median_ages[i,j]
                
print df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill']].head(10)   
df['AgeIsNull'] = pd.isnull(df.Age).astype(int)    

print df[['Gender','Pclass','Age','AgeFill', 'AgeIsNull']]         