#alerts_menu.py

#  Install 'tabulate' using `pip3 install tabulate`
from tabulate import tabulate
import menu


class Alerts_CLI:


    def display_Alerts(self,alertList):
        
        header  = ["LVL","Time","IP","Port","Description"]

        data = alertList
        
        table = tabulate(data, header, tablefmt="fancy_grid")
        
        print(table)
        
        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)
        