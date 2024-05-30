#!/usr/bin/python3
"""Module for Serializing and Deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """defines serialize to xml"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """defines deserialize from xml and reconstruct the dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    reconstructed_dict = {}
    for child in root:
        try:
            value = int(child.text)
        except ValueError:
            try:
                value = float(child.text)
            except ValueError:
                value = child.text
        reconstructed_dict[child.tag] = value

    return reconstructed_dict
