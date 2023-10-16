import menu
from tabulate import tabulate
from backend import packets

class PcapMenu:
    def __init__(self):
        # Fetch the PCAP data during initialization
        self.packet_data = packets.PackTime()
        self.packet_data.run_sniffer()

        self.menu_helper = menu.Menu()
        self.valid_search_commands = [
            "Time", "Source", "Destination", "Protocol", "Length", "Description"]

    def navigate_next_menu(self):
        next_menu = self.menu_helper.get_user_input(">> ", self.menu_helper.choice_set)
        self.menu_helper.navigate_next_menu(next_menu)

    def _print_pcap_table(self, pcap_dictionary: list):
        header = self.valid_search_commands
        data = [list(pcap.values()) for pcap in pcap_dictionary]
        table = tabulate(data, headers=header, tablefmt="fancy_grid")
        print(table)

    def display_matching_pcaps(self, search_command: list):
        target_value = search_command[1].lower()
        search = search_command[0]

        matching_pcaps = [pcap for pcap in self.packet_data if str(pcap.get(search, '')).lower() == target_value]

        if matching_pcaps:
            self._print_pcap_table(matching_pcaps)
        else:
            print("Unable to locate the specified PCAP file")

    def handle_pcap_search(self, user_input: str):
        match user_input:
            case _ if "Show" in user_input:
                pcap_search_type = self.menu_helper.get_user_input(
                    "Enter your search type (e.g. protocol ) \n", self.valid_search_commands)
                pcap_search_value = input("Enter value for search\n")
                pcap_search = [pcap_search_type, pcap_search_value]
                self.display_matching_pcaps(pcap_search)
                self.navigate_next_menu()

            case _ if "All" in user_input:
                self._print_pcap_table(self.packet_data)
                self.navigate_next_menu()

if __name__ == "__main__":
    # Create a PcapMenu instance and invoke the desired methods for testing if necessary
    menu_instance = PcapMenu()
    while True:
        choice = input("Enter choice (Show, All or Quit): ")
        if choice == "Quit":
            break
        menu_instance.handle_pcap_search(choice)
