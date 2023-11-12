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
    configuration = {}
    
    def ip_in_List(self, packet_ip):
        
        for k,dic in ip_Checker.configuration.items():
            if packet_ip in dic['whitelist']:
                return True
        return False