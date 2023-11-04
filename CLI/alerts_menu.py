################################################################################
# File: alerts_menu.py
#
# Version: [5.0]
#
# Description: This file contains the implementation of the Alerts_CLI class,
#              which is responsible for displaying alerts in a CLI interface.
#
# Modification History:
# [11/01/2023] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Implement the display_Alerts method to display alerts in a tabular format.
# - [Task 2]: Add functionality to get user input for navigating to the next menu.
#
################################################################################

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import menu

# Install 'tabulate' using `pip3 install tabulate`
from tabulate import tabulate
import threading
from backend import packets,alerts_manager


class Alerts_CLI:
    def __init__(self):
        self.alert_thread = threading.Thread(target=self.display_alerts)
         # Make the thread a daemon so it doesn't block program exit
        self.alert_thread.daemon = True 

    def display_Alerts(self,alertList):
        
        print("Alerts")
        
        
        # Todo 1
        # Consider moving this after configurations.
        # To access alerts post-sniffer run on a thread, use this.
        # Ensure this runs throughout the CLI program, even if the user navigates other menus.
        # Find a way to always run a thread post-file execution or explore alternative methods.
        
        pack_time = packets.PackTime()
        thread = threading.Thread(target=pack_time.run_sniffer)
        thread.start()
        
     
        # get alerts 
        getter = alerts_manager.AlertManager().sharedAlerts
        
        
        # Display alerts
        # Todo 2
        # Goal: Continuously display alerts in this menu without user intervention.
        # Problems:
        # 1. How can we accept input without disrupting the alert display?
        # 2. How do we prevent user input in the terminal from mixing with the alerts or getting overridden by new data?

        
        
        menu_helper = menu.Menu()
        
        
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        
        menu_helper.navigate_next_menu(next_menu)
