# navigator.py

def navigate(menu_option_selected: str):
    """Navigates to the selected menu."""
    if menu_option_selected == "Help":
        from help_menu import HelpMenu  # Moved the import inside
        menu = HelpMenu()
        menu.display_help()
    elif menu_option_selected == "Config":
        from config_menu import ConfigureCLI  # Moved the import inside
        print(">> Config")
        path = input("Enter path to Configuration file: ")
        ConfigureCLI.configure(path)
    # ... (add other elif conditions for other options as required)
