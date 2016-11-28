# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:47:17 2016

@author: abgoswam
"""

import pandas as pd
import random
import json
import collections

data = {'reward':[10, 11,12],
        'actionname':['x', 'y', 'z'],
        'age':[70, 40, 50],
        'Scored Labels':[10, 9, 20]
}

df = pd.DataFrame(data)