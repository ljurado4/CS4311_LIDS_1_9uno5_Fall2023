#File: pcap_menu.py
#
# Description: This file contains the implementation of the PcapMenu class, which is responsible for displaying and searching network packet data in a tabulated format. It provides functions to display all packets or filter packets based on specific criteria.
#
# @ Author:Benjamin Hansen
# @ Modifier: Lizbeth Jurado

import sys
import os
import webbrowser
from tabulate import tabulate
from backend.packets import PackTime

from menu import Menu



class PcapMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.menu_helper = menu.Menu()
        self.valid_search_commands = [
            "Time", "Source","Destination","Protocol", "Length", "Description"]
        self.valid_filter_options = [
            "High Severity", "Medium Severity", "Low Severity"]


    def handle_pcap_search(self):
        

        print("Handle PCAP search ")
        next_menu = self.get_user_input(">> ",self.choice_set)
        self.navigate_next_menu(next_menu)
        
    



    
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



    def print_filter_options():
        print("The filter option are as follows:")
        print("High Severity - displays only the level 3 alerts")
        print("Medium Severity - displays only the level 2 alerts")
        print("Low Severity - displays only the level 1 alerts")
        #Add more as needed

        


    def handle_pcap_search(self, user_input: str):
        """Parses the user command to determine the PCAP search criteria and then 
        calls the appropriate function to retrieve PCAP data.

        Args:
            user_input (str): The command string from the user.
        """

        match user_input:

            case _ if "Show" in user_input:
                
       
                pcap_search_type = self.menu_helper.get_user_input(
                            "Enter your search type (e.g. protocol ) \n", self.valid_search_commands)
                
                pcap_search_value = input("Enter value for search\n")
                pcap_search = [pcap_search_type,pcap_search_value]
                
                self.display_matching_pcaps(pcap_search)
                
                self.navigate_next_menu()
            
            case _ if "All" in user_input:
                
                self._print_pcap_table(self.packet_data)
                self.navigate_next_menu()
            
            case _ if "Filter" in user_input:
                self.print_filter_options()
                pcap_filter_type = self.menu_helper.get_user_input("Please enter your filter option",self.valid_filter_options)
                pcap_filter_max = input("Enter number of packets to filter")
                            #[command like High severity, number of packets to view]
                pcap_filter = [pcap_filter_type,pcap_filter_max]
                self.display_filtered_pcaps(pcap_filter)
                self.navigate_next_menu()

            
            

                
                            




                    
                    
                        
                    
                
                
        
