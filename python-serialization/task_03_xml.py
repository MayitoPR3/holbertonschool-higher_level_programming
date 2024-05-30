#!/usr/bin/python3
"""module for the Task 3"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """defines the serialization to xml"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """defines the deserialization from xml"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
