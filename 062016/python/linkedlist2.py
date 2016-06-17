# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 11:43:31 2016

@author: agoswami
"""

class Node:
    def __init__(self, val):
        self.item = val
        self.next = None
                
def insert(node, head):
    if(head is None):
        return node
    else:
        node.next = head
        return node

def display(node):
    temp = node
    while(temp):
        print "{0}:".format(temp.item),
        temp = temp.next

    print "NULL"
    
def reverseAlt(node):
    if node is None or node.next is None:
        return node

    prev = None        
    head = None
    while(node):
        nxt = node.next
        if nxt is None:
            break
        
        node.next = nxt.next
        nxt.next = node
        if(prev is not None):
            prev.next = nxt
        
        if(head is None):
            head = nxt
            
        prev = node
        node = node.next

    return head

if __name__ == "__main__":
    mylist = [3,4,6,8,7]

    head = None    
    for num in mylist[::-1]:
        node = Node(num)
        head = insert(node, head)
        
    display(head)
    
    head = reverseAlt(head)
    display(head)    
    