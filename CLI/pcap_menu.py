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
# Author : Lizbeth Jurado
#
################################################################################
# File: pcap_menu.py

import sys
import os
import webbrowser
from tabulate import tabulate
from backend import packets
import menu  # Import the Menu class from menu.py

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class PcapMenu:
    def __init__(self) -> None:
        self.menu_helper = menu.Menu()
        self.valid_search_commands = ["Time", "Source", "Destination", "Protocol", "Length", "Description"]
        self.packet_data = packets.PackTime().packet_list

    def navigate_next_menu(self, menu_option_selected: str) -> None:
        """Navigate to the next menu based on the user's selection"""
        match menu_option_selected:
            case _ if "Show" in menu_option_selected:
                # Handle show command
                pcap_search_type = self.menu_helper.get_user_input(
                    "Enter your search type (e.g., protocol) \n", self.valid_search_commands)
                pcap_search_value = input("Enter value for search\n")
                pcap_search = [pcap_search_type, pcap_search_value]
                self.display_matching_pcaps(pcap_search)
                self.navigate_next_menu(self.menu_helper.get_user_input(">> ", self.menu_helper.choice_set))
            
            case _ if "All" in menu_option_selected:
                # Handle all command
                self._print_pcap_table(self.packet_data)
                self.navigate_next_menu(self.menu_helper.get_user_input(">> ", self.menu_helper.choice_set))

            case _ if "Show HTML" in menu_option_selected:
                # Handle show HTML command
                self.display_pcap_in_html()
                self.navigate_next_menu(self.menu_helper.get_user_input(">> ", self.menu_helper.choice_set))

    def display_pcap_in_html(self):
        print("Displaying PCAP data in the web browser...")
        webbrowser.open('http://127.0.0.1:5000/show_pcap')

    def _print_pcap_table(self, pcap_dictionary: dict):
        header = self.valid_search_commands
        data = [list(pcap.values()) for pcap in pcap_dictionary]
        table = tabulate(data, headers=header, tablefmt="fancy_grid")
        print(table)

    def display_matching_pcaps(self, search_command: list):
        target_value = search_command[-1]
        search = search_command[0]
        matching_pcaps = []

        for pcap in self.packet_data:
            for attribute, value in pcap.items():
                if attribute == search and value == target_value:
                    matching_pcaps.append(pcap)
                    break

        if matching_pcaps:
            self._print_pcap_table(matching_pcaps)
        else:
            print("Unable to locate the specified PCAP file")
