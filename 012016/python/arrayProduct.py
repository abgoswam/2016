# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:05:58 2016

@author: agoswami
"""

from collections import defaultdict

def arrProdDefaultDict(arr):
    res = []
    dd = defaultdict(lambda: [1,1])
    
    runningproduct = 1
    for i in range(1, len(arr)):
        runningproduct = runningproduct * arr[i-1]
        dd[i][0] = runningproduct

    runningproduct = 1
    for i in range(len(arr)-2, -1, -1):
        runningproduct = runningproduct * arr[i+1]        
        dd[i][1] = runningproduct

    for i in range(len(arr)):
        res.append(dd[i][0] * dd[i][1])
    
    return res

def arrProd(arr):
    res = []
    
    forwardProd = [1]
    backProd = [1]
    
    runningproduct = 1
    for i in range(1, len(arr)):
        runningproduct = runningproduct * arr[i-1]
        forwardProd.append(runningproduct)
        
    runningproduct = 1
    for i in range(len(arr)-2, -1, -1):
        runningproduct = runningproduct * arr[i+1]        
        backProd.append(runningproduct)
    
    backProd.reverse()
    for i in range(len(arr)):
        res.append(forwardProd[i] * backProd[i])
    
    print arr
    print forwardProd
    print backProd
    
    return res

if __name__ == "__main__":
    arr = [2,3,4,7,8,9]
    res = arrProd(arr)
    
    print "-"*40    
    print res    

    res2 = arrProdDefaultDict(arr)
    print "-"*40    
    print res2
