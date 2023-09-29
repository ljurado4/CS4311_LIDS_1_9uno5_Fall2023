from scapy.all import IP, TCP, send, RandIP

def simulate_unknown_ips():
    # change dest to valid agents ip 
    ip_layer = IP(src=RandIP(), dst="")
    tcp_layer = TCP(dport=80)
    packet = ip_layer/tcp_layer
    send(packet)

if __name__ == "__main__":
    simulate_unknown_ips()