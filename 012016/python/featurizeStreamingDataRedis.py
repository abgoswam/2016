# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:44:07 2016

@author: agoswami
"""

import time
import redis
import numpy as np
from collections import defaultdict
from sklearn.utils import murmurhash3_32

if __name__ == "__main__":
    
    joinedfile = r'E:\hackerreborn\012016\_resources\kddcup\JoinedLogs_TrainTest_Sample1K.tsv'

#    start timer
    start = time.time()

    N = 20    
    
#   Localbox.dictionary to maintain features
    eidFeatures = defaultdict(lambda : [
        0, #0. oldest timestamp,
        0, #1. most recent timestamp,
        0, #2. (mostrecent - oldest)
        0, #3, frequency
        np.zeros(N), #4 hashingbins for cid
        np.zeros(N), #5 hashingbins for src_evt 
        np.zeros(N), #6 hashingbins for cat
        np.zeros(N), #7 hashingbins for obj
        ])    

#    Redis
    r = redis.StrictRedis(
        host='teamonestatefulml.redis.cache.windows.net', 
        port=6380, 
        db=0, 
        password='/ePnyLrKSdKOuSdBfB/6hoHIoN4TsZCv+2RXg0r7PEE=', 
        ssl=True)     
    
    with open(joinedfile, 'rb') as fh:
#        read the first line which contains headers        
        line = fh.readline()        
        
        k = 0 # index to keep track of progress
        for line in fh:
            k = k + 1
            if(k % 100 == 0):
                print k
                
            tokens = line.split("\t")
            eid = tokens[0]
            cid = tokens[1]
            timestamp = long(tokens[3])
            src_evt = tokens[4]
            cat = tokens[5]
            obj = tokens[6]

#           Localbox. recency feature    
            if eid in eidFeatures:             
                if timestamp < eidFeatures[eid][0]:
                    eidFeatures[eid][0] = timestamp
                    eidFeatures[eid][2] = (eidFeatures[eid][1] - eidFeatures[eid][0])
                elif timestamp > eidFeatures[eid][1]:
                    eidFeatures[eid][1] = timestamp
                    eidFeatures[eid][2] = (eidFeatures[eid][1] - eidFeatures[eid][0])
            else:
                eidFeatures[eid][0] = eidFeatures[eid][1] = timestamp
             
#            Redis. recency feature 
            keyoldesttimestamp  = eid + '_0'
            keylatesttimestamp  = eid + '_1'
            keytimestampdiff    = eid + '_2'
            
            valoldesttimestamp = r.get(keyoldesttimestamp)
            vallatesttimestamp = r.get(keylatesttimestamp)
            
            if(valoldesttimestamp is None or vallatesttimestamp is None):
                r.set(keyoldesttimestamp, timestamp)
                r.set(keylatesttimestamp, timestamp)
            else:
                if timestamp < long(valoldesttimestamp):
                    r.set(keyoldesttimestamp, timestamp)
                    r.set(keytimestampdiff, long(vallatesttimestamp) - timestamp)
                elif timestamp > long(vallatesttimestamp):
                    r.set(keylatesttimestamp, timestamp)
                    r.set(keytimestampdiff, timestamp - long(valoldesttimestamp))
            
#           Localbox. frequency feature
            eidFeatures[eid][3] = eidFeatures[eid][3] + 1
            
#           Redis. frequency feature
            keyfrequency = eid + '_3'
            r.incr(keyfrequency, 1)
                         
#           Localbox. monetary features (from hashing)
            eidFeatures[eid][4][murmurhash3_32(cid) % N] += 1
            eidFeatures[eid][5][murmurhash3_32(src_evt) % N] += 1
            eidFeatures[eid][6][murmurhash3_32(cat) % N] += 1
            eidFeatures[eid][7][murmurhash3_32(obj) % N] += 1
            
##           Redis. monetary features (from hashing)            
            keycid      = eid + '_4' + '_' + str(murmurhash3_32(cid) % N)
            keysrcevt   = eid + '_5' + '_' + str(murmurhash3_32(src_evt) % N)
            keycat      = eid + '_6' + '_' + str(murmurhash3_32(cat) % N)
            keyobj      = eid + '_7' + '_' + str(murmurhash3_32(obj) % N)
            
            r.incr(keycid, 1)
            r.incr(keysrcevt, 1)
            r.incr(keycat, 1)
            r.incr(keyobj, 1)
            
#    stop timer
    end = time.time()
    print "Featurization time (seconds) : {0}".format(end-start)
    
#    write output to file    
    with open('streamingFeaturesRedis.csv', 'wb') as f:
        s = 'eid,oldesttimestamp,recenttimestamp,diff,frequency'
        s += ',' + ','.join(['cid'+str(i) for i in range(N)])
        s += ',' + ','.join(['se'+str(i) for i in range(N)])
        s += ',' + ','.join(['cat'+str(i) for i in range(N)])
        s += ',' + ','.join(['obj'+str(i) for i in range(N)])
        
        f.write(s + '\n')
        
        for (key, value) in eidFeatures.items():
            f.write(key + "," + str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + ","+ str(value[3]) + ","
                + ",".join(str(s) for s in value[4]) + ","
                + ",".join(str(s) for s in value[5]) + ","
                + ",".join(str(s) for s in value[6]) + ","
                + ",".join(str(s) for s in value[7]) + "\n")
        
