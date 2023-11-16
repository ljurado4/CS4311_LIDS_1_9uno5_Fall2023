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
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self):
        self.stop_streaming = False
        self.input_buffer = []
        self.lines_to_display = []
        self.MAX_LINES = 100
        self.user_typing_event = threading.Event()
        self.alert_manager = alerts_manager.AlertManager()
        self.instanceMenu = menu.Menu()
        self.pack_time = packets.PackTime()
        self.thread = threading.Thread(target=self.display_Alerts)

    def display_Alerts(self):
        while not self.stop_streaming:
            if not self.user_typing_event.is_set():
                alerts = self.alert_manager.get_alerts()
                self.lines_to_display.extend(alerts)
                self.lines_to_display = self.lines_to_display[-self.MAX_LINES:]
                self.refresh_display()
            time.sleep(1)

    def refresh_display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in self.lines_to_display:
            print(line)
        print("Type something (or 'q' to quit): " + ''.join(self.input_buffer), end='', flush=True)

    def run(self):
        self.thread.daemon = True
        self.thread.start()

        try:
            while True:
                self.user_typing_event.set()
                user_input = input()
                self.user_typing_event.clear()
                self.lines_to_display.append("You typed: " + user_input)
                thread2 = threading.Thread(target=self.instanceMenu.navigate_next_menu, args=(user_input,))
                thread2.start()
        finally:
            self.stop_streaming = True
            self.thread.join()

=======
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
    
=======

# @ Author: Benjamin Hansen
# @ Modifier: Alejandro Hernandez

>>>>>>> c60afdbbcf112d267e305114e1f43fccba511c31
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
<<<<<<< HEAD

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
>>>>>>> 62fa2d62cd435ade65ea262397353ec5a718c228

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

<<<<<<< HEAD
        # Todo 1
        # Consider moving this after configurations.
        # To access alerts post-sniffer run on a thread, use this.
        # Ensure this runs throughout the CLI program, even if the user navigates other menus.
        # Find a way to always run a thread post-file execution or explore alternative methods.
        
        #pack_time = packets.PackTime()
        #thread = threading.Thread(target=pack_time.run_sniffer)
       # thread.start()
        
     
        # get alerts 
       
       # getter = alerts_manager.AlertManager().sharedAlerts
=======


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

        
>>>>>>> 62fa2d62cd435ade65ea262397353ec5a718c228
        
    #     #menu_helper = menu.Menu()
        
        
    #    # next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        
<<<<<<< HEAD
        #menu_helper = menu.Menu()
        
        
       # next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        
        #menu_helper.navigate_next_menu(next_menu)
=======
    #     #menu_helper.navigate_next_menu(next_menu)
        
        
    #     menu_helper = menu.Menu()
        
        
    #     next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        
    #     menu_helper.navigate_next_menu(next_menu)
>>>>>>> 62fa2d62cd435ade65ea262397353ec5a718c228
=======
>>>>>>> c60afdbbcf112d267e305114e1f43fccba511c31
