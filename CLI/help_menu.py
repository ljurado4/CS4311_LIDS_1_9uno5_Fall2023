# help_menu.py

from navigator import navigate
import menu

class HelpMenu:
    
    def display_help(self):
        """Displays information regarding the commands the user may perform while using CLI version of LIDS."""
        print("The following are system commands to change from the system windows and what each function does.")
        print("\tConfig: Parse the XML file and updates whitelist/blacklist, etc.")
        print("\tShowPCAP: Display information from the latest PCAP.")
        print("\tAlert: Displays the Alerts.")
        
        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)