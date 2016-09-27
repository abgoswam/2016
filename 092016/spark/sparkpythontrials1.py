# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:57:51 2016

@author: agoswami
"""

import os
import sys

# Path for spark source folder
#os.environ['SPARK_HOME'] = r"D:\spark-2.0.0-bin-hadoop2.7"

# Append pyspark  to Python Path
sys.path.append("D:\spark-2.0.0-bin-hadoop2.7\python")
sys.path.append("D:\spark-2.0.0-bin-hadoop2.7\python\lib\py4j-0.10.1-src.zip")

try:
    import pyspark
    print ("Successfully imported Spark Modules")

except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)

# Initialize SparkContext
sc = pyspark.SparkContext('local')
print(sc)

words = sc.parallelize(["scala","java","hadoop","spark","akka", "abhishek"])
print(words.count())

#sqlContext = pyspark.sql.SQLContext(sc)\
#    .config("spark.sql.warehouse.dir", "file:///c:/tmp")    
#print(sqlContext)

spark = pyspark.sql.SparkSession.builder\
        .master("local[*]")\
        .appName("trial app 1")\
        .config('spark.sql.warehouse.dir', 'file:///C:/tmp') \
        .getOrCreate()
 
dataPath = "export.csv"
diamonds = spark.read.format("csv")\
  .option("header","true")\
  .option("inferSchema", "true")\
  .load(dataPath)
  
diamonds.show()
sc.stop()