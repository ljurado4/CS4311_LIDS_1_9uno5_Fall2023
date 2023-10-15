#ipChecker.py

import xml.etree.ElementTree as ET

import os
import sys

#current_directory = os.getcwd()
#parent_directory = os.path.dirname(current_directory)
#file_path = os.path.join(parent_directory, 'app.py')

#import sys
#sys.path.append('file_path')  # Add the path to the directory containing the module

#from .. import app

#import app

#current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (my_repo directory)
#parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

# Add the parent directory to sys.path
#sys.path.append(parent_directory)

# Now you can import app.py as a module
#import app

class ip_Checker:
    
    def __init__(self):
        
        #self.data = app.upload_xml_data()

        #ip_addresses = []

        #for system_data in data['network']['system']:
         #   whitelist_ips = system_data['whitelist'].split(',')
          #  ip_addresses.extend(whitelist_ips)
    
        
        
        #Get path to xml file 

        current_file_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_file_directory)
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