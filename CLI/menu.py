from help_menu import HelpMenu
from pcap_menu import PcapMenu

class Menu():
    """A class for common functions the CLI will use across different menus."""
    
    def __init__(self) -> None:
        # Omitted "Show PCAP X" because it's uncertain how we will allow the user to identify or search for a specific PCAP file.
        self.choice_set = {"Help", "Config", "Show PCAP", "Alert", "Exit"}
    
    def get_user_input(self, message: str, valid_input: set) -> str:
        """Gets and validates user input."""
        user_input = input(message)
        
        while user_input not in valid_input:
            print("Incorrect input. Valid inputs are:")
            for val_input in valid_input:
                print(val_input)
            user_input = input(message)

        return user_input
    
    def navigate_next_menu(self, menu_option_selected: str) -> None:
        """Navigates to the selected menu."""
        if menu_option_selected == "Help":
            menu = HelpMenu()
            menu.display_help()
        elif menu_option_selected == "Config":
            from config_menu import ConfigureCLI  # Move the import here to prevent circular imports.
            print(">> Config")
            path = input("Enter path to Configuration file: ")
            ConfigureCLI.configure(path)
        elif menu_option_selected == "Show PCAP":
            pcap_menu = PcapMenu()
            pcap_menu.display()
        elif menu_option_selected == "Alert":
            # Call class for Alert menu
            # (Your existing Alert logic here)
            pass
        elif menu_option_selected == "Exit":
            print("Exiting")
            exit()
