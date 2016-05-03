# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 18:01:41 2016

@author: agoswami
"""

#
# the curse of dimensionality
#


from __future__ import division
import math, random

# this isn't right if you don't from __future__ import division
def mean(x): 
    return sum(x) / len(x)
    
def distance(pointA, pointB):
    sqsum = 0
    for i, j in zip(pointA, pointB):
        sqsum += (i-j)*(i-j)
        
    return math.sqrt(sqsum)   
    
def random_point(dim):
    return [random.random() for _ in range(dim)]

def random_distances(dim, num_pairs):
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]


if __name__ == "__main__":

    dimensions = range(1, 101, 5)

    avg_distances = []
    min_distances = []

    random.seed(0)
    for dim in dimensions:
        distances = random_distances(dim, 10000)  # 10,000 random pairs
        avg_distances.append(mean(distances))     # track the average
        min_distances.append(min(distances))      # track the minimum
        print dim, min(distances), mean(distances), min(distances) / mean(distances)