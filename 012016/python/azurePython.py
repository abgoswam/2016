# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 02:14:18 2016

@author: agoswami
"""

#import sys
#print '\n'.join(sys.path)

import pandas as pd
from azure.storage.table import TableService
import datetime as dt

table_service = TableService(account_name='teamonestorage', account_key='n0JURznA9nCqw897uFG3YKRg3yIWQ6CAbQ3Rg3Ygp/+fZllj3IlU26EmG9d2TLRQBC24GSEMuT2V2jy5qrxiMQ==', protocol='http')

##query for a set of entities
#utc = dt.datetime.utcnow()
#utcSub30 = utc - dt.timedelta(minutes=30)
#filterQuery = "PartitionKey gt '{0}'".format(utcSub30)

filterQuery = "PartitionKey eq '{0}'".format('2016-01-19 18:11:50.755')

next_pk=None
next_rk=None

taskEntities = []
#Using continuation token
while True:
    tasks = table_service.query_entities('teamonestatefulml', 
                                     filterQuery, 
                                     next_partition_key=next_pk, 
                                     next_row_key=next_rk,
                                     top=1000)
                                     
    for task in tasks:
        taskEntities.append(task)
   
    if hasattr(tasks, 'x_ms_continuation'):
        x_ms_continuation = getattr(tasks, 'x_ms_continuation')
        next_pk = x_ms_continuation['nextpartitionkey']
        next_rk = x_ms_continuation['nextrowkey']
    else:
        break  

df_details = pd.DataFrame([('AzTable', len(taskEntities))], columns=['Source', 'EntityCount'])

# Return value must be of a sequence of pandas.DataFrame
print  df_details