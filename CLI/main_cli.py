# main_cli.py

#from CLI.menu import Menu
import menu
import argparse

def main():
    alert_menu = menu.Menu()
    alert_menu.navigate_next_menu("Alert")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="CLI for LIDS.")
    parser.add_argument("--config_file",required=True, help="configuration file name (e.g. config.xml)")
    args = parser.parse_args()
    main()
