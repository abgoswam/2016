# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:49:07 2016

@author: agoswami
"""

def doubler(f):
    def g(x):
        return 2 * f(x)

    return g

def f1(x):
    return x + 1

def magic(*args, **kwargs):
    print "unnamed args:", args
    print "keyword args:", kwargs
    
print f1(9)

myg1 = doubler(f1)
print myg1(9)

magic(1,2, key="word", key2="word2")

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
xticks_args = [i+ 0.5 for i, _ in enumerate(movies)]

magic(xticks_args, movies)

def f2(x, y):
    return x + y

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        print "*args :" 
        print args
        print "**kwargs :" 
        print kwargs
        return 2 * f(*args, **kwargs)

    return g

g = doubler_correct(f2)
print g(1, 2) # 6

g = doubler_correct(f1)
print g(9)