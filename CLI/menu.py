import config_parser
import help_menu
import pcap_menu
import alerts_menu
import main_menu

class Menu():
    """A class for common functions the CLI will use across different menus."""

    def __init__(self) -> None:
        self.choice_set = {"Help", "Config", "Show PCAP", "Alert", "Exit","All PCAPs"}
        
    
    def is_pcap_command(self, user_input: str) -> bool:
        """Checks if the given user input contains the "Show PCAP" command.

        Args:
            user_input (str): The input string from the user.

        Returns:
            bool: True if "Show PCAP" is present in the user_input False otherwise
        """
        return "Show PCAP" in user_input or "All PCAPs" in user_input

    def get_user_input(self, message: str, valid_input: set) -> str:
        """Gets and validates user input."""
        user_input = input(message)
        
        if self.is_pcap_command(user_input):
            return user_input
            
        
        while user_input not in valid_input:
            print("Incorrect input. Valid inputs are:")
            for val_input in valid_input:
                print(val_input)
            user_input = input(message)
            if "Show PCAP" in user_input:
                return user_input
                    
            if self.is_pcap_command(user_input):
                return user_input
        
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
            case _ if menu_option_selected == "Start Menu":
                main_menu_instance = main_menu.MainMenu()
                main_menu_instance.show_menu()

            case _ if menu_option_selected == "Help":
                # call class for help menu
                menu = help_menu.HelpMenu()
                menu.display_help()

            case _ if menu_option_selected == "Config":
                print(">> Config")
                path = input(">> Enter configuration file name\n")
                configuration = config_parser.ConfigureCLI()
                configuration.configure(path)
    
            case _ if self.is_pcap_command(menu_option_selected):
                # call class for help Show PCAP
                pcap_menu_display = pcap_menu.PcapMenu()
                pcap_menu_display.handle_pcap_search(menu_option_selected)
            
            case _ if menu_option_selected == "Alert":
                # call class for Alert menu
                print(">> Alert")
                alertList = [
                    [2, "11.6578", "192.128.0.1", 80, "Unknown host ping"],
                    [3, "11.6578", "193.127.0.2", 27, "port scan"],
                    [1, "11.6578", "192.128.0.1", 80, "fail login attempt"],
                    [2, "11.6578", "193.124.0.3", 4040, "Unknown host ping"],
                ]
                alert_men = alerts_menu.Alerts_CLI()
                alert_men.display_Alerts(alertList)
            case _ if menu_option_selected == "Exit":
                print("Exiting")
                exit()
                