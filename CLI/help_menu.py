from menu import Menu

#TODO: Fix Circular import error here and config_menu
class HelpMenu:
    
    def display_help(self):

        """Displays information regarding the commands the user may perform while using CLI verision of LIDS
        
        This function will be a display menu that displays information regarding commands 
        the user may use to access the desired page and displays the purpose of the page.
        The pages include Config, ShowPCAP, and Alert
        """
        
        print("The following are system commands to change from the system windows and what each function does.")
        print("\tConfig: Parse the XML file and updates whitelist/blacklist, etc.")
        print("\tShowPCAP: Display information from the latest PCAP.")
        print("\tAlert: Displays the Alerts.")
        next_menu = input(">> ")
        menu.navigate_next_menu(next_menu)
        
