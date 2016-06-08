# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:56:32 2016

@author: agoswami
"""

from __future__ import division # want 3 / 2 == 1.5
import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot
from collections import defaultdict, Counter

A = [[1,2,3],
     [4,5,6]]
     
B = [[1,2],
     [3,4],
     [5,6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column1(A, j):
    return [A[i][j] for i in range(len(A))]
        
def get_column2(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]
                
r, c = shape(B)
print get_column1(A,1)
print get_column2(B,0)

def is_diagonal(i, j):
    return 1 if i == j else 0

identity_matrix = make_matrix(7, 5, is_diagonal)

def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]
#
#def vector_subtract(v, w):
#    """subtracts two vectors componentwise"""
#    return [v_i - w_i for v_i, w_i in zip(v,w)]
#
#def vector_sum(vectors):
#    return reduce(vector_add, vectors)
#
#def scalar_multiply(c, v):
#    return [c * v_i for v_i in v]
#    
#def vector_mean(vecs):
#    vecs_len = len(vecs)
#    vecs_sum = vector_sum(vecs)
#    vecs_mean = scalar_multiply(1/vecs_len, vecs_sum)
#    return vecs_mean
#
#def dot(v, w):
#    return sum(v_i * w_i for v_i , w_i in zip(v,w))
#    
#u = [1, 1, 1]
#v = [90, 120, 45]
#w = [1, 2, 3]
#
#vecs = [u, v, w]
#vecs_mean = vector_mean(vecs)
#dot_v_w = dot(v, w)

#vecs_sum = reduce(vector_add, vecs)
#print vecs_sum
#
#result = vecs[0]
#for vec in vecs[1:]:
#    result = [v_i + w_i for v_i, w_i in zip(result, vec)]
#
#print result

#v = [90, 
#     120, 
#     45]
#     
#w = [1,
#     2,
#     3]
#     
#v_w = [v_i + w_i for v_i, w_i in zip(v, w)]
#
#def double(x):
#    return 2 * x
#
#def multiply(x, y): 
#    print type(x)    
#    print x
#    print y
#    return x * y
#
#xs = [1, 2, 3, 4]
#twice_xs = [double(x) for x in xs]
#twice_xs = map(double, xs)
#
#products = map(multiply, [1,2], [4,5])    