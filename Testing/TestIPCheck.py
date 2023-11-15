# File: TestIPChecker.py
#
# Description: The file has a template that appears to be the main or welcome page of a Local Intrusion Detection System (LIDS). This page likely serves as an entry point to the system, where users can upload a configuration file. 
# 
# @ Author:
# @ Modified: Alejandro Hernandez

from ipChecker import ip_Checker

checker = ip_Checker()


# Simulate a packet with an IP to check
packet_ip_to_check = "10.0.0.2"

# Check if the IP is in the whitelist
if checker.ip_in_List(packet_ip_to_check):
    print(f"IP {packet_ip_to_check} is in the whitelist.")
else:
    print(f"IP {packet_ip_to_check} is not in the whitelist.")