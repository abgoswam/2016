# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 13:13:26 2016

@author: agoswami
"""

def base2(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    else:  
#        works
        ndiv2list = base2(n/2)
#        print ndiv2list
        ndiv2list.append(n % 2)
        return ndiv2list
        
#        wont work
#        this is because append does things in-place. the return value of append is 'None'
#        return base2(n/2).append(n % 2)

def base3(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n == 2:
        return [2]
    else:
        ndiv3list = base3(n/3)
        ndiv3list.append(n % 3)
        return ndiv3list

def listadd1(l): 
    if len(l) == 0:
#        adding 1 to an empty list : []
        return [1]
        
    lastentry = l.pop() # l is now the shortened list
    
    newentry = lastentry + 1
    if newentry < 2:
        l.append(newentry)
        return l
    else:
        newl = listadd1(l)
        newl.append(-1)
        return newl

#verify listadd1 functionality    
listadd1([1])
listadd1([1, -1])
listadd1([1, 1])
listadd1([1, 0])

def balancedternary(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, -1]
    else:
        ndiv3list = balancedternary(n/3)
        mod = n % 3
        if mod == 0:
            ndiv3list.append(0)
        elif mod == 1:
            ndiv3list.append(1)
        else:
            ndiv3list = listadd1(ndiv3list)
            ndiv3list.append(-1)
        
        return ndiv3list

#verify balancedternary functionality
balancedternary(5)
       
for i in range(10):
    print "{0} : {1} : {2} : {3}".format(i, base2(i), base3(i), balancedternary(i))
    
    