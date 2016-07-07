# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 11:24:41 2016

@author: agoswami
"""

import numpy as np

def cut_rod(p, n):
    if n == 0:
        return 0
        
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n - i))
        
    return q

def memoized_cut_rod(p, n):
#    initialized with default value
    r = np.full((n+1,), -1)    
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))

    r[n] = q
    return q
    
def bottom_up_cut_rod(p, n):
    r = np.zeros(n+1)
    
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i] + r[j - i])
            
        r[j] = q
    
    return r[n]
    
if __name__ == "__main__":
    p = [-1, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    
    for temp_n in range(1, len(p)):
        print temp_n, cut_rod(p, temp_n)
        
    for temp_n in range(1, len(p)):
        print temp_n, memoized_cut_rod(p, temp_n)
        
    for temp_n in range(1, len(p)):
        print temp_n, bottom_up_cut_rod(p, temp_n)        
        