# File: main_menu.py
#
# Description: This file contains the implementation of the MainMenu class, which  represents the main menu of the CLI (Command Line Interface) for LIDS (Local Intrusion Detection System). It provides functions to display the main menu options and navigate to different menus based on user input.
#
# @ Author: Benjamin Hansen
# @ Modifier:

import menu

# @ Author: Benjamin Hansen
class MainMenu:
    """
    Represents the main menu of the CLI.
    
    This class provides a function to display the main menu and navigate
    to different menus based on user input.
    """

    def show_menu(self):
        """Displays the main menu options to the user.
        
        Presents the main menu prompt. After taking input, it 
        prints details and then uses the 'menu' module to navigate to
        the next appropriate menu.
        """

        menu_instance = menu.Menu()
        print(
            f'name: {menu_instance.host_name}\n'
            f'IP: {menu_instance.ip_address}\n'
            f'MAC: {menu_instance.mac_address}\n'
            f'PORT(s): {" ".join(menu_instance.open_ports)}\n'
        )

        # Assuming 'menu.Menu()' creates an instance of the menu class.
        menu_instance = menu.Menu()

        # Assuming 'get_user_input' method fetches user input and validates it.
        next_menu_choice = menu_instance.get_user_input(">> ", menu_instance.choice_set)

        # Assuming 'navigate_next_menu' method navigates based on the user's choice.
        menu_instance.navigate_next_menu(next_menu_choice)
