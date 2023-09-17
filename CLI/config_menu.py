# config_menu.py
import menu

class ConfigureCLI:
    
    def configure(self, path_config_file: str) -> None:
        """Configure the CLI based on an XML file."""


        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)
