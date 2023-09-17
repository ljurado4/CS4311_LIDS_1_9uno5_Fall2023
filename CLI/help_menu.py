
import menu


class HelpMenu:
    
    def display_help(self):
        """Displays information regarding the commands the user may perform while using CLI version of LIDS."""
        print("The following are system commands to change from the system windows and what each function does.")
        print("\tStart Menu: Used to return to the start menu that was displayed upon start up.")
        print("\tConfig: Parse the XML file and updates whitelist/blacklist, etc.")
        print("\tShow PCAP: Display information from the latest PCAP.")
        print("\tAlert: Displays the Alerts.")
        print("\tExit: Exits the system.")
        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)