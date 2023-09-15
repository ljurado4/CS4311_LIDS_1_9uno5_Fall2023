from navigator import navigate
from pcap_menu import PcapMenu

class Menu():
    """A class for common functions the CLI will use across different menus."""

    def __init__(self) -> None:
        self.choice_set = {"Help", "Config", "Show PCAP", "Alert", "Exit", "Show PCAP X"}
        self.pcaps = {
            1: {"name": "pcap1", "path": "./pcaps/pcap1.pcap", "timestamp": "2023-09-13 12:00:00", "size": "10MB"},
            2: {"name": "pcap2", "path": "./pcaps/pcap2.pcap", "timestamp": "2023-09-13 12:05:00", "size": "8MB"}
        }
        self.pcapxs = {
            1: {"name": "pcapx1", "path": "./pcaps/pcapx1.pcapx", "timestamp": "2023-09-13 12:10:00", "size": "5MB"},
            2: {"name": "pcapx2", "path": "./pcaps/pcapx2.pcapx", "timestamp": "2023-09-13 12:15:00", "size": "6MB"}
        }

    def get_user_input(self, message: str, valid_input: set) -> str:
        """Gets and validates user input."""
        user_input = input(message)
        
        while user_input not in valid_input:
            print("Incorrect input. Valid inputs are:")
            for val_input in valid_input:
                print(val_input)
            user_input = input(message)

        return user_input
    
    def show_all_pcaps(self):
        """Displays details of all PCAPs."""
        for pcap_id, pcap_data in self.pcaps.items():
            print(f"PCAP ID: {pcap_id}")
            for key, value in pcap_data.items():
                print(f"{key.capitalize()}: {value}")
            print("------")

    def show_all_pcapxs(self):
        """Displays details of all PCAP Xs."""
        for pcapx_id, pcapx_data in self.pcapxs.items():
            print(f"PCAP X ID: {pcapx_id}")
            for key, value in pcapx_data.items():
                print(f"{key.capitalize()}: {value}")
            print("------")

    def navigate_next_menu(self, menu_option_selected: str) -> None:
        if menu_option_selected == "Show PCAP":
            self.show_all_pcaps()
            while True:
                try:
                    pcap_id = int(input("Enter PCAP ID to view details or 0 to go back: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid PCAP ID or 0 to go back.")
            if pcap_id:
                self.show_pcap_details(pcap_id)

        elif menu_option_selected == "Show PCAP X":
            self.show_all_pcapxs()
            while True:
                try:
                    pcapx_id = int(input("Enter PCAP X ID to view details or 0 to go back: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid PCAP X ID or 0 to go back.")
            if pcapx_id:
                self.show_pcapx_details(pcapx_id)

        elif menu_option_selected == "Alert":
            # Call class for Alert menu
            # (Your existing Alert logic here)
            pass
        elif menu_option_selected == "Exit":
            print("Exiting")
            exit()
        else:
            navigate(menu_option_selected)

    def show_pcap_details(self, pcap_id: int) -> None:
        """Displays details of a single PCAP based on its ID."""
        if pcap_id not in self.pcaps:
            print("Invalid PCAP ID.")
            return

        pcap_data = self.pcaps[pcap_id]
        print(f"\nDetails for PCAP ID: {pcap_id}")
        for key, value in pcap_data.items():
            print(f"{key.capitalize()}: {value}")
        print("------")

    def show_pcapx_details(self, pcapx_id: int) -> None:
        """Displays details of a single PCAP X based on its ID."""
        if pcapx_id not in self.pcapxs:
            print("Invalid PCAP X ID.")
            return

        pcapx_data = self.pcapxs[pcapx_id]
        print(f"\nDetails for PCAP X ID: {pcapx_id}")
        for key, value in pcapx_data.items():
            print(f"{key.capitalize()}: {value}")
        print("------")
