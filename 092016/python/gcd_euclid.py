# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 09:54:47 2016

@author: agoswami
"""

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        
if __name__ == "__main__":
    print gcd(21, 14)
    print gcd(252, 105)
    print gcd(24, 16)