#packets.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyshark
from datetime import datetime
import threading as th
from threading import Semaphore
import os
import asyncio
import webbrowser
from . import packet_analyzer,ipChecker
import time
from config_condition import config_condition

class PackTime:
    packet_list = []
    checker = False
    ipList = []
    ipDouble = []
    identifier = 0
    packets_captured = 0
    cap_sem = Semaphore(1)
    process_sem = Semaphore(0)
    packet_analyzer = packet_analyzer.PacketAnalyzer()

    def __init__(self):
        self.pack_time = None

    #Modified by Alejandro Hernanded 
    
    def create_packet(self, in_packet):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        if 'IP' in in_packet or "Src" in in_packet or "Source" in in_packet:
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
                src_port = in_packet.udp.srcport
                dst_port = in_packet.udp.dstport
                protocol = 'UDP'
                description = 'UDP Packet'
            elif 'ICMP' in in_packet:
                protocol = 'ICMP'
                description = 'ICMP Packet'
                src_port = "321"
                dst_port = "123"
            elif 'SSH' in in_packet:
                protocol = 'SSH'
                description = 'SSH Packet'
            elif 'RDP' in in_packet:
                protocol = 'RDP'
                description = 'RDP Packet'
            elif 'FTP' in in_packet:
                protocol = 'FTP'
                description = 'FTP Packet'
            else:
                protocol = 'Other'
                description = "Unknown/Other Protocol"
                src_port = "321"
                dst_port = "123"
            packet_length = int(in_packet.length)
            pcap_data = str(in_packet)  # Capture PCAP data as a string
            temp_packet_dict = {
                "Time": time,
                "SourceIP": src,
                "DestinationIP": dst,
                "Protocol": protocol,
                "Length": packet_length,
                "Description": description,
                "SourcePort": src_port,
                "DestinationPort": dst_port,
                "PCAPData": pcap_data  # Add the actual PCAP data here
            }
            self.packet_list.append(temp_packet_dict)

    #modified by Alejandro Hernandez

    def packet_handler(self):
        while True:
            self.process_sem.acquire()
            self.cap_sem.acquire()
            if not self.packet_list:
                self.cap_sem.release()
                break
            packet = self.packet_list.pop(0)
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            #time = datetime.strptime(time0,"%Y-%m-%d %H:%M:%S.%f")
            if type(packet) == dict:
                self.identifier += 1
                self.packet_analyzer.analyze_packet(packet,time, self.identifier,packet["SourceIP"],packet["SourcePort"],packet["DestinationIP"],packet["DestinationPort"],packet["Protocol"])
            self.cap_sem.release()

    #Modified by Alejandro Hernandez
    
    def run_sniffer(self):
        # Wait for the configuration
        with config_condition:
            config_condition.wait()  # Wait for notification
            config = ipChecker.ip_Checker.configuration
            
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:

            packet_handler_thread = th.Thread(target=self.packet_handler)
            packet_handler_thread.start()

            capture = pyshark.LiveCapture(interface="enp0s3")
            # capture = pyshark.LiveCapture()
            for in_packet in capture:

                self.cap_sem.acquire()
                packet = self.create_packet(in_packet)
                self.packet_list.append(packet)
                self.process_sem.release()
                self.cap_sem.release()


            packet_handler_thread.join()
        finally:
            loop.close()

def show_pcap_data(pcap_data):
    with open('temp_pcap.html', 'w') as temp_file:
        temp_file.write(f'<pre>{pcap_data}</pre>')

    webbrowser.open('temp_pcap.html')
