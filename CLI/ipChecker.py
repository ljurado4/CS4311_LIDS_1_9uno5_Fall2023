import xml.etree.ElementTree as ET
import os

class ip_Checker:
    
    def __init__(self):
        
        #Get path to xml file 
        current_directory = os.getcwd()
        parent_directory = os.path.dirname(current_directory)
        file_path = os.path.join(parent_directory, 'Sample.xml')  
        
        
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        self.whitelist_values = []

        # Iterate to find system elements and whitlist ip values
        for system_element in root.findall('./system'):
            whitelist_element = system_element.find('whitelist')

            if whitelist_element is not None:
                whitelist = whitelist_element.text

                self.whitelist_values.extend(whitelist.split(','))    
        
    def ip_in_List(self, packet_ip):
        if (str(packet_ip) not in self.whitelist_values):
            return False
        else:
            return True