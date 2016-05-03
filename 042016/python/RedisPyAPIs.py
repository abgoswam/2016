# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 10:12:23 2016

@author: agoswami
"""

import redis

if __name__ == "__main__":
    
    entityid = 'userX'
    
        # Redis. Trial
    db = redis.StrictRedis(
                    host='simplexagredistrial.redis.cache.windows.net', 
                    port=6380, 
                    db=0, 
                    password='m4JD03/PtZjrZ6rXzQ5wHY44WZHpfj2KzJr+AtMXhi4=', 
                    ssl=True)
                    
    
#    keys        
    keyRecencyMin       = entityid + '_RecencyMin'
    keyRecencyMax       = entityid + '_RecencyMax'
    keyFrequencyCount   = entityid + '_FrequencyCount'   
    keyMonetaryValue    = entityid + '_MonetaryValue'     
    keyUniqueHours      = entityid + '_UniqueHours';
    keyUniqueDays       = entityid + '_UniqueDays';
    keyUniqueWeeks      = entityid + '_UniqueWeeks';     
    
    keys = []        
    keys.append(keyRecencyMin)
    keys.append(keyRecencyMax)
    keys.append(keyFrequencyCount)
    keys.append(keyMonetaryValue)
    
##    mget
#    mgetfeatures = db.mget(keys)
#    print mgetfeatures
#    
#    print db.scard(keyUniqueHours)
#    print db.scard(keyUniqueDays)
#    print db.scard(keyUniqueWeeks)
    
    pipe = db.pipeline()
    for key in keys:
        pipe.get(key)
        
    pipe.scard(keyUniqueHours)
    pipe.scard(keyUniqueDays)
    pipe.scard(keyUniqueWeeks)
    
    values = pipe.execute()
    print values