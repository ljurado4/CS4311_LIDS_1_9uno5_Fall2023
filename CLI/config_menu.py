# config_menu.py

class ConfigureCLI:
    
    def configure(self, path_config_file: str) -> None:
        from menu import Menu  # Move the import inside the function

        #parse xml file and update

        menu_instance = Menu()
        next_menu = input(">> ")
        menu_instance.navigate_next_menu(next_menu)
