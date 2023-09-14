import menu

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
        print("Main Menu")
        print(
            "name: John Doe\n"
            "IP: 192.168.1.100\n"
            "MAC: 00:1A:2B:3C:4D:5E\n"
            "PORT: 8080"
        )

        # Assuming 'menu.Menu()' creates an instance of the menu class.
        menu_instance = menu.Menu()

        # Assuming 'get_user_input' method fetches user input and validates it.
        next_menu_choice = menu_instance.get_user_input(">> ", menu_instance.choice_set)

        # Assuming 'navigate_next_menu' method navigates based on the user's choice.
        menu_instance.navigate_next_menu(next_menu_choice)


