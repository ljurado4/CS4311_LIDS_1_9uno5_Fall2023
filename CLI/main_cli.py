################################################################################
# File: main_cli.py
#
# Version: [4.0]
#
# Description: This file serves as the entry point for the CLI (Command Line
#              Interface) of LIDS (Local Intrusion Detection System). It initializes
#              the system and starts the Alert menu.
#
# Modification History:
# [11/01/23] - [3.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Implement the 'main' function to initialize the CLI and start the Alert menu.
################################################################################

import menu
import argparse

def main():
    alert_menu = menu.Menu()
    alert_menu.navigate_next_menu("Alert")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="CLI for LIDS.")
    parser.add_argument("--config_file", required=True, help="configuration file name (e.g. config.xml)")
    args = parser.parse_args()
    main()
