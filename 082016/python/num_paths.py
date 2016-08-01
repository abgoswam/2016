# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 16:30:49 2016

@author: agoswami
"""

import numpy as np

def numPaths(k):
    m = np.zeros((k,k), dtype=np.int)
    
#    zeroth row is easy to fill
    for i in range(1,k):
        m[0,i] = 1
    
#    start from first row
    for i in range(1, k):
        for j in range(i, k):
            m[i, j] = m[i, j -1] + m[i - 1][j]
            
#    print m
    return m[k-1, k-1]
    
if __name__ == "__main__":
    for i in range(1,10):
        nw = numPaths(i)
        print "{0}:{1}".format(i, nw)