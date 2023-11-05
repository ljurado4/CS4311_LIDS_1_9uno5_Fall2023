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

# File: alerts_menu.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import menu

# Install 'tabulate' using `pip3 install tabulate`
from tabulate import tabulate
import threading
from backend import packets, alerts_manager

class Alerts_CLI:
    def __init__(self):
        self.alert_thread = threading.Thread(target=self.display_Alerts)
        self.alert_thread.daemon = True

    def display_Alerts(self):
        while True:
            # Fetch alerts and format them into a string
            alerts = self.get_alerts()  # Implement get_alerts() to fetch alerts as needed
            alert_string = "\n".join(alerts)  # Convert alerts to a string with line breaks

            # You can print the alerts to the console if needed
            print(alert_string)

            # Sleep for a while before checking for alerts again
            time.sleep(1)

    def get_alerts(self):
        # Implement this method to fetch alerts from the alerts_manager or any other source
        # Return a list of alert messages
        alerts = []  # Initialize an empty list to store alert messages

        # Example: Fetch alerts from some source and append them to the list
        alerts.append("Alert 1: Some message")
        alerts.append("Alert 2: Another message")

        return alerts  # Return the list of alert messages
        pass
