# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 11:43:31 2016

@author: agoswami
"""

class Node:
    def __init__(self, val):
        self.item = val
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def insert(self, node):
        if(self.head is None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def display(self):
        temp = self.head
        while(temp):
            print "{0}:".format(temp.item),
            temp = temp.next

if __name__ == "__main__":
    mylist = [3,4,6,8]
    myLL = LL()
    
    for num in mylist[::-1]:
        node = Node(num)        
        myLL.insert(node)
        
    myLL.display()