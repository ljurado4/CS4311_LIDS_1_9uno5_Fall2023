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


    for alert in getter:
        print(alert)
    
    