# File: main_menu.py
#
# Description: This file contains the implementation of the MainMenu class, which  represents the main menu of the CLI (Command Line Interface) for LIDS (Local Intrusion Detection System). It provides functions to display the main menu options and navigate to different menus based on user input.
#
# @ Author: Benjamin Hansen
# @ Modifier:

from menu import Menu

# @ Author: Benjamin Hansen
class MainMenu(Menu):
    """
    Represents the main menu of the CLI.
    
    This class provides a function to display the main menu and navigate
    to different menus based on user input.
    """
    def __init__(self):
        super().__init__()
        

# @ Author: Benjamin Hansen
    def show_menu(self):
        """Displays the main menu options to the user.
        
        Presents the main menu prompt. After taking input, it 
        prints details and then uses the 'menu' module to navigate to
        the next appropriate menu.
        """

        
       
        print(
            f'name: {Menu.host_name}\n'
            f'IP: {Menu.ip_address}\n'
            f'MAC: {Menu.mac_address}\n'
            f'PORT(s): {" ".join(Menu.open_ports)}\n'
        )
        next_menu = self.get_user_input(">> ",self.choice_set)
        self.navigate_next_menu(next_menu)
