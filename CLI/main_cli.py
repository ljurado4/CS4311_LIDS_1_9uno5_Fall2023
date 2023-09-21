# main_cli.py

import menu
import argparse

def main():

    menu_helper = menu.Menu()
    next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
    menu_helper.navigate_next_menu(next_menu)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="CLI for LIDS.")
    parser.add_argument("--config_file",required=True, help="configuration file name (e.g. config.xml)")
    args = parser.parse_args()
    main()
