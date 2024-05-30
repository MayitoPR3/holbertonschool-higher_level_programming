#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)
    print(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    deserialized_dict = {}
    for child in root:
        try:
            value = int(child.text)
        except ValueError:
            try:
                value = float(child.text)
            except ValueError:
                value = child.text
        deserialized_dict[child.tag] = value

    return deserialized_dict
