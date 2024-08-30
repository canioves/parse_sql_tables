from lxml import etree
import os

class Xml_parser:
    def __init__(self, file_dir):
        self.file_dir = file_dir
    
        
    def get_sql(self):
        queries = []
        xml = etree.parse(self.file_dir)
        root = xml.getroot()
        for elem in root.findall("DataSources/SqlDataSource", root.nsmap):
            query = elem.attrib['SelectCommand']
            queries.append(query)
        return queries