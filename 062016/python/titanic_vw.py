# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:58:16 2016

@author: agoswami
"""

import csv

#---------------- train ----------------------

#infilename = r'E:\hackerreborn\mlhackerdatasets\01_titanic\titanic_train.csv'
#outfilename = r'E:\hackerreborn\2016\062016\python\out_train.vw'
#
#with open(infilename, 'rb') as infile, open(outfilename, "wb") as outfile:   
##    read header
#    infile.readline()
#    
#    csvreader = csv.reader(infile)
#    for line in csvreader:
#        print line
#        
#        vw_line = ""
#        if str(line[1]) == "1":
#            vw_line += "1 '"
#        else:
#            vw_line += "-1 '"
#            
#        vw_line += str(line[0]) + " |f "        
#        vw_line += "passenger_class_"+ str(line[2]) +" "
#        vw_line += "last_name_" + (line[3].split(",")[0]).replace(" ", "_") + " "
#        vw_line += "sex_"+ str(line[4]) +" "
#        if len(str(line[5])) > 0:
#            vw_line += "age:" + str(line[5]) + " "
#        
#        vw_line += "siblings_onboard:" + str(line[6]) + " "
#        vw_line += "family_members_onboard:" + str(line[7]) + " "
#        vw_line += "embarked_" + str(line[11]) + " "
#        outfile.write(vw_line[:-1] + "\n")

#---------------- test ----------------------

#infilenametest = r'E:\hackerreborn\mlhackerdatasets\01_titanic\titanic_test.csv'
#outfilenametest = r'E:\hackerreborn\2016\062016\python\out_test.vw'
#
#with open(infilenametest, 'rb') as infile, open(outfilenametest, "wb") as outfile:    
##    read header
#    infile.readline()
#    
#    csvreader = csv.reader(infile)
#    for line in csvreader:
#        print line
#        
#        vw_line = "1 '"
#            
#        vw_line += str(line[0]) + " |f "        
#        vw_line += "passenger_class_"+ str(line[1]) +" "
#        vw_line += "last_name_" + (line[2].split(",")[0]).replace(" ", "_") + " "
#        vw_line += "sex_"+ str(line[3]) +" "
#        if len(str(line[4])) > 0:
#            vw_line += "age:" + str(line[4]) + " "
#        
#        vw_line += "siblings_onboard:" + str(line[5]) + " "
#        vw_line += "family_members_onboard:" + str(line[6]) + " "
#        vw_line += "embarked_" + str(line[10]) + " "
#        outfile.write(vw_line[:-1] + "\n")

#-------------------- kaggle predictions -----------------------

infilenamepreds = r'E:\hackerreborn\2016\062016\python\test_predictions.txt'
outfilenamepreds = r'E:\hackerreborn\2016\062016\python\kaggle.txt'

with open(infilenamepreds, "r") as infile, open(outfilenamepreds, "wb") as outfile:
  outfile.write("PassengerId,Survived\n")
  
  for line in infile.readlines():
    kaggle_line = str(line.split(" ")[1]).replace("\n","")

    if str(int(float(line.split(" ")[0]))) == "1":
      kaggle_line += ",1\n"
    else:
      kaggle_line += ",0\n"

    outfile.write(kaggle_line)

#--------------------------------------------------------------------------------------    
#    line = f.readline()
#    print line
#    
#    line = f.readline().strip()
#    print line    
#    line = f.readline().strip()
#    print line
#    
#    csvreader = csv.reader(f)
#    line = csvreader.next()
#    print line    
#    line = csvreader.next()
#    print line
#    
#    print "----------"

#import pandas as pd
#
#df = pd.read_csv(r'E:\hackerreborn\mlhackerdatasets\01_Titanic\titanic_train.csv')

#filename = r'E:\hackerreborn\2016\062016\_resources\coffee.csv'
#
#with open(filename, 'rb') as f:
#    line = f.read()
#    print line
#    
#print "-------------"
#
##Python’s “readlines” reads everything in the text file and has them in a list of lines. 
##Here is how to use Python’s “readlines”
#with open(filename, 'rb') as f:
#    lines = f.readlines()
#
#    for line in lines:
#        print line
#    
#    print lines
#
#print "-------------"
#    
##A better way to read a text file that is memory-friendly is to read the file line by line, that is one line at a time. 
##Python has (at least) two ways to read a text file line by line easily.    
#with open(filename, 'rb') as f:
#    line = f.readline()
#    
#    ## If the file is not empty keep reading line one at a time
#    ## till the file is empty
#    while line:
#        print line
#        line = f.readline()
#
#print "-------------"