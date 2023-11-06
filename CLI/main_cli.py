# main_cli.py

#from CLI.menu import Menu
import menu
import argparse

def main():
    print('starting main_cli')
    alert_menu = menu.Menu()
    alert_menu.navigate_next_menu("Alert")
    #print('main ran')


if __name__ == "__main__":
    print('main method start')
    parser = argparse.ArgumentParser(description="CLI for LIDS.")
    parser.add_argument("--config_file",required=True, help="configuration file name (e.g. config.xml)")
    args = parser.parse_args()
    main()
