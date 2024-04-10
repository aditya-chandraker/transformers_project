import xml.etree.ElementTree as ET
tree = ET.parse('annotations.xml')
root = tree.getroot()
print(root)