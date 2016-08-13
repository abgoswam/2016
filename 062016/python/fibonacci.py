# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 10:24:01 2016

@author: agoswami
"""
import time
import datetime
import numpy as np

def fibB(n):
    if n==0 or n==1:
        return 1
    
    return fibB(n-1) + fibB(n-2)

globalFibVal = [1,1]
def fibBG(n):
    if len(globalFibVal) < (n + 1):
        globalFibVal.append(fibBG(n-1) + fibBG(n-2)) 
    
    return globalFibVal[n]

def fibI(n):
    fibValues = [1, 1]
    for i in range(2, n+1):
        fibValues.append(fibValues[i-1] + fibValues[i-2])
        
    return fibValues[-1]

#as per normal convention, here is what i am following:
#    F_0 = 0
#    F_1 = 1
#    F_2 = 1
#    F_3 = 2

def fibIA(n):
    if n==0 or n==1:
        return n
        
    arr = np.empty(n+1, dtype=int)
    arr[0] = 0
    arr[1] = 1
    
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n]

if __name__ == "__main__":

    for i in range(25):
        print i, fibB(i)
#        
#    print "------------"
#
#    for i in range(40):
#        print i, fibBG(i)
#
#    print "------------"    
#    
#    for i in range(40):
#        print i, fibI(i)

    print "------------"
    
    for i in range(25):    
        print i, fibIA(i)    
    
    