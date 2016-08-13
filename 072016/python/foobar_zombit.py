# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 22:34:01 2016

@author: agoswami
"""

def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    
    activity_set = set()
    if m <= n:
        activity_set.add(m)
        activity_set = activity_set.union(recursive_activity_selector(s, f, m, n))
    
    return activity_set

def greedy_activity_selector(s, f):
    activity_set = set()
    activity_set.add(1)
    k = 1
    for m in range(2, len(s)):
        if s[m] >= f [k]:
            activity_set.add(m)
            k = m
            
    return (activity_set)

def answer(meetings):
    meetings.sort(key=lambda m: m[1])
    print meetings    
    
    s = [0]
    f = [0]
    for m in meetings:
        s.append(m[0])
        f.append(m[1])
    
    activity_set_r = recursive_activity_selector(s, f, 0, len(s)-1)    
    activity_set_g = greedy_activity_selector(s, f)    
    
    print s
    print f
    print activity_set_r
    print activity_set_g
    
    return len(activity_set_g)
    
if __name__ == "__main__":
    meetings1 = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]] 
    answer(meetings1)
    
    meetings2 = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]] 
    answer(meetings2)
    
    meetings3 = [
        [1, 4], 
        [3, 5], 
        [0, 6], 
        [5, 7],
        [3, 9],
        [5, 9],
        [6, 10],
        [8, 11],
        [8, 12],
        [2, 14],
        [12, 16]] 
    answer(meetings3)    
    