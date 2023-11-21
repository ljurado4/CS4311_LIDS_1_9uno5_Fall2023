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

from menu import Menu



class PcapMenu(Menu):
    def __init__(self) -> None:
        super().__init__()


    def handle_pcap_search(self):
        

        print("Handle PCAP search ")
        next_menu = self.get_user_input(">> ",self.choice_set)
        self.navigate_next_menu(next_menu)
        
    



    
