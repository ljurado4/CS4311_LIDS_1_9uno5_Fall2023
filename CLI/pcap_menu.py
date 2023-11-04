################################################################################
# File: pcap_menu.py
#
# Version: [5.0]
#
# Description: This file contains the implementation of the PcapMenu class, which
#              is responsible for displaying and searching network packet data in
#              a tabulated format. It provides functions to display all packets
#              or filter packets based on specific criteria.
#
# Modification History:
# [11/01/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Implement the '_print_pcap_table' method to print pcap data in a tabulated format.
# - [Task 2]: Implement the 'display_matching_pcaps' method to display pcaps that match the search criteria.
# - [Task 3]: Implement the 'handle_pcap_search' method to parse user commands and retrieve PCAP data.
#
################################################################################

import menu
from tabulate import tabulate
from backend import packets

"""
NOTE: Include that tabulate needs to be installed from the command terminal
"""
class PcapMenu:
    packet_data = []

    packet_data = packets.PackTime()
    """
    NOTE: The line below will only capture a set # of
    packets, Used only for testing, review packets.py 
    and refactor for practical use
    """
    # packet_data.run_sniffer()
    
    def __init__(self) -> None:
        self.menu_helper = menu.Menu()
        self.valid_search_commands = [
            "Time", "Source","Destination","Protocol", "Length", "Description"]

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

    def handle_pcap_search(self, user_input: str):
        """Parses the user command to determine the PCAP search criteria and then 
        calls the appropriate function to retrieve PCAP data.

        Args:
            user_input (str): The command string from the user.
        """

        match user_input:
            case _ if "Show" in user_input:
                pcap_search_type = self.menu_helper.get_user_input(
                            "Enter your search type (e.g., protocol) \n", self.valid_search_commands)
                pcap_search_value = input("Enter value for search\n")
                pcap_search = [pcap_search_type, pcap_search_value]
                self.display_matching_pcaps(pcap_search)
                self.navigate_next_menu()
            
            case _ if "All" in user_input:
                self._print_pcap_table(self.packet_data)
                self.navigate_next_menu()
