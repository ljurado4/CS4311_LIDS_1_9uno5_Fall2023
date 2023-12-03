# File: packets.py
#
# Description: Includes methods for creating and handling network packets. It also imports various modules and defines class attributes for managing packet data and synchronization.
#
# @ Author: 
# @ Modifier:Alejandro Hernandez
# @ Modifier:Lizbeth Jurado
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
    packet_list_Keep = []
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


# @ Modifier:Alejandro Hernandez
    
    def create_packet(self, in_packet):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        if 'IP' in in_packet or "Src" in in_packet or "Source" in in_packet:
            src = in_packet.ip.src
            dst = in_packet.ip.dst
            handShake = False
            # print()
            if 'TCP' in in_packet:
                flags = in_packet.tcp.flags
                protocol = 'TCP'
                flags = in_packet.tcp.flags
                flags2 = int(in_packet.tcp.flags,16)
                src_port = in_packet.tcp.srcport
                dst_port = in_packet.tcp.dstport
                if in_packet.tcp.flags_fin == 1 or in_packet.tcp.flags_fin in in_packet or in_packet.tcp.flags_push in in_packet or in_packet.tcp.flags_push == 1 or in_packet.tcp.flags_reset == 1 or in_packet.tcp.flags_reset in in_packet or in_packet.tcp.flags_urg == 1 or in_packet.tcp.flags_urg in in_packet or in_packet.tcp.flags_ack == 1 or in_packet.tcp.flags_ack in in_packet:
                    handShake = True
                if in_packet.tcp.flags_syn == '1' and in_packet.tcp.flags_ack == '0':
                    # print("True")
                    handShake = True
                if flags2 and 0x02:
                    description = 'TCP Handshake SYN'
                    handShake = True
                    # print("True")
                else:
                    description = 'Other TCP Packet'
                    handShake = False
            elif 'UDP' in in_packet:
                src_port = in_packet.udp.srcport
                dst_port = in_packet.udp.dstport
                protocol = 'UDP'
                description = 'UDP Packet'
                if in_packet.transport_layer == 'UDP':
                    handShake = True
                else:
                    handShake = False
            elif 'ICMP' in in_packet:
                protocol = 'ICMP'
                description = 'ICMP Packet'
                src_port = "321"
                dst_port = "123"
                handShake = True
            elif 'SSH' in in_packet:
                protocol = 'SSH'
                description = 'SSH Packet'
                handShake = False
            elif 'RDP' in in_packet:
                protocol = 'RDP'
                description = 'RDP Packet'
                handShake = False
            elif 'FTP' in in_packet:
                protocol = 'FTP'
                description = 'FTP Packet'
                handShake = False
            elif 'SCTP' in in_packet:
                protocol = 'SCTP'
                description = 'SCTP Packet'
                if in_packet.sctp.chunk_type in in_packet or in_packet.sctp.chunk_type in in_packet:
                    handShake = True
            else:
                protocol = 'Other'
                description = "Unknown/Other Protocol"
                src_port = "321"
                dst_port = "123"
                handshake = False
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
                "PCAPData": pcap_data,  # Add the actual PCAP data here
                "HandShake" : handShake
            }

            
            self.packet_list.append(temp_packet_dict)
            PackTime.packet_list_Keep.append(temp_packet_dict)

# @ Modifier:Alejandro Hernandez

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
                self.packet_analyzer.analyze_packet(packet,time, self.identifier,packet["SourceIP"],packet["SourcePort"],packet["DestinationIP"],packet["DestinationPort"],packet["Protocol"],packet["HandShake"], PackTime.packet_list_Keep)
            self.cap_sem.release()

# @ Modifier:Alejandro Hernandez
    
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

# @ Modified: LizbethBranch
# For macOS
            capture = pyshark.LiveCapture(interface="en0")

            #capture = pyshark.LiveCapture(interface="enp0s3")
           
            #capture = pyshark.LiveCapture()

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
