# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:38:07 2016

@author: abgoswam
"""

import os
import sys

# Path for spark source folder
os.environ['SPARK_HOME']="/usr/local/spark/spark-2.0.1-bin-hadoop2.7"

#if we want to use python 3
#os.environ["PYSPARK_PYTHON"]="/usr/bin/python3"

# Append pyspark  to Python Path
sys.path.append("/usr/local/spark/spark-2.0.1-bin-hadoop2.7/python")

#sys.path.append("/usr/local/spark/spark-2.0.1-bin-hadoop2.7/python/lib/py4j-0.10.3-src.zip")

#"""SimpleApp.py"""
#from pyspark import SparkContext
#
#logFile = "/usr/local/spark/spark-2.0.1-bin-hadoop2.7//README.md"  # Should be some file on your system
#sc = SparkContext("local", "Simple App")
#logData = sc.textFile(logFile).cache()
#
#numAs = logData.filter(lambda s: 'a' in s).count()
#numBs = logData.filter(lambda s: 'b' in s).count()

#print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

import pyspark

# Initialize SparkContext
sc = pyspark.SparkContext('local')
print(sc)

words = sc.parallelize(["scala","java","hadoop","spark","akka", "abhishek"])
print(words.count())

spark = pyspark.sql.SparkSession.builder\
        .master("local[*]")\
        .appName("trial app 1")\
        .getOrCreate()

dataPath = "/home/abgoswam/hackerreborn/2016/122016/python/parkinsons_updrs.csv"
diamonds = spark.read.format("csv")\
  .option("header","true")\
  .option("inferSchema", "true")\
  .load(dataPath)

diamonds.show()

#sc.stop()
