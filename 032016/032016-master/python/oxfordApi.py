# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 14:03:32 2016

@author: agoswami
"""

########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '2ab3a1ef04714aada6fe64c2a3728cca',
}

params = urllib.urlencode({
    # Request parameters
    'visualFeatures': 'All',
})

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1/analyses?%s" % params, "{\"Url\": \"http://as2.ftcdn.net/jpg/00/03/72/76/220_F_3727624_AA8RwMFdStlFOUCCvqwlxnuk6JP4OmAO.jpg\"}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

############ Python 3.2 #############
#import http.client, urllib.request, urllib.parse, urllib.error, base64
#
#headers = {
#    # Request headers
#    'Content-Type': 'application/json',
#    'Ocp-Apim-Subscription-Key': '{subscription key}',
#}
#
#params = urllib.parse.urlencode({
#    # Request parameters
#    'visualFeatures': 'All',
#})
#
#try:
#    conn = http.client.HTTPSConnection('api.projectoxford.ai')
#    conn.request("POST", "/vision/v1/analyses?%s" % params, "{body}", headers)
#    response = conn.getresponse()
#    data = response.read()
#    print(data)
#    conn.close()
#except Exception as e:
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))
#
#####################################