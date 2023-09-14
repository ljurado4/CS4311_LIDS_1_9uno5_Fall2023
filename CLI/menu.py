import config_menu
import help_menu
import pcap_menu

class Menu():
    """A class for common functions the CLI will use across different menus.
    
    This class provides utility methods for obtaining and validating user input
    when navigating through diffrent menu options in CLI.
    """
    def __init__(self) -> None:
         # Omitted "Show PCAP X" because it's uncertain how we will allow user to identify or search for specific PCAP file.
        self.choice_set = {"Help","Config","Show PCAP","Alert","Exit"}
    
    def get_user_input(self, message: str,valid_input: set) -> str:
        """Gets user input and validates input

        Args:
            message (str): Message to be displayed to the user.
            valid_input (set): A set of valid inputs the user can enter on the terminal.
        """
        user_input = input(message)
        
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
        
    
  
        match menu_option_selected:
            case _ if menu_option_selected == "Help":
                # call class for help menu
                menu = help_menu.HelpMenu()
                menu.display_help()
            case _ if menu_option_selected == "Config":
                print(">> Config")
                path = input("Enter path to Configuration file")
                config_menu.ConfigureCLI.configure(path)
            case _ if menu_option_selected == "Show PCAP":
                # call class for help Show PCAP
                pcap_menu_display = pcap_menu.PcapMenu()
                pcap_menu_display.display()
            
            case _ if menu_option_selected == "Alert":
                # call class for Alert menu
                pass
            case _ if menu_option_selected == "Exit":
                print("Exiting")
                exit()
                

        
