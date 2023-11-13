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
import threading
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import menu
from backend import packets, alerts_manager

class Alerts_CLI:
    #def __init__(self):
    #    self.stop_streaming = False
    #    self.input_buffer = []
    #    self.lines_to_display = []
    #    self.MAX_LINES = 100
    #    self.user_typing_event = threading.Event()
    #    self.alert_manager = alerts_manager.AlertManager()
    #    self.instanceMenu = menu.Menu()
    #    self.pack_time = packets.PackTime()
    #    self.thread = threading.Thread(target=self.display_Alerts)#
    
    #modified Alejandro Hernandez
    
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

    #     while not self.stop_streaming:
    #         if not self.user_typing_event.is_set():
    #             alerts = self.alert_manager.get_alerts()
    #             self.lines_to_display.extend(alerts)
    #             self.lines_to_display = self.lines_to_display[-self.MAX_LINES:]
    #             self.refresh_display()
    #         time.sleep(1)

    # def refresh_display(self):
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     for line in self.lines_to_display:
    #         print(line)
    #     print("Type something (or 'q' to quit): " + ''.join(self.input_buffer), end='', flush=True)

    # def run(self):
    #     self.thread.daemon = True
    #     self.thread.start()

    #     try:
    #         while True:
    #             self.user_typing_event.set()
    #             user_input = input()
    #             self.user_typing_event.clear()
    #             self.lines_to_display.append("You typed: " + user_input)
    #             thread2 = threading.Thread(target=self.instanceMenu.navigate_next_menu, args=(user_input,))
    #             thread2.start()
    #     finally:
    #         self.stop_streaming = True
    #         self.thread.join()



    #     # Todo 1
    #     # Consider moving this after configurations.
    #     # To access alerts post-sniffer run on a thread, use this.
    #     # Ensure this runs throughout the CLI program, even if the user navigates other menus.
    #     # Find a way to always run a thread post-file execution or explore alternative methods.
        
    #     #pack_time = packets.PackTime()
    #     #thread = threading.Thread(target=pack_time.run_sniffer)
    #    # thread.start()
        
     
    #     # get alerts 
       
    #    # getter = alerts_manager.AlertManager().sharedAlerts
        
        
    #     # Display alerts
    #     # Todo 2
    #     # Goal: Continuously display alerts in this menu without user intervention.
    #     # Problems:
    #     # 1. How can we accept input without disrupting the alert display?
    #     # 2. How do we prevent user input in the terminal from mixing with the alerts or getting overridden by new data?

        
        
    #     #menu_helper = menu.Menu()
        
        
    #    # next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        
    #     #menu_helper.navigate_next_menu(next_menu)
        
        
    #     menu_helper = menu.Menu()
        
        
    #     next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        
    #     menu_helper.navigate_next_menu(next_menu)