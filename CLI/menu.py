from config_menu import ConfigureCLI
from help_menu import HelpMenu

class Menu():
    """A class for common functions the CLI will use across different menus.
    
    This class provides utility methods for obtaining and validating user input
    when navigating through diffrent menu options in CLI.
    """
    
    def get_user_input(self, message: str,valid_input: set) -> str:
        """Gets user input and validates input

        Args:
            message (str): Message to be displayed to the user.
            valid_input (set): A set of valid inputs the user can enter on the terminal.
        """
        user_input = input(message+"\n")
        
        #Incorrect user input 
        while user_input not in valid_input:
            print("Wrong input valid inputs are")
            for val_input in valid_input:
                print(val_input)
            user_input = input(message)

        return user_input
    
    def navigate_next_menu(self, menu_option_selected: str) -> None:
        """Navigate to thje next menu based on the user's selection
        
        This function takes a menu option and navigated to the next appropiate menu
        based on the user's input. The function supports options "Help", "Config", 
        "Show PCAP", and "Alert".

        Args:
            menu_option_selected (str): The menu option that the user has selected.
        """
        
        # Omitted "Show PCAP X" because it's uncertain how we will allow user to identify or search for specific PCAP file.
        option_selected = self.get_user_input(menu_option_selected,{"Help","Config","Show PCAP","Alert"})
        
        match option_selected:
            case _ if option_selected == "Help":
                # call class for help menu
                menu = HelpMenu
                menu.display_help
                pass
            case _ if option_selected == "Config":
                print(">> Config")
                path = input("Enter path to Configuration file")
                ConfigureCLI.configure(path)
                
                pass
            case _ if option_selected == "Show PCAP":
                # call class for help Show PCAP
                pass
            case _ if option_selected == "Alert":
                # call class for Alert menu
                pass

        
