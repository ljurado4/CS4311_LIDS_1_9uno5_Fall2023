# File: main_cli.py
#
# Description: This file serves as the entry point for the CLI (Command Line Interface) of LIDS (Local Intrusion Detection System). It initializes the system and starts the Alert menu.
# 
# @ Author: Benjamin Hansen
# @ Modifier:

import menu
import argparse

# @ Author: Benjamin Hansen
def main():
    alert_menu = menu.Menu()
    alert_menu.navigate_next_menu("Alert")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="CLI for LIDS.")
    parser.add_argument("--config_file", required=True, help="configuration file name (e.g. config.xml)")
    args = parser.parse_args()
    main()
