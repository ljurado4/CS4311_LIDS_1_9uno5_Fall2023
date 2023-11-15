# File: simulate_port_scans.py
#
#
# Description: 
# This script is designed to simulate a port scan on a specified IP address using Scapy, a powerful interactive packet manipulation tool. The script attempts to connect to ports ranging from 1 to 1024 and identifies which ports are open by examining the responses.
#
# @ Author :
# @ Modified:



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


