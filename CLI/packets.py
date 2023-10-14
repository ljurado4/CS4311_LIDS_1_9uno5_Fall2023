import pyshark
from datetime import datetime
import threading as th
from threading import Semaphore
from CLI.Alerts import Alerts
import asyncio
#from CLI.Alerts 

"""
NOTE: Used Python 3.11 because interpreter could 
not resolve the pyshark import

NOTE: For pyshark utilization
With Python311 and Python311\Scripts in PATH, use 'pip install pyshark'

"""
class PackTime:
    packet_list = []
    #alert_list = []
    ################
    #Delete when alert logic is ready, only exists to 
    #limit packets for testing
    packets_captured = 0
    #################
    queue_sem = Semaphore(1)
    flag_sem = Semaphore(0)

    def __init__(self):
        self.pack_time = None
        self.thread1 = th.Thread(target=self.packet_handler,args=())
        self.thread2 = th.Thread(target = self.start_file_cap,args=("C:\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\AA_Day1_Traffic.pcapng"))

    """
    create_packet will take in a packet and format the packet to be 
    enqueued to the global list of packets
    """
    def create_packet(self,in_packet):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        if 'IP' in in_packet:
            src = in_packet.ip.src
            dst = in_packet.ip.dst
            if 'TCP' in in_packet:
                protocol = 'TCP'
                flags = in_packet.tcp.flags
                src_port = in_packet.tcp.srcport
                dst_port = in_packet.tcp.dstport
                if 'SYN' in flags:
                    description = 'TCP Handshake SYN'
                else:
                    description = 'Other TCP Packet'
            elif 'UDP' in in_packet:
                src_port = in_packet.tcp.srcport
                dst_port = in_packet.tcp.dstport
                protocol = 'UDP'
                description = 'UDP Packet'
            elif 'ICMP' in in_packet:
                protocol = 'ICMP'
                description = 'ICMP Packet'
            else:
                protocol = 'Other'
                description = "Unknown/Other Protocol"
            packet_length = int(in_packet.length)
            temp_packet_dict = {
                "Time": time,
                "Source": src,
                "Destination": dst,
                "Protocol": protocol,
                "Length": packet_length,
                "Description": description
            }
            self.add_alert(severity= "Medium",time= time,IP = src,Port=dst_port,description = description)
            self.packet_list.append(temp_packet_dict)
        
    """
    packet_handler will dequeue a packet from the list and will use the alert logic
    to analyze the packet and determine if it is an alert
    """
    def packet_handler(self):
        #loop = asyncio.new_event_loop()
        #asyncio.set_event_loop(loop)
        #async def handle_packets():
        while True:
            self.flag_sem.acquire()
            self.queue_sem.acquire()
            if not self.packet_list:
                self.queue_sem.release()
                break
            packet = self.packet_list.pop(0)
            #Use packet_analyzer for alert logic
            #self.queue_sem.release()
            print("Packet: ", packet)
        #loop.run_until_complete(handle_packets())

    """
    Creates alert object and appends to alert_list List
    """
    def add_alert(self,severity, time, IP, Port, description):
        alert_to_add = Alerts(severity, time, IP, Port, description)
        self.alert_list.append(alert_to_add)

    def start_file_cap(self,pcap_file):
        capture = pyshark.FileCapture(pcap_file)
        for in_packet in capture:
            self.queue_sem.acquire()
            packet = self.create_packet(in_packet)
            print(in_packet)
            self.packet_list.append(packet)
            self.flag_sem.release()
            self.queue_sem.release()
        capture.close()

    """
    Used as driver code of the class, starts
    sniffing the network using previous classes
    on differing threads
    """
    def run_sniffer(self,):

        pcap_file_paths = ["C\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\7-17-EN.pcapng",
                           "C:\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\AA_Day1_Traffic.pcapng",
                           "C:\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\cvi.pcapng",
                           "C:\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\eth0-LDV-wireshark.pcapng",
                           "C:\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\nmap scan.pcapng",
                           "C:\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\sv_day1traffic.pcapng",
                           "C:\\Users\\velas\\OneDrive\\Documents\\PCAPs\\traffic\\vd_07.17.23.pcapng"]

        packet_handler_thread = th.Thread(target=self.packet_handler())
        packet_handler_thread.start()
        #capture = pyshark.LiveCapture()                                                     

        capture_threads = []
        for pcap_file in pcap_file_paths:
            capture_thread = th.Thread(target=self.start_file_cap,args=(pcap_file))
            capture_threads.append(capture_thread)
            capture_thread.start()
        for thread in capture_threads:
            thread.join()
            """
            capture_thread = th.Thread(target=)
            capture = pyshark.FileCapture(pcap_file)
            
            for in_packet in capture:
                self.queue_sem.acquire()
                packet = self.create_packet(in_packet)
                self.packet_list.append(packet)
                self.flag_sem.release()
                self.queue_sem.release()
            capture.close()  
            """
        self.flag_sem.release()
        # Notify the packet_handler thread that no more packets are coming
        packet_handler_thread.join()

        """
        for in_packet in capture.sniff_continuously():
            self.queue_sem.acquire()
            self.create_packet(in_packet)
            self.flag_sem.release()
            #################
            self.packets_captured += 1
            if self.packets_captured >= 5:
                break
            #################
            self.queue_sem.release()
        """
    #may add or change to export alerts, depending on packet_analyzer implementation
    def export_packets(self):
        return self.packet_list


