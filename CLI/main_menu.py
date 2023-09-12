from menu import Menu 

class MainMenu:
    """
    Represents the main menu of the CLI
    
    This class provides a function to display the main menu and navigate
    to diffrent menu's based on user input.
    """

    def show_menu():
        """Displays the main menu options to the user.
        
        Presents the main menu promt. After taking input, it 
        prints details and then uses 'menu' module to navigate to
        the next appropiate menu
        """

        menu = Menu()

        print("Main Menu")
        next_menu = input(">>")

        print(
            "name: John Doe\n"
            "IP: 192.168.1.100\n"
            "MAC: 00:1A:2B:3C:4D:5E\n"
            "PORT: 8080"
        )
        menu.navigate_next_menu(next_menu)

