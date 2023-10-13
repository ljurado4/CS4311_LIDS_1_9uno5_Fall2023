#help_menu.py

import menu


class HelpMenu:
    
    def display_help(self):
        """Displays information regarding the commands the user may perform while using CLI version of LIDS."""
        print("The following are system commands to change from the system windows and what each function does.")
        print("\tStart Menu: Used to return to the start menu that displays host information.")
        print("\tConfig: Parse the XML file and updates whitelist/blacklist, etc.")
        print("\tShow PCAP: Display information from the latest PCAP.")
        print("\t\tCan search for a particulat PCAP through certain attributes, such as Time, Source, Destination, etc.")
        print("\t\tShow PCAP All: displays all captured PCAPs")
        print("\tAlert: Displays the Alerts.")
        print("\tSeverity Levels:")
        print("\t\t1. High severity - Level 3")
        print("\t\t2. Medium severity - Level 2")
        print("\t\t3. Low severity - Level 1")
        print("\tExit: Exits the system.")
        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)