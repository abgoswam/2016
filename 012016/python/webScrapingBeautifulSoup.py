# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:23:03 2016

@author: agoswami
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_category_links(section_url):
    soup = make_soup(section_url)
    
    boccat = soup.find("dl", "boccat")
    category_links = [BASE_URL + dd.a["href"] 
                for dd in boccat.findAll("dd")]
    return category_links

def get_category_winner(category_url):
    soup = make_soup(category_url)
    
    category = soup.find("h1", "headline").string
    category_url = winners = runnerups = None
    if category is not None:    
        category = category.encode('utf-8').strip()
        winners = [h2.string for h2 in soup.findAll("h2", "boc1")]
        runnerups = [h2.string for h2 in soup.findAll("h2", "boc2")]
    
    return {"category": category,
            "category_url": category_url,
            "winners": winners,
            "runnersups": runnerups}
            
if __name__ == "__main__":
    
    section_url = 'http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228'
    category_links = get_category_links(section_url)
    
    for categorylink in category_links:
        info = get_category_winner(categorylink)
        print "{0} : {1}".format(info['category'], info['winners'])
            
    guysfromrolla = 'http://www.4guysfromrolla.com/'
    soup = make_soup(guysfromrolla)

    links = []    
    for a in soup.findAll("a"):
        if a.has_attr("href") and len(a["href"]) > 0:
            links.append(a["href"])
            
#    equivalent code using functional tools
    valid = filter(lambda x : x.has_attr("href") and len(a["href"]) > 0, soup.findAll("a"))
    links = [a["href"] for a in valid]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    