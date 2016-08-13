# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:12:30 2016

@author: agoswami
"""

from collections import Counter

def IsPermutation(a, b):
    if(len(a) != len(b)):
        return False
        
    a_counts = Counter(a)
#    b_counts = Counter(b)

    for i, v in enumerate(b):
        #    print i, v
        if v not in a_counts:
            return False
            
        a_counts[v] -= 1
        if(a_counts[v] < 0):
            return False
    
    return True, a_counts
    
if __name__ == "__main__":
    a = [1,1,1,1,2,2,2,3,3,4]
    b = [2,2,2,4,1,1,1,1,3,3]
    
    res, res_count = IsPermutation(a, b)
    print res
    print res_count