#File: config_parser.py
#
# Description:This file contains the implementation of the ConfigureCLI class, which is responsible for parsing an XML configuration file and updating the system accordingly.


# @ Author: Benjamin Hansen
# @ Modifier: Benjamin Hansen
# @ Modifier: Sandra Barba

from menu import Menu
import os
import xml.etree.ElementTree as ET
from defusedxml.ElementTree import parse
from lxml import etree


# @ Author: Benjamin Hansen

class ConfigureCLI(Menu):
    """
    Command Line Interface configuration class.
    
    This class is responsible for parsing the XML configuration file and updating 
    the system accordingly.
    """
    
    def __init__(self) -> None:
        super().__init__()



    def find_path(self, filename):
        """
        Searches the entire file system for a file with the specified name.
        """
        for root,_, files in os.walk('/'): 
            if filename in files:
                return os.path.join(root, filename)
            
        
        return None 
    
    def validate_xml(self, xml_path, xsd_path):
        """
        Validates an XML file against an XSD schema.
        """
        xmlschema_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        xml_doc = etree.parse(xml_path)
        return xmlschema.validate(xml_doc)
    
    
    

    def configure(self, config_file_name: str) -> None:
        """
        Parses the provided XML configuration file and updates the system.

        Args:
            config_file_name (str): The name of the XML configuration file.

        """
        xsd_path = self.find_path('schema.xsd') #path to XSD file

        config_file_path = self.find_path(config_file_name)
        print("config_file_path",config_file_path)

       
        if config_file_path is None:
            print("Configuration file not found.")
            return

        if not self.validate_xml(config_file_path, xsd_path):
            print("XML file is not valid according to the schema.")
            return
        

        if config_file_path and self.validate_xml(config_file_path, xsd_path):
            tree = etree.parse(config_file_path)
            root = tree.getroot()
        
        for system in root.findall('system'):
            name = system.find('name').text
            ip = system.find('ip').text
            mac = system.find('mac').text
            ports = system.find('ports').text.split(',')
            whitelist = system.find('whitelist').text.split(',')
            
            print(f"Hostname: {name}")
            print(f"IP Address: {ip}")
            print(f"MAC Address: {mac}")
            print(f"Open Ports: {ports}")
            print(f"Whitelisted IPs: {whitelist}")

        if not self.validate_xml(config_file_path, xsd_path):
            print("XML file is not valid according to the schema.")
            return
        

        if config_file_path and self.validate_xml(config_file_path, xsd_path):
            tree = etree.parse(config_file_path)
            root = tree.getroot()
        #tree = ET.parse(config_file_path)
        #tree = parse(config_file_path)
        #root = tree.getroot()
        
            for system in root.findall('system'):
                name = system.find('name').text
                ip = system.find('ip').text
                mac = system.find('mac').text
                ports = system.find('ports').text.split(',')
                whitelist = system.find('whitelist').text.split(',')
                
                print(f"Hostname: {name}")
                print(f"IP Address: {ip}")
                print(f"MAC Address: {mac}")
                print(f"Open Ports: {ports}")
                print(f"Whitelisted IPs: {whitelist}")

                
                Menu.update_system_config(name, ip, mac, ports, whitelist)
            
        
    def configure_handler(self,config_file: str) -> None:
        

        self.configure(config_file)
        
        next_menu = self.get_user_input(">> ",self.choice_set)
        self.navigate_next_menu(next_menu)
