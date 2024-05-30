import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Create root element
    root = ET.Element("data")

    # Iterate through dictionary items
    for key, value in dictionary.items():
        # Create child element for each key-value pair
        child = ET.SubElement(root, key)
        # Set text of child element to string representation of value
        child.text = str(value)

    # Create ElementTree object
    tree = ET.ElementTree(root)

    # Write XML tree to file
    tree.write(filename)


def deserialize_from_xml(filename):
    # Parse XML file
    tree = ET.parse(filename)

    # Get root element
    root = tree.getroot()

    # Initialize empty dictionary
    deserialized_dict = {}

    # Iterate through child elements
    for child in root:
        # Add key-value pair to dictionary, converting value to appropriate type
        deserialized_dict[child.tag] = convert_value(child.text)

    return deserialized_dict


def convert_value(value):
    # Try to convert value to integer
    try:
        return int(value)
    # If conversion fails, try to convert to float
    except ValueError:
        try:
            return float(value)
        # If conversion fails again, return value as string
        except ValueError:
            return value