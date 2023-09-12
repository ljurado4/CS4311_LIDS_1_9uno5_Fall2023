from menu import Menu


class ConfigureCLI:
    
    def configure(path_config_file: str) -> None:
        menu = Menu()
        next_menu = input(">> ")
        #parse xml file and update
        
        menu.navigate_next_menu(next_menu)