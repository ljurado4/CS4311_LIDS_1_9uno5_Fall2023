import menu
#  Install 'tabulate' using `pip install tabulate`
from tabulate import tabulate


class Alerts_CLI:


    def display_Alerts(self,alertList):
        
        header  = ["LVL","Time","IP","Port","Description"]

        data = alertList
        
        table = tabulate(data, header, tablefmt="fancy_grid")
        
        print(table)
        
        menu_instance = menu.Menu()
        next_menu = input(">>")
        menu_instance.navigate_next_menu(next_menu)