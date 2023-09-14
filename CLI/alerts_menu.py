import menu
import tabulate


class Alerts_CLI:


    def display_Alerts(alertList):
        
        header  = ["LVL","Time","IP","Port","Description"]

        data = alertList
        
        table = tabulate(data, header, tablefmt="fancy_grid")
        
        print(table)
        
        menu = menu.Menu()
        next_menu = input(">>")
        menu.navigate_next_menu(next_menu)