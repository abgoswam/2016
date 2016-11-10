# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 08:38:00 2016

@author: agoswami
"""

import csv
import uuid
import urllib2
import json 
import requests
import threading
import logging

data =  {

        "Inputs": {

                "input1":
                {
                    #"ColumnNames": ["Label", "EventId", "EventCounter", "VideoId", "ArticleChannel", "ReferrerDomain", "DeviceType", "ClientId", "Source", "Rank", "VideoClickCount_1", "VideoNoClickCount_1", "VideoCTR_1", "VideoClickCount_0.999995", "VideoNoClickCount_0.999995", "VideoCTR_0.999995", "VideoClickCount_0.99995", "VideoNoClickCount_0.99995", "VideoCTR_0.99995", "VideoClickCount_0.9995", "VideoNoClickCount_0.9995", "VideoCTR_0.9995", "VideoClickCount_0.999", "VideoNoClickCount_0.999", "VideoCTR_0.999", "VideoCTRVelocity_0.999995-1", "VideoCTRVelocity_0.99995-0.999995", "VideoCTRVelocity_0.9995-0.99995", "VideoCTRVelocity_0.999-0.9995", "VideoCTRLambda_0", "VideoCTRLambda_1", "VideoCTRLambda_50", "VideoCTRLambda_200", "ArticleChannelVideoClickCount_1", "ArticleChannelVideoNoClickCount_1", "ArticleChannelVideoCTR_1", "ArticleChannelVideoClickCount_0.999995", "ArticleChannelVideoNoClickCount_0.999995", "ArticleChannelVideoCTR_0.999995", "ArticleChannelVideoClickCount_0.99995", "ArticleChannelVideoNoClickCount_0.99995", "ArticleChannelVideoCTR_0.99995", "ArticleChannelVideoClickCount_0.9995", "ArticleChannelVideoNoClickCount_0.9995", "ArticleChannelVideoCTR_0.9995", "ArticleChannelVideoClickCount_0.999", "ArticleChannelVideoNoClickCount_0.999", "ArticleChannelVideoCTR_0.999", "ArticleChannelVideoCTRVelocity_0.999995-1", "ArticleChannelVideoCTRVelocity_0.99995-0.999995", "ArticleChannelVideoCTRVelocity_0.9995-0.99995", "ArticleChannelVideoCTRVelocity_0.999-0.9995", "ArticleChannelVideoCTRLambda_0", "ArticleChannelVideoCTRLambda_1", "ArticleChannelVideoCTRLambda_50", "ArticleChannelVideoCTRLambda_200", "scoredlabels", "actionprobability"],
                    "ColumnNames": ["label", "eventid", "eventcounter", "videoid", "articlechannel", "referrerdomain", "devicetype", "clientid", "source", "rank", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "n10", "n11", "n12", "n13", "n14", "n15", "n16", "n17", "n18", "n19", "n20", "n21", "n22", "n23", "n24", "n25", "n26", "n27", "n28", "n29", "n30", "n31", "n32", "n33", "n34", "n35", "n36", "n37", "n38", "n39", "n40", "n41", "n42", "n43", "n44", "n45", "n46", "scoredlabels", "actionprobability"],
                    "Values": None
                },        
        },
       "GlobalParameters": {}
    }

url = 'https://ussouthcentral.services.azureml.net/workspaces/ec223f662aa543f3a6d2003c215d9792/services/656320e0d7d4422c9b7860433e39ff20/execute?api-version=2.0&details=true'
api_key = 'mklgYg/OfRPlnEdkwcB7EVdZ9DFibApBBCW36QONOyN/Gve42CA/5yl9YpRkOzUOMKYXsMI280VN0mcWC2tCqQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    
filename = r'F:\Complex\Trials\TLC_data\train.csv'


logging.basicConfig(level=logging.ERROR,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker(k):
    fileout = r'F:\Complex\Trials\_myscripts\traineventsinfo' + '_' + str(k) + '.csv'
    with open(filename, 'rb') as f, \
        open(fileout, 'wb', 0) as fo: 

        # creating the csv reader
        csvreader = csv.reader(f)
    
        header = csvreader.next()
        #print "header : {0}".format(header)
            
        # iterate over the csvreader
        idx = 0
        for line in csvreader:
            idx += 1
            
            if (idx < k * 1):
                continue
            elif (idx >= (k+1) * 1):
                break
            else:
#                so we are dealing with rows between   k <= idx < (k+1) 
                guid = uuid.uuid4()
                label = int(line[0])
        
                fo.writelines("{0},{1}\n".format(line[1], line[2])) # print EventCounter, VideoId. Soon we will insert GUID here
                
                line.insert(1, str(guid)) 
                line.append('0.2') # scored labels
                line.append('0.8') # action probability 
                     
                if label > 0:
                    line[0] = '0'
                    
                    data['Inputs']['input1']['Values'] = [line]
                    body = str.encode(json.dumps(data))
                    
                    try:
                        requests.post(url, data = body, headers=headers)
                    except requests.exceptions.RequestException as e:
                        logging.error(e)
                        continue
                    
        #            req = urllib2.Request(url, body, headers) 
        #            response = urllib2.urlopen(req)
        #            result = response.read()
        #            print(result)
                    
                line[0] = str(label)
                data['Inputs']['input1']['Values'] = [line]
                body = str.encode(json.dumps(data))
        
                try:
                    requests.post(url, data = body, headers=headers)
                except requests.exceptions.RequestException as e:
                    logging.error(e)
                    continue
            
        #        req = urllib2.Request(url, body, headers) 
        #        response = urllib2.urlopen(req)
        #        result = response.read()
        #        print(result)

            
threads = []
for i in range(100):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()           
            
