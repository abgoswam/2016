# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 11:03:31 2015

@author: agoswami

Reference: https://leetcode.com/problems/find-median-from-data-stream/
"""
#from __future__ import division

class MinHeap:
    def __init__(self):
        self.items = [-1]
        self.vsize = 0

    def add(self, num): 
        if(self.vsize == (len(self.items) - 1)):
            self.items.append(num)
        else:
            self.items[self.vsize + 1] = num
            
        self.vsize += 1
        
#        try to fix value at vsize if necessary
        fixidx = self.vsize       
        while(True):
            parentidx = (fixidx / 2)
            if(parentidx <= 0):
                break
            
            leftidx = (2 * parentidx)
            rightidx = (2 * parentidx) + 1

            smalleridx = leftidx            
            smallerval = self.items[smalleridx]
            
            if(rightidx <= self.vsize and self.items[rightidx] < smallerval):
                smalleridx = rightidx                
                smallerval = self.items[smalleridx]
                
            if(self.items[parentidx] < smallerval):
                break
            else:
                tmp = self.items[parentidx]
                self.items[parentidx] = self.items[smalleridx]
                self.items[smalleridx] = tmp
                
            fixidx = parentidx
            
        return
            
    def deleteTop(self):      
        if((self.vsize < 1) or (len(self.items) <= 1)):
            raise ValueError("trying to delete from invalid Min Heap.")
            
        topval = self.items[1]
        self.items[1] = self.items[self.vsize]
        self.vsize -=1 
        
        if((self.vsize == 0) or (self.vsize == 1)):
            return topval
        
        fixidx = 1
        while(True):
            leftidx = 2 * fixidx
            if(leftidx > self.vsize):
                break
            
            rightidx = (2 * fixidx) + 1
            
            smalleridx = leftidx            
            smallerval = self.items[smalleridx]
            
            if(rightidx <= self.vsize and self.items[rightidx] < smallerval):
                smalleridx = rightidx                
                smallerval = self.items[smalleridx]
                
            if(self.items[fixidx] < smallerval):
                break
            else:
                tmp = self.items[fixidx]
                self.items[fixidx] = self.items[smalleridx]
                self.items[smalleridx] = tmp
            
            fixidx = smalleridx
        
        
        return topval
        
        
class MaxHeap:
    def __init__(self):
        self.items = [-1]
        self.vsize = 0

    def add(self, num):
        if(self.vsize == (len(self.items) - 1)):
            self.items.append(num)
        else:
            self.items[self.vsize + 1] = num
            
        self.vsize += 1
        
#        try to fix value at vsize if necessary
        fixidx = self.vsize       
        while(True):
            parentidx = (fixidx / 2)
            if(parentidx <= 0):
                break
            
            leftidx = (2 * parentidx)
            rightidx = (2 * parentidx) + 1

            largeridx = leftidx            
            largerval = self.items[largeridx]
            
            if(rightidx <= self.vsize and self.items[rightidx] > largerval):
                largeridx = rightidx                
                largerval = self.items[largeridx]
                
            if(self.items[parentidx] > largerval):
                break
            else:
                tmp = self.items[parentidx]
                self.items[parentidx] = self.items[largeridx]
                self.items[largeridx] = tmp
                
            fixidx = parentidx
            
        return
        

        
    def deleteTop(self):
        if((self.vsize < 1) or (len(self.items) <= 1)):
            raise ValueError("trying to delete from invalid Min Heap.")
            
        topval = self.items[1]
        self.items[1] = self.items[self.vsize]
        self.vsize -=1 
        
        if((self.vsize == 0) or (self.vsize == 1)):
            return topval
        
        fixidx = 1
        while(True):
            leftidx = 2 * fixidx
            if(leftidx > self.vsize):
                break
            
            rightidx = (2 * fixidx) + 1
            
            largeridx = leftidx            
            largerval = self.items[largeridx]
            
            if(rightidx <= self.vsize and self.items[rightidx] > largerval):
                largeridx = rightidx                
                largerval = self.items[largeridx]
                
            if(self.items[fixidx] > largerval):
                break
            else:
                tmp = self.items[fixidx]
                self.items[fixidx] = self.items[largeridx]
                self.items[largeridx] = tmp
            
            fixidx = largeridx
        
        
        return topval


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap = MaxHeap()
        self.minheap = MinHeap()
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        
#       in all other cases, we know the max heap has at least 1 value
        if((self.maxheap.vsize == 0) or (num <= self.maxheap.items[1])):
            self.maxheap.add(num)
        else:
            self.minheap.add(num)
          
#       need to rebalance the trees in case there is mismatch in the size
        if(self.maxheap.vsize - self.minheap.vsize > 1): 
            val = self.maxheap.deleteTop()
            self.minheap.add(val)
            
        elif(self.minheap.vsize - self.maxheap.vsize > 1):
            val = self.minheap.deleteTop()
            self.maxheap.add(val)

#        verify difference of sizes are not greater than 1
        if(abs(self.maxheap.vsize - self.minheap.vsize) > 1):
            raise ValueError("difference of sizes greater than 1")
            

        return

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        median = 0
        if((self.minheap.vsize < 1) and (self.maxheap.vsize < 1)):                
            return 0
        
        if(self.maxheap.vsize > self.minheap.vsize):
            median = self.maxheap.items[1]
        elif(self.minheap.vsize > self.maxheap.vsize):
            median = self.minheap.items[1]
        else:
            median = (self.maxheap.items[1] + self.minheap.items[1]) / 2.0
        
        return median


def displayHeaps(mf):
    print "-" * 40
    print "Max Heap : "    
    for i in range(1, mf.maxheap.vsize + 1):
        print mf.maxheap.items[i]
        
    print "Min Heap : "    
    for i in range(1, mf.minheap.vsize + 1):
        print mf.minheap.items[i]

    print "Median : {0}".format(mf.findMedian())        
    print "-" * 40

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()

#mf.addNum(1)
#displayHeaps(mf)
#
#mf.addNum(100)
#displayHeaps(mf)
#
#mf.addNum(500)
#displayHeaps(mf)
#
#mf.addNum(50)
#displayHeaps(mf)
#
#mf.addNum(30)
#displayHeaps(mf)
# 
#mf.addNum(20)
#displayHeaps(mf) 

mf.addNum(11) 
mf.addNum(2) 
mf.addNum(4)
mf.addNum(3)
mf.addNum(7)
mf.addNum(10)
mf.addNum(9)
mf.addNum(-1) 
displayHeaps(mf)
 
mf.findMedian()