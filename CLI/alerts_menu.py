# File: alerts_menu.py
#
# Description: Displaying alerts through a command-line interface (CLI). The class includes a method called display_Alerts that initiates the capture of network packets and then prints a list of alerts obtained from an AlertManager
#
# @ Author: Benjamin Hansen
# @ Modifier: Alejandro Hernandez


import sys
import os
import threading
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import menu
from backend import packets, alerts_manager

# @ Author: Benjamin Hansen
class Alerts_CLI:

# @ Author: Benjamin Hansen
# @ Modifier: Alejandro Hernandez

    def display_Alerts(self):
        pack_time = packets.PackTime()
        thread = threading.Thread(target=pack_time.run_sniffer)
        thread.start()
        print("Debugged Display alerts")
        lstAlerts = alerts_manager.AlertManager().sharedAlerts
        print("Printing list alerts ",lstAlerts) # printing list 
        for i in lstAlerts:
            
            print(i)
        menu_helper = menu.Menu()
        
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        
        menu_helper.navigate_next_menu(next_menu)
