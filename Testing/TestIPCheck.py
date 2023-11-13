
##################################################################
# File: TestIPChecker.py
#
# Version: [5.0]
#
# Description: The file has a template that appears to be the main or welcome page of a
# Local Intrusion Detection System (LIDS). This page likely serves as an entry point to the system,
# where users can upload a configuration file. 

# Tasks:
# - [Task 1]: Complete the backend integration for the file upload form to ensure that the uploaded configuration file is received, validated, and processed by the server.
# - [Task 2]: Implement the functionality in LIDS_Main.js to handle the file upload interaction, such as file validation, providing user feedback, and possibly parsing the XML file client-side before sending it to the server.
# - [Task 3]: Design the user interface in main.css to provide a responsive and intuitive design for the file upload process.
# - [Task 4]: Set up server-side validation to check the integrity and format of the uploaded file to prevent malformed or potentially malicious files from being processed.
# - [Task 5]: Write unit tests to test the file upload functionality under various conditions to ensure robustness.
# - [Task 6]: Implement error handling to gracefully inform the user of any issues with their upload, whether due to network problems, file issues, or server errors.
# - [Task 7]: Ensure that accessibility standards are met so that all potential users can navigate and use the file upload feature effectively.
#
##################################################################

#Modified Alejandro Hernandez

from ipChecker import ip_Checker

checker = ip_Checker()


# Simulate a packet with an IP to check
packet_ip_to_check = "10.0.0.2"

# Check if the IP is in the whitelist
if checker.ip_in_List(packet_ip_to_check):
    print(f"IP {packet_ip_to_check} is in the whitelist.")
else:
    print(f"IP {packet_ip_to_check} is not in the whitelist.")