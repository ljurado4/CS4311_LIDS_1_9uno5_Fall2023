#TestIPChecker.py

from ipChecker import ip_Checker

checker = ip_Checker()


# Simulate a packet with an IP to check
packet_ip_to_check = "10.0.0.2"

# Check if the IP is in the whitelist
if checker.ip_in_List(packet_ip_to_check):
    print(f"IP {packet_ip_to_check} is in the whitelist.")
else:
    print(f"IP {packet_ip_to_check} is not in the whitelist.")