################################################################################
# File: alerts_menu.py
# Version: [3.0]
# Description: This file contains the implementation of the Alerts_CLI class,
#              which is responsible for displaying alerts in a CLI interface.
#
# Modification History:
# [11/01/2023] - [3.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
# Tasks:
# - [Task 1]: Implement the display_Alerts method to display alerts in a tabular format.
# - [Task 2]: Add functionality to get user input for navigating to the next menu.
################################################################################

# Install 'tabulate' using `pip3 install tabulate`
from tabulate import tabulate

class Alerts_CLI:

    def display_Alerts(self, alertList):
        header = ["LVL", "Time", "IP", "Port", "Description"]
        data = alertList
        table = tabulate(data, header, tablefmt="fancy_grid")
        print(table)
        menu_helper = menu.Menu()  # Make sure to import the 'menu' module if it's used here.
        next_menu = menu_helper.get_user_input(">> ", menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)
