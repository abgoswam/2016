# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:25:34 2016

@author: agoswami
"""
import requests
import pandas as pd
import numpy as np
import json

#sample json from DF--------------
queryset = [{'created':"05-16-13", 'counter':1, 'id':13}, {'created':"05-16-13", 'counter':1, 'id':34}, {'created':"05-17-13", 'counter':1, 'id':12}, {'created':"05-16-13", 'counter':1, 'id':7}, {'created':"05-18-13", 'counter':1, 'id':6}]
queryset_df = pd.DataFrame.from_records(queryset).set_index('id')
q_j = queryset_df.to_json(orient='records')

#sample json from DF--------------
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}

df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df_j = df.to_json(orient='records')

#Sending to event hub-----------------
url = 'https://simplexagpmeh.servicebus.windows.net/simplexagpmeh/messages?timeout=60&api-version=2014-01'
payload = {'key':'dummy', 'key2':'dummy2'}
headers = {'ContentType': 'application/atom+xml;type=entry;charset=utf-8',
           'Host': 'simplexagpmeh.servicebus.windows.net',
           'Authorization': 'SharedAccessSignature sr=http%3a%2f%2fsimplexagpmeh.servicebus.windows.net%2f&sig=KLZPPyqRVNM6LYiy6B7Mjj70e1ElCulZJp%2fgGhGC3HY%3d&se=1507916650&skn=RootManageSharedAccessKey'}

r = requests.post(url, data = df_j, headers=headers)

#---
tokens_df = df.to_csv(index=False).strip().split('\n')
for i in range(1, len(tokens_df)):
    print tokens_df[i]
    requests.post(url, data = tokens_df[i], headers=headers)

#---
df_j_listobj = json.loads(df_j)
for item in df_j_listobj:
    print json.dumps(item)
    requests.post(url, data = json.dumps(item), headers=headers)

#----------------
#----------------
#-----------------
#--------------------------
url = 'https://simplexagpmeh.servicebus.windows.net/simplexagpmeh/messages?timeout=60&api-version=2014-01'
payload = {'key':'dummy', 'key2':'dummy2'}
headers = {'ContentType': 'application/json',
           'Host': 'simplexagpmeh.servicebus.windows.net',
           'Authorization': 'SharedAccessSignature sr=http%3a%2f%2fsimplexagpmeh.servicebus.windows.net%2f&sig=T8k9W3zAMXghAWXFceDpAU%2blKajfe4ha%2fp00dB2j8mI%3d&se=1476288568&skn=RootManageSharedAccessKey'}
r = requests.post(url, data = payload, headers=headers)

#-----------trial 2-----
url = 'https://api.github.com/some/endpoint'
payload = {'key':'dummy'}
headers = {'key': 'dummy'}
r = requests.post('http://httpbin.org/post', data = payload, headers=headers)

#-----------trial 1-----
url = 'https://api.github.com/some/endpoint'
payload = "{'key1': 'value1', 'key2': 'value2'}"
r = requests.post('http://httpbin.org/post', data = payload)

print r.text