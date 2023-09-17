# main_cli.py

import menu

def main():
    menu_helper = menu.Menu()
    next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
    menu_helper.navigate_next_menu(next_menu)

if __name__ == "__main__":
    main()
