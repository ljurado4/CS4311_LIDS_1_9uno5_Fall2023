##################################################################
# File: simulate_port_scans.py
#
# Version: [5.0]
#
# Description: 
# This script is designed to simulate a port scan on a specified IP
# address using Scapy, a powerful interactive packet manipulation tool.
# The script attempts to connect to ports ranging from 1 to 1024 and
# identifies which ports are open by examining the responses.
#
# The use of this script should be authorized and compliant with all
# applicable laws and regulations as port scanning can be considered
# invasive and may be illegal on networks without explicit permission.
#

# Tasks:
# - [Task 1]: Define the target IP address and port range for the scan.
# - [Task 2]: Implement a loop to iterate through the specified range of ports.
# - [Task 3]: Craft and send a SYN packet to each port using Scapy.
# - [Task 4]: Analyze the responses to determine if a port is open (SYN-ACK received).
# - [Task 5]: Print out the open ports to the user.
# - [Task 6]: Handle exceptions and errors that may occur during the scan process.
# - [Task 7]: Ensure the script adheres to ethical guidelines and legal requirements.
# - [Task 8]: Document the function and script usage with appropriate comments.
#
##################################################################

# Rest of the script...


from scapy.all import IP, TCP, sr1

def simulate_port_scan():
    target_ip = "192.168.1.100"
    start_port = 1
    end_port = 1024

    
    for port in range(start_port, end_port+1):
        packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            continue
        if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            print(f"Port {port} is open!")

if __name__ == "__main__":
    simulate_port_scan()


