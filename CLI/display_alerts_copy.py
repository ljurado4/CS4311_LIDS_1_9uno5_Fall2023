import threading
import time
import os
from datetime import datetime
import queue  # Add this import for a thread-safe queue

# Your existing imports
from alerts_menu import Alerts_CLI
from menu import Menu

# Import the PortDetection class from the PortChecker module
from backend.PortChecker import PortDetection

# Instantiate the PortDetection class
port_checker = PortDetection()

stop_streaming = False
input_queue = queue.Queue()  # Use a thread-safe queue for input
lines_to_display = []
MAX_LINES = 100

# Create an Event object to signal when the user is typing
user_typing_event = threading.Event()

def display_stream():
    global lines_to_display
    alerts = Alerts_CLI()
    while not stop_streaming:
        if not user_typing_event.is_set():
            alerts_data = alerts.get_alerts()  # Fetch alerts
            alerts_string = "\n".join(alerts_data)  # Convert alerts to a string with line breaks
            lines_to_display.append(alerts_string)  # Append formatted alerts
            lines_to_display = lines_to_display[-MAX_LINES:]
            refresh_display()
        time.sleep(1)

def refresh_display():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display the recent lines
    for line in lines_to_display:
        print(line)

    # Display the current user input
    print("Type something (or 'q' to quit): ", end='', flush=True)

def process_network_data(srcIP, destinationPort):
    current_timestamp = datetime.now()
    timeAllowed = 60
    threshold1 = 100
    threshold2 = 200

    # Use the port_checker instance to check the ports
    result = port_checker.port_Checking(srcIP, destinationPort, current_timestamp, timeAllowed, threshold1, threshold2)
    if result:
        lines_to_display.append(f"Port scan detected from {srcIP} on port {destinationPort}: {result}")
        refresh_display()

# Function to handle user input
def handle_user_input():
    while True:
        user_input = input()
        if user_input == 'q':
            break
        input_queue.put(user_input)  # Put user input into the queue

# Start the thread to display the constant stream
thread = threading.Thread(target=display_stream)
thread.daemon = True
thread.start()

instanceMenu = Menu()

# Start a thread to handle user input
input_thread = threading.Thread(target=handle_user_input)
input_thread.start()

try:
    while True:
        try:
            user_input = input_queue.get(timeout=1)  # Get user input from the queue
            lines_to_display.append("You typed: " + user_input)
            thread2 = threading.Thread(target=instanceMenu.navigate_next_menu, args=(user_input,))
            thread2.start()
            # Here, you might call process_network_data with actual network data
        except queue.Empty:
            pass

finally:
    stop_streaming = True
    thread.join()
