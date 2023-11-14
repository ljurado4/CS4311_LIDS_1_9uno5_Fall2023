##################################################################
# File: testPackets.py
#
# Version: [5.0]
#
# Description: 
# This Python script is designed to test the functionality of the packets and alert management systems within a backend module. It includes a main executable section that launches a packet sniffing thread and then retrieves and displays alerts and packet identifiers using the alerts manager. The testing routine is essential for ensuring the reliability and correctness of the packets handling and alert notification subsystem.
#
# @ Author: 
# @ Modified: Alejandro Hernandez
#


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend import alerts_manager,packets  # Replace 'your_module' with the actual module name

import threading

import time

# @ Modified: Alejandro Hernandez

if __name__ == "__main__":

    pack_time = packets.PackTime()

    thread = threading.Thread(target=pack_time.run_sniffer)

    thread.start()

    time.sleep(10)

    
    getter = alerts_manager.AlertManager().sharedAlerts

    getter2 = alerts_manager.AlertManager().identifierList


    for alert in getter:
        print(alert)
    
    for packet in getter2:
        print(packet)
    
    