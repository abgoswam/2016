# -*- coding: utf-8 -*-
"""
Created on Sat May 14 19:04:00 2016

@author: agoswami
"""

import math
import random
import collections as coll
import matplotlib.pyplot as plt

#def bucketize(point, bucket_size):
#    return bucket_size * math.floor(point / bucket_size)
##    return math.floor(point / bucket_size)
#
#def make_histogram(points, bucket_size):
#    return coll.Counter(bucketize(point, bucket_size) for point in points)
#
#def plot_histogram(points, bucket_size, title=""):
#    histogram = make_histogram(points, bucket_size)
#    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
#    plt.title(title)
#    plt.show()
##    
###for i in range(15):
###    print bucketize(i, 4)
##    
##random.seed(0)
##
##uniform = [200 * random.random() - 100 for _ in range(10000)]
###normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]
##
##plot_histogram(uniform, 50, "Uniform Histogram")
#
#def random_normal():
#    return random.random()
#    
#xs = [random_normal() for _ in range(10000)]
#ys1 = [ x + random_normal() / 2 for x in xs]
#ys2 = [-x + random_normal() / 2 for x in xs]
#
#plot_histogram(ys1, 10, "ys1")
#plot_histogram(ys2, 10, "ys2")

def correlation_matrix(data):
    
    _, num_columns = shape(data)
    
    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))
        
    return make_matrix(num_columns, num_columns, matrix_entry)
