# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 07:38:36 2016

@author: agoswami

Code from : http://www.blog.pythonlibrary.org/2013/04/30/python-101-intro-to-xml-parsing-with-elementtree/

"""
import time
import xml.etree.ElementTree as xml
import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom


#http://stackoverflow.com/questions/17402323/use-xml-etree-elementtree-to-write-out-nicely-formatted-xml-files
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """

    "The idea is to print your Element in a string, parse it using minidom and convert it again in XML using the toprettyxml function"
    
    rough_string = xml.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def createXML(filename):
    
    root = xml.Element("zAppointments")
    
    appt = xml.Element("appointment")
    root.append(appt)
    
#    adding appt children
    begin = xml.SubElement(appt, "begin")
    begin.text = "12345678"
    
    uid = xml.SubElement(appt, "uid")
    uid.text = "040000008200E000"
 
    alarmTime = xml.SubElement(appt, "alarmTime")
    alarmTime.text = "1181572063"
    
    state = xml.SubElement(appt, "state")
 
    location = xml.SubElement(appt, "location")
 
    duration = xml.SubElement(appt, "duration")
    duration.text = "1800"
 
    subject = xml.SubElement(appt, "subject")
    
    tree = xml.ElementTree(root)
    with open(filename, "w") as fh:
        tree.write(fh)

def editXML(filename, updatedfilename):
    
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    
    for begin_time in root.iter("begin"):
        begin_time.text = time.ctime(int(begin_time.text))
    

    s = prettify(root)
    print s
    
#    tree = ET.ElementTree(root)
    with open(updatedfilename, "w") as f:
#        tree.write(f)
        f.write(s)

def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """
    
    tree = ET.ElementTree(file=xml_file)
    print tree.getroot()
    
    root = tree.getroot()
    print "tag=%s, attrib=%s" % (root.tag, root.attrib)
    
    for child in root:
        print child.tag, child.attrib
        if child.tag == "appointment":
            for step_child in child:
                print step_child.tag

    # iterate over the entire tree
    print "-" * 40
    print "Iterating using a tree iterator"
    print "-" * 40
    iter_ = tree.getiterator()
    for elem in iter_:
        print elem.tag

    # get the information via the children!
    print "-" * 40
    print "Iterating using getchildren()"
    print "-" * 40
    appointments = root.getchildren()
    for appointment in appointments:
        appt_children = appointment.getchildren()
        for appt_child in appt_children:
            print "%s=%s" % (appt_child.tag, appt_child.text)


#----------------------------------------------------------------------
if __name__ == "__main__":

    filename = "appt.xml"    
    updatedfilename = "updated.xml"   
    
    createXML(filename)
    
##    just playing around with how to read / write text to files in python   
#    f = open(filename, "ab")
#    f.writelines("abhishek\n")
#    f.writelines("goswami\n")
#    f.writelines("microsoft\n")
#    f.close()
#    
#    with open(filename, "rb") as fh:
#        s = fh.read()        
#        print "++ line:{0}".format(s)
#        for line in fh:
#            print "-- line:{0}".format(line)
    
    editXML(filename, updatedfilename)    
    
    parseXML(updatedfilename)
    
    