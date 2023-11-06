#pcap_menu.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import menu
from tabulate import tabulate
#import packets
from backend import packets
from backend import alerts_manager
#from backend import db 

"""
NOTE: Include that tabulate needs to be installed from command terminal
"""
class PcapMenu:

    """
    NOTE: The line below will only capture a set # of
    packets, Used only for testing, review packets.py 
    and refactor for practical use
    """
    #packet_data.run_sniffer()
    
    """
    packet_data = [
        {
            "Severity" : "Medium Severity",
            "Time": "2023-09-16 12:01:23.456789",
            "Source": "192.168.1.2",
            "Destination": "192.168.1.100",
            "Protocol": "TCP",
            "Length": 64,
            "Description": "TCP Handshake SYN"
        },
        {
            "Severity" : "Low Severity",
            "Time": "2023-09-16 12:01:23.456990",
            "Source": "192.168.1.100",
            "Destination": "192.168.1.2",
            "Protocol": "UDP",
            "Length": 64,
            "Description": "UDP Handshake SYN, ACK"
        },
        {
            "Severity" : "High Severity",
            "Time": "2023-09-16 12:02:00.000000",
            "Source": "192.168.1.3",
            "Destination": "192.168.1.101",
            "Protocol": "ICMP",
            "Length": 32,
            "Description": "Ping Request"
        },
        {
            "Severity" : "Medium Severity",
            "Time": "2023-09-16 12:02:00.100000",
            "Source": "192.168.1.101",
            "Destination": "192.168.1.3",
            "Protocol": "ICMP",
            "Length": 32,
            "Description": "Ping Reply"
        },
        {
            "Severity" : "High Severity",
            "Time": "2023-09-16 12:02:05.678910",
            "Source": "192.168.1.4",
            "Destination": "192.168.1.5",
            "Protocol": "TCP",
            "Length": 128,
            "Description": "HTTP GET Request"
        },
        {
            "Severity" : "Low Severity",
            "Time": "2023-09-16 12:02:05.789123",
            "Source": "192.168.1.5",
            "Destination": "192.168.1.4",
            "Protocol": "TCP",
            "Length": 256,
            "Description": "HTTP 200 OK Response"
        }]
    """
    
    def __init__(self) -> None:
        self.menu_helper = menu.Menu()
        self.valid_search_commands = [
            "Time", "Source","Destination","Protocol", "Length", "Description"]
        self.valid_filter_options = [
            "High Severity", "Medium Severity", "Low Severity"]
        self.identifier_list = alerts_manager.AlertManager.identifierList
        self.alert_list = alerts_manager.AlertManager.sharedAlerts

    def navigate_next_menu(self):
        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)
        
    
    
    def _print_pcap_table(self, pcap_dictionary: dict):
        """
        Print a tabulated representation of the given pcap data.
        
        Args:
        - pcap_dictionary (dict): Dictionary containing pcap data.
        """
        
        header = self.valid_search_commands
        data = [list(pcap.values()) for pcap in pcap_dictionary]
        table = tabulate(data, headers=header, tablefmt="fancy_grid")
        print(table)

    
    def display_matching_pcaps(self, search_command: list):
        """
        Display pcaps that match the given search command and target value.

        Args:
         full_command (str): The complete search command input.
         search_command (str): The specific command to match.

        """
        
        target_value = search_command[-1]
        search = search_command[0]

        matching_pcaps = []

        for pcap in self.packet_data:
            for attribute, value in pcap.items():
                # Check if the current attribute matches the search command and its value matches the target value
                if attribute == search and value == target_value:
                    matching_pcaps.append(pcap)
                    break  

        if matching_pcaps:
            self._print_pcap_table(matching_pcaps)
        else:
            # Print a message if no matching pcap is found
            print("Unable to locate the specified PCAP file")

    def display_filtered_pcaps(self,filter_command: list):
        #[command like High severity, number of packets to view]
        command = filter_command[0]
        max_pcaps = filter_command[-1]

        filtered_pcaps = []

        for pcap in self.packet_data:
            for attribute, value in pcap.items():
                # Check if the current attribute matches the search command and its value matches the target value
                if attribute == command and value >= max_pcaps:
                    filtered_pcaps.append(pcap)
                    value += 1
                    break



    def print_filter_options(self):
        print("The filter option are as follows:")
        print("High Severity - displays only the level 3 alerts")
        print("Medium Severity - displays only the level 2 alerts")
        print("Low Severity - displays only the level 1 alerts")
        #Add more as needed

        


    def handle_pcap_search(self, identifier: str):
        """Parses the user command to determine the PCAP search criteria and then 
        calls the appropriate function to retrieve PCAP data.

        Args:
            user_input (str): The command string from the user.
        """
        found = False
        for dict in self.identifier_list:
            if identifier in dict:
                print(dict[identifier])
                found = True
                break
        if not found:
            pass
    
    def print_ident(self):
        print("IDENTIFIERS")
        print(self.identifier_list)

    def print_alerts(self):
        print("BEGIN ALERTS")
        print(self.alert_list)
    
            
            

                
                            




                    
                    
                        
                    
                
                
        
