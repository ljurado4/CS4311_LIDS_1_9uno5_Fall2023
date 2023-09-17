import menu
from tabulate import tabulate

class PcapMenu:
    packet_data = [
        {
            "Time": "2023-09-16 12:01:23.456789",
            "Source": "192.168.1.2",
            "Destination": "192.168.1.100",
            "Protocol": "TCP",
            "Length": 64,
            "Description": "TCP Handshake SYN"
        },
        {
            "Time": "2023-09-16 12:01:23.456990",
            "Source": "192.168.1.100",
            "Destination": "192.168.1.2",
            "Protocol": "TCP",
            "Length": 64,
            "Description": "TCP Handshake SYN, ACK"
        }
    ]
    
    def __init__(self) -> None:
        self.menu_helper = menu.Menu()
        self.valid_search_commands = [
            "Time", "Source", "Protocol", "Length", "Description"]

    def navigate_next_menu(self):
        menu_helper = menu.Menu()
        next_menu = menu_helper.get_user_input(">> ",menu_helper.choice_set)
        menu_helper.navigate_next_menu(next_menu)
        
    
    
    def _print_pcap_table(self, pcap_dictionary: dict):
        """
        Print a tabulated representation of the given pcap data.
        
        Args:
        - pcap_dictionary (dict): Dictionary containing pcap data.
        """
        header = self.valid_search_commands
        
        data = list(pcap_dictionary.values())
        
        table = tabulate(data, header, tablefmt="fancy_grid")

        print(table)
        
    def display_all_pcaps(self):
        """
        Display all pcap entries
        """

        for pcap in self.packet_data:
            self._print_pcap_table(pcap)

        

    
    def display_matching_pcaps(self, full_command: str, search_command: str):
        """
        Display pcaps that match the given search command and target value.

        Args:
         full_command (str): The complete search command input.
         search_command (str): The specific command to match.

        """
            
        target_value = full_command.split(" ")[-1]
        found_pcap = False
        
        for pcap in self.packet_data:
            
            for attribute, value in pcap.items():
                
                 # Check if the current attribute matches the search command and its value matches the target value
                if attribute == search_command and value == target_value:
                    self._print_pcap_table(pcap)
                    found_pcap = True
        
        # Print a message if no matching pcap is found
        if not found_pcap:
            print("Unable to locate the specified PCAP file")
                    
        
        
        


    def handle_pcap_search(self, user_input: str):
        """Parses the user command to determine the PCAP search criteria and then 
        calls the appropriate function to retrieve PCAP data.

        Args:
            user_input (str): The command string from the user.
        """

        match user_input:

            case _ if "Show" in user_input:
                
                valid_search_command = False
                
                pcap_search_type = ""
                while not valid_search_command:
                    
                    for command in self.valid_search_commands:
                        if command in user_input:
                            valid_search_command = True
                            pcap_search_type = command
                    
                    # Wrong search command
                    if not valid_search_command:
                        pcap_search_type = self.menu_helper.get_user_input(
                                "Invalid search command", self.valid_search_commands)
                
                # TODO: Allow users to 'exit' to leave or 'menu' to return to the main menu.
                
                self.display_search(user_input,pcap_search_type)
                
                self.navigate_next_menu()
            
            case _ if "All" in user_input:
                
                self.display_all_pcaps()
                self.navigate_next_menu()
            
            

                
                            




                    
                    
                        
                    
                
                
        
