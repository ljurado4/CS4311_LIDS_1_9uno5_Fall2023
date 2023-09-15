# main_cli.py

from menu import Menu

def main():
    main_menu = Menu()

    while True:
        print("\nMain Menu:")
        for option in main_menu.choice_set:
            print(f"- {option}")
        print("- All PCAPs")  # Add this line
        
        valid_choices = main_menu.choice_set | {"All PCAPs"}  # Updated valid choices
        user_choice = main_menu.get_user_input(">> ", valid_choices)
        main_menu.navigate_next_menu(user_choice)

if __name__ == "__main__":
    main()
