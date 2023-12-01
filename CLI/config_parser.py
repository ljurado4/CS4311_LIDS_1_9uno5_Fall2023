#File: config_parser.py
#
# Description:This file contains the implementation of the ConfigureCLI class, which is responsible for parsing an XML configuration file and updating the system accordingly.


# @ Author: Benjamin Hansen
# @ Modifier: Benjamin Hansen


from menu import Menu
import os
import xml.etree.ElementTree as ET
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

    

    def validate_xml(self, xml_file_path, xsd_file_path):
        """
        Validate the XML file against the XSD schema.
        """
        xmlschema_doc = etree.parse(xsd_file_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)
    
        xml_doc = etree.parse(xml_file_path)
        return xmlschema.validate(xml_doc)


    def find_config_file_path(self, filename):
        """
        Searches the entire file system for a file with the specified name.
        """
        for root,_, files in os.walk('/'): 
            if filename in files:
                return os.path.join(root, filename)
            
        
        return None 
    
    
    def configure(self, config_file_name: str, config_dir_path: str, xsd_file_path: str) -> None:
        """
        Parses the provided XML configuration file and updates the system.

        Args:
            config_file_name (str): The name of the XML configuration file.

        """

       # config_file_path = self.find_config_file_path(config_file_name)
       # print("config_file_path",config_file_path)
        config_file_path = self.find_config_file_path(config_file_name, config_dir_path)
        if config_file_path is None:
            print("Configuration file not found.")
            return

        if not self.validate_xml(config_file_path, xsd_file_path):
            print("XML file is not valid according to the schema.")
            return
    

        tree = ET.parse(config_file_path)
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

            
            Menu.update_system_config(name, ip, mac, ports, whitelist)
            
        
    def configure_handler(self,config_file: str) -> None:
        
        
        self.configure(config_file)
        
        next_menu = self.get_user_input(">> ",self.choice_set)
        self.navigate_next_menu(next_menu)