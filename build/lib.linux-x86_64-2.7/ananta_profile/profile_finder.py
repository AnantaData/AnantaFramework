

__author__ = 'lakmal'

from lxml import etree
import xml.etree.ElementTree as ET

def getProfileTag(fileName,no):
    xPath = '//Profile[@No="'+no+'"]'
    fileLoc = "/home/lakmal/PycharmProjects/AnantaUi/AnantaWorkspace/"
    tree = etree.parse(fileLoc+fileName)
    return ET.tostring(tree.xpath(xPath)[0])

def setProfileTag(fileName,no, tag):
    xPath = "//Profiles"
    fileLoc = "/home/lakmal/PycharmProjects/AnantaUi/AnantaWorkspace/"
    tree = etree.parse(fileLoc+fileName)
    element = tree.xpath(xPath)[0]
    for child in element.findall('Profile'):
        print child.get('No')
        if(child.get('No')==str(no)):
            element.remove(child)
    elem = etree.XML(tag)
    element.append(elem)
    '''root = etree.Element("root")
    for child in root.findall('Profiles'):
        child = element
        break'''
    f = open(fileLoc+fileName, 'w')
    f.write(etree.tostring(tree, pretty_print=True))
    f.close()
