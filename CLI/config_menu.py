# config_menu.py

class ConfigureCLI:
    
    def configure(self, path_config_file: str) -> None:
        """Configure the CLI based on an XML file."""
        from menu import Menu  # Local import to avoid circular dependencies
        # Parse xml file and update configurations here

        menu_instance = Menu()
        next_menu = input(">> ")
        menu_instance.navigate_next_menu(next_menu)
