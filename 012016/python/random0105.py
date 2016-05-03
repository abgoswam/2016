# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 08:00:27 2016

@author: agoswami
"""

from collections import defaultdict
from collections import Counter

city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)

for state, city in city_list:
    cities_by_state[state].append(city)
    
for state, cities in cities_by_state.iteritems():
    print state, ', '.join(cities)
    
    
myCounter = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print myCounter

# print the 2 most common words and their counts
for word, count in myCounter.most_common(2):
    print word, count
