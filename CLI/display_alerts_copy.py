import threading
import time
import os
from alerts_menu import Alerts_CLI
from menu import Menu

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

# Start the thread to display the constant stream
thread = threading.Thread(target=display_stream)
thread.daemon = True
thread.start()

instanceMenu = Menu()

try:
    while True:
        #user_typing_event.set()  # Signal that the user is typing
        user_input = input()
        #user_typing_event.clear()  # Signal that the user is done typing
        lines_to_display.append("You typed: " + user_input)
        thread2 = threading.Thread(target=instanceMenu.navigate_next_menu, args=(user_input,))
        thread2.start()

finally:
    stop_streaming = True
    thread.join()