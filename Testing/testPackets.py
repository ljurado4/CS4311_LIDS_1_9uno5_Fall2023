##################################################################
# File: testPackets.py
#
# Version: [5.0]
#
# Description: 
# This Python script is designed to test the functionality of the packets
# and alert management systems within a backend module. It includes a
# main executable section that launches a packet sniffing thread and then
# retrieves and displays alerts and packet identifiers using the alerts
# manager. The testing routine is essential for ensuring the reliability
# and correctness of the packets handling and alert notification subsystem.
#

# Tasks:
# - [Task 1]: Initialize and start a packet sniffing thread from the packets module.
#             This task involves creating an instance of the PackTime class and running
#             its sniffer in a separate thread.
# - [Task 2]: Sleep the main thread for a predefined duration to allow the sniffer thread
#             to collect data.
# - [Task 3]: Retrieve shared alerts from the alert manager and print each alert to the console.
#             This task is crucial for verifying the alert triggering mechanism in the system.
# - [Task 4]: Retrieve a list of packet identifiers from the alert manager and print each
#             identifier. This is to check the correct logging and identification of packets
#             by the system.
# - [Task 5]: Ensure the proper termination and cleanup of the sniffing thread after testing.
#             This task is not explicitly defined in the code but is an essential part of a
#             robust testing routine.
#
##################################################################

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend import alerts_manager,packets  # Replace 'your_module' with the actual module name

import threading

import time


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
    
    