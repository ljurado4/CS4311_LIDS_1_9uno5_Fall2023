import menu

class ConfigureCLI:
    
    def configure(self, path_config_file: str) -> None:
        

        #parse xml file and update

        menu_instance = menu.Menu()
        next_menu = input(">> ")
        menu_instance.navigate_next_menu(next_menu)
