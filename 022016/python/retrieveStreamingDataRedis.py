# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:05:26 2016

@author: agoswami
"""

import redis

if __name__ == "__main__":

    N = 20 
    
    eids = ['1', '3', '4', '5']
    
    #    Redis
    r = redis.StrictRedis(
        host='teamonestatefulml.redis.cache.windows.net', 
        port=6380, 
        db=0, 
        password='/ePnyLrKSdKOuSdBfB/6hoHIoN4TsZCv+2RXg0r7PEE=', 
        ssl=True) 
        
    for eid in eids:
        print eid

#        Keys        
        keyoldesttimestamp  = eid + '_0'
        keylatesttimestamp  = eid + '_1'
        keytimestampdiff    = eid + '_2'
        keyfrequency = eid + '_3'        
        keycids     = [eid + '_4' + '_' + str(i) for i in range(N)]  
        keysrcevts  = [eid + '_5' + '_' + str(i) for i in range(N)] 
        keycats     = [eid + '_6' + '_' + str(i) for i in range(N)] 
        keyobjs     = [eid + '_7' + '_' + str(i) for i in range(N)] 
        
##        incase i want to delete keys
#        r.delete(keyoldesttimestamp)
#        r.delete(keylatesttimestamp)  
#        r.delete(keytimestampdiff)
#        r.delete(keyfrequency)
#        for key in keycids:
#            r.delete(key)
#            
#        for key in keysrcevts:
#            r.delete(key)
#            
#        for key in keycats:
#            r.delete(key)
#            
#        for key in keyobjs:
#            r.delete(key)
            
        
#        Features (basic)
        features = []
        features.append(r.get(keyoldesttimestamp))
        features.append(r.get(keylatesttimestamp))
        features.append(r.get(keytimestampdiff))
        features.append(r.get(keyfrequency))
        
        for key in keycids:
            features.append(r.get(key))
            
        for key in keysrcevts:
            features.append(r.get(key))
            
        for key in keycats:
            features.append(r.get(key))
            
        for key in keyobjs:
            features.append(r.get(key))
            
        sanitizedFeatures = ['0' if f is None else f for f in features]
        print sanitizedFeatures
        
#        Features (pipeline)
        keys = []        
        keys.append(keyoldesttimestamp)
        keys.append(keylatesttimestamp)
        keys.append(keytimestampdiff)
        keys.append(keyfrequency)
        keys.extend(keycids)
        keys.extend(keysrcevts)
        keys.extend(keycats)
        keys.extend(keyobjs)

        pipe = r.pipeline()
        for key in keys:
            pipe.get(key)
        
        pipelinefeatures = pipe.execute()
        pipelineSanitizedFeatures = ['0' if f is None else f for f in pipelinefeatures]
        print pipelineSanitizedFeatures
        
        
        
        
        