# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:54:22 2016

@author: agoswami
"""

import redis
    
r = redis.StrictRedis(
    host='teamonestatefulml.redis.cache.windows.net', 
    port=6380, 
    db=0, 
    password='/ePnyLrKSdKOuSdBfB/6hoHIoN4TsZCv+2RXg0r7PEE=', 
    ssl=True) 
    
#basic redis    
r.set('foo', 'bar')
retval = r.get('foo2')
print retval 
r.incr('_abcd',1)
retval = r.get('_abcd')
print retval
r.incr('_abcd',1)
retval = r.get('_abcd')
print retval 

#hash set

#HSET user:1000 name "John Smith"
#HSET user:1000 email "john.smith@example.com"
#HSET user:1000 password "s3cret"
#To get back the saved data use HGETALL:
#
#
#HGETALL user:1000
#You can also set multiple fields at once:
#
#
#HMSET user:1001 name "Mary Jones" password "hidden" email "mjones@example.com"
#If you only need a single field value that is possible as well:
#
#HGET user:1001 name => "Mary Jones"

#HSET user:1000 visits 10
#HINCRBY user:1000 visits 1 => 11
#HINCRBY user:1000 visits 10 => 21
#HDEL user:1000 visits
#HINCRBY user:1000 visits 1 => 1


r.hset('user:1000', 'name', 'John Smith')
r.hset('user:1000', 'email', 'john.smith@example.com')
r.hset('user:1000', 'password', 's3cret')
user_1000 = r.hgetall('user:1000')
print "{0}:{1}:{2}".format(user_1000['name'], user_1000['email'], user_1000['password'])

mapping = {"name" : "Mary Jones", "password" : 'hidden',  "email" : 'mjones@example.com'}
r.hmset('user:1001', mapping)
user_1001 = r.hgetall('user:1001')
print "{0}:{1}:{2}".format(user_1001['name'], user_1001['email'], user_1001['password'])

user_1001_name = r.hget('user:1001', 'name')
print user_1001_name

r.hset('user:1000', 'visits', 20)
r.hincrby('user:1000', 'visits', 10)
user_1000_visits = r.hget('user:1000', 'visits')
print user_1000_visits




