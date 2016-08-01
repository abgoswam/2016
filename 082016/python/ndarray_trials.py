# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 11:33:51 2016

@author: agoswami
"""

import numpy as np

#Method 1: Initialize numpy array using lists
m1 = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

#Method 2: Initialize numpy array with zeros.
m2 = np.zeros((2,3))

#Method 3: Using fill and full
m3_fill = np.array([1, 2])
m3_fill.fill(0)

m3_full = np.full((2,3), 10, dtype=np.int)

#Understanding multi-dimensional slicing in Python
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
B = np.array(A)
print B[1:3, 1:3]

for i in range(len(B)):
    for j in range(len(B[0])):
        print "{0} ".format(B[i,j]),
        
    print 