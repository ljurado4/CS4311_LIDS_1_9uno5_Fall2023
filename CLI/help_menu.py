# help_menu.py

from navigator import navigate

class HelpMenu:
    
    def display_help(self):
        """Displays information regarding the commands the user may perform while using CLI version of LIDS."""
        print("The following are system commands to change from the system windows and what each function does.")
        print("\tConfig: Parse the XML file and updates whitelist/blacklist, etc.")
        print("\tShowPCAP: Display information from the latest PCAP.")
        print("\tAlert: Displays the Alerts.")
        
        next_menu = input(">> ")
        navigate(next_menu)
