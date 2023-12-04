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


#Checks if an ip is in the whitelist    
    def ip_in_List(self, packet_ip):
        
        for k,dic in ip_Checker.configuration.items():
            white_list =  set(dic['whitelist'].split(','))
            # print("Whitelist",white_list)
            # print("packet_ip",packet_ip)
            if packet_ip in white_list:
                return True
            # sys.exit(0)
        return False