import threading
import time
import os
from datetime import datetime  # This would be required to simulate timestamps for port checking

# Your existing imports
from alerts_menu import Alerts_CLI
from menu import Menu

# Import the PortDetection class from the PortChecker module
from backend.PortChecker import portDetection

# Instantiate the PortDetection class
port_checker = portDetection()

stop_streaming = False
input_buffer = []
lines_to_display = []
MAX_LINES = 100  # You can adjust this for the number of lines to display

# Create an Event object to signal when the user is typing
user_typing_event = threading.Event()

def display_stream():
    global lines_to_display
    alerts = Alerts_CLI()
    while not stop_streaming:
        if not user_typing_event.is_set():
            lines_to_display.append(alerts)
            # Ensure we don't keep more lines than necessary
            lines_to_display = lines_to_display[-MAX_LINES:]
            refresh_display()
        time.sleep(1)

def refresh_display():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    # Display the recent lines
    for line in lines_to_display:
        print(line)

    # Display the current user input
    print("Type something (or 'q' to quit): " + ''.join(input_buffer), end='', flush=True)

def process_network_data(srcIP, destinationPort):
    # This function would process network data and use port_checker to detect port scans
    # For demonstration purposes, let's simulate a timestamp and call the port checking method
    current_timestamp = datetime.now()
    timeAllowed = 60  # Time in seconds
    threshold1 = 100  # Threshold for alert level 1
    threshold2 = 200  # Threshold for alert level 2

    # Use the port_checker instance to check the ports
    result = port_checker.port_Checking(srcIP, destinationPort, current_timestamp, timeAllowed, threshold1, threshold2)
    if result:
        lines_to_display.append(f"Port scan detected from {srcIP} on port {destinationPort}: {result}")
        refresh_display()

# Start the thread to display the constant stream
thread = threading.Thread(target=display_stream)
thread.daemon = True
thread.start()

instanceMenu = Menu()

try:
    while True:
        user_input = input()
        if user_input == 'q':
            break  # Break out of the loop to quit
        lines_to_display.append("You typed: " + user_input)
        thread2 = threading.Thread(target=instanceMenu.navigate_next_menu, args=(user_input,))
        thread2.start()
        # Here, you might call process_network_data with actual network data

finally:
    stop_streaming = True
    thread.join()