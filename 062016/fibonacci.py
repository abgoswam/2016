# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 10:24:01 2016

@author: agoswami
"""
import time
import datetime

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


    
if __name__ == "__main__":
    start = datetime.time()    
    print fibB(35)
    end = datetime.time()
    print "Time for fibB : {0}".format(end - start)
    
    start = datetime.time()    
    print fibBG(35)
    end = datetime.time()
    print "Time for fibBG : {0}".format(end - start)
#    
    start = datetime.time()    
    print fibI(35)
    end = datetime.time()
    print "Time for fibI : {0}".format(end - start)
    
#    for i in range(40):
#        print i, fibB(i)
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