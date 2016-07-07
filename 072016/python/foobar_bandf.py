# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 11:06:03 2016

@author: agoswami
"""

def reprbaseb(n, b):
    reverse_rems = []        
    while n:
        quotient, remainder = divmod(n, b)
        reverse_rems.append(remainder)
        n = quotient
        
    return reverse_rems

def answer(n):
#    base case. For 0, the min base is always 2
    if n == 0 or n == 1:
        return 2
        
    ans = None   
    for b in range(2, n):  #the insight here is that (n-1) will surely produce a palindrome. 
        reverse_rems = reprbaseb(n, b)
        if (reverse_rems == reverse_rems[::-1]):
            ans = b
            break
    
    return ans    
     
if __name__ == "__main__":
#    print reprbaseb(0, 2)    
    for i in range(0,100):
        print i, answer(i)