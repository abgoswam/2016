# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:25:08 2016

@author: agoswami
"""


class TreeNode():
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


def iterInsert(root, v):
    if root == None:
        root = TreeNode(v)
        return root
        
    p = root
    while(True):
        if ((v <= p.value) & (p.left == None)):
            p.left = TreeNode(v)
            break
        elif((v > p.value) & (p.right == None)):
            p.right = TreeNode(v)
            break
        elif (v <= p.value):
            p = p.left
        else:
            p = p.right
            
    return root
    
def inorder(root):
    if root == None:
        return
        
    inorder(root.left)
    print "{0}".format(root.value)
    inorder(root.right)
    

if __name__ == "__main__":
    
    intlist = [100, 50, 200, 75, 150]
    
    root = None
    for item in intlist:
        root = iterInsert(root, item)
    
    inorder(root)