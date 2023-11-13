################################################################################
# File: config_parser.py
# Description: This file contains the implementation of the ConfigureCLI class,
#              which is responsible for parsing an XML configuration file and
#              updating the system accordingly.
#
################################################################################

import menu
import os
import xml.etree.ElementTree as ET

class ConfigureCLI:
    """
    Command Line Interface configuration class.
    
    This class is responsible for parsing the XML configuration file and updating 
    the system accordingly.
    """

    def configure(self, config_file_name: str) -> None:
        """
        Parses the provided XML configuration file and updates the system.

        Args:
            config_file_name (str): The name of the XML configuration file.

        """
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(dir_path, config_file_name)
        tree = ET.parse(config_path)
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

            menu_instance = menu.Menu()
            menu_instance.update_system_config(name, ip, mac, ports, whitelist)
            
        # Move to the next menu selection 
        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ", menu_helper.choice_set)
        menu.Menu().navigate_next_menu(next_menu)
