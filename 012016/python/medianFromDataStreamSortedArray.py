# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 11:03:31 2015

@author: agoswami

Reference: https://leetcode.com/problems/find-median-from-data-stream/
"""

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sortedA = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        
#        lets first append the value to the list
        self.sortedA.append(num)
        
        keyIdx = len(self.sortedA) - 1
        keyValue = self.sortedA[keyIdx]
        
        i = keyIdx - 1
        while i >= 0 and self.sortedA[i] > keyValue:
            self.sortedA[i+1] = self.sortedA[i]
            i=i-1
            
        #ith element is either smaller or -1, so we need to insert pivot into (i+1)
        self.sortedA[i+1] = keyValue
        
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        
        n = len(self.sortedA)
        
        if n == 0:
            return 0
        
        midIndex = n/2
        if n % 2 == 1:
#           for the odd case, just return the middle element
            retVal = self.sortedA[midIndex]
        else:
#            for the even case, return the mean of the middle two elements
            retVal = (self.sortedA[midIndex] + self.sortedA[midIndex - 1]) / 2.0
            
        return retVal
            
        

# Your MedianFinder object will be instantiated and called as such:

mf = MedianFinder()
mf.addNum(6),
print mf.findMedian(),

mf.addNum(10),
print mf.findMedian(),

mf.addNum(2),
print mf.findMedian()