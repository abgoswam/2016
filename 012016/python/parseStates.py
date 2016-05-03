# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:03:56 2016

@author: agoswami
"""

import time
import xml.etree.ElementTree as xml
import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom
import matplotlib.pyplot as plt

def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """
    
    tree = ET.ElementTree(file=xml_file)
    print tree.getroot()
    
    root = tree.getroot()
    print "tag=%s, attrib=%s" % (root.tag, root.attrib)
    
#    for child in root:
#        print child.tag, child.attrib
#        if child.tag == "appointment":
#            for step_child in child:
#                print step_child.tag

#    # iterate over the entire tree
#    print "-" * 40
#    print "Iterating using a tree iterator"
#    print "-" * 40
#    iter_ = tree.getiterator()
#    for elem in iter_:
#        print elem.tag
#
    # get the information via the children!
    print "-" * 40
    print "Iterating using getchildren()"
    print "-" * 40
    states = root.getchildren()
    for state in states:
        if((state.attrib['name'] == 'Alaska') | (state.attrib['name'] == 'Hawaii')):
            continue
        
        state_children = state.getchildren()
        data = []        
        for point in state_children:
#            print "%s=%s" % (point.tag, point.attrib)
#            print "lat:{0}, lng:{1}".format(point.attrib['lat'], point.attrib['lng'])
            data.append((point.attrib['lng'], point.attrib['lat']))
            X = [ x for (x,y) in data ]
            Y = [ y for (x,y) in data ]
            plt.plot(X,Y)

if __name__ == "__main__":
    filename = r"F:\aghackerreborn\012016\resources\states.xml"
    
    parseXML(filename)