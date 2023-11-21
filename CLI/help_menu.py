################################################################################
# File: help_menu.py
#
# Description: This file contains the implementation of the HelpMenu class, which provides information about the commands that users can perform while using the CLI version of LIDS (Local Intrusion Detection System).
#
# @ Author: Benjamin Hansen
# @ Modifier: Seth Velasco 

from menu import Menu

# @ Author: Benjamin Hansen
# @ Modifier: Seth Velasco 
class HelpMenu(Menu):
    
    def __init__(self) -> None:
        super().__init__()
    
    def display_help(self):
        """Displays information regarding the commands the user may perform while using CLI version of LIDS."""
        print("The following are system commands to change from the system windows and what each function does.")
        print("\tStart Menu: Used to return to the start menu that displays host information.")
        print("\tConfig: Parse the XML file and updates whitelist/blacklist, etc.")
        print("\tShow PCAP: Display information from the latest PCAP.")
        print("\t\tCan search for a particular PCAP through certain attributes, such as Time, Source, Destination, etc.")
        print("\t\tShow PCAP All: displays all captured PCAPs")
        print("\tAlert: Displays the Alerts.")
        print("\tSeverity Levels:")
        print("\t\t1. High severity - Level 3")
        print("\t\t2. Medium severity - Level 2")
        print("\t\t3. Low severity - Level 1")
        print("\tExit: Exits the system.")
        
        next_menu = self.get_user_input(">> ", self.choice_set)
        self.navigate_next_menu(next_menu)
