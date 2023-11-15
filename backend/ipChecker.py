# File: ipChecker.py
#
# Description: Defines a Python class named ip_Checker that provides a method ip_in_List for checking if a given IP address is in a whitelist defined in a configuration dictionary.
#
# @ Author: 
# @ Modifier: Alejandro Hernandez

import xml.etree.ElementTree as ET

import os
import sys

# @ Modifier: Alejandro Hernandez

class ip_Checker:
    configuration = {}
    
    def ip_in_List(self, packet_ip):
        
        for k,dic in ip_Checker.configuration.items():
            if packet_ip in dic['whitelist']:
                return True
        return False