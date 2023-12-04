# File: main_cli.py

# Description: This file serves as the entry point for the CLI (Command Line Interface) of LIDS (Local Intrusion Detection System). It initializes the system and starts the Alert menu.

# @ Author: Benjamin Hansen
# @ Modifier:

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from menu import Menu
import argparse
from config_parser import ConfigureCLI
from backend import packets
import threading
from config_condition import config_condition




# @ Author: Benjamin Hansen
class MainCLI(Menu):

    # @ Author: Benjamin Hansen
    def __init__(self,config_file):
        super().__init__()
        self.config_file = config_file

    # @ Author: Benjamin Hansen
    def run(self):
        super().navigate_next_menu("Alert")


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="CLI for LIDS.")
    parser.add_argument("--config_file", required=True, help="Configuration file name (e.g., config.xml)")
   
    args = parser.parse_args()

    configure_system = ConfigureCLI()
    # Pass the additional arguments to the configure method
    configure_system.configure(args.config_file)



    pack_time = packets.PackTime()
    thread = threading.Thread(target=pack_time.run_sniffer)
    thread.start()
    
    
    with config_condition:
        config_condition.notify_all()
    
    cli_main = MainCLI(args.config_file)
    cli_main.run()
