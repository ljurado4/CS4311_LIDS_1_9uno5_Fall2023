#packets.py

import pyshark
from datetime import datetime
import threading as th
from threading import Semaphore
import os
import os
import glob
import asyncio
from . import packet_analyzer
import time

"""
NOTE: Used Python 3.11 because interpreter could 
not resolve the pyshark import

NOTE: For pyshark utilization
With Python311 and Python311\Scripts in PATH, use 'pip install pyshark'

"""
class PackTime:
    packet_list = []
    checker = False
    ipList = []
    ipDouble = []
    identifier = 0
    ################
    #Delete when alert logic is ready, only exits to 
    #limit packets for testing
    packets_captured = 0
    #################
    cap_sem = Semaphore(1)
    process_sem = Semaphore(0)

    packet_analyzer = packet_analyzer.PacketAnalyzer()

    def __init__(self):
        self.pack_time = None
        self.packetAnalyzer = packet_analyzer.PacketAnalyzer 
    """
    create_packet will take in a packet and format the packet to be 
    enqueued to the global list of packets
    """
    def create_packet(self,in_packet):
        
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
                dst_port = "123"
                
            else:
                protocol = 'Other'
                description = "Unknown/Other Protocol"
                dst_port = "123"
            packet_length = int(in_packet.length)
            temp_packet_dict = {
                "Time": time,
                "Source": src,
                "Destination": dst,
                "Protocol": protocol,
                "Length": packet_length,
                "Description": description,
                "Port": dst_port
            }
            self.packet_list.append(temp_packet_dict)

    """
    packet_handler will dequeue a packet from the list and will use the alert logic
    to analyze the packet and determine if it is an alert
    """
    def packet_handler(self):
        
        while True:
            self.process_sem.acquire()
            self.cap_sem.acquire()
            if not self.packet_list:
                self.cap_sem.release()
                break
            packet = self.packet_list.pop(0)
            # Add alert detecting logic here
            #Something along the lines of
            #if alertDetector(in_packet):
            #pull packet and move elsewhere

            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            #if type(packet) == dict:
             #   if packet["Source"] in self.ipDouble:
              #      lvl = "3"
                
               # elif packet["Source"] in self.ipList:
                #    lvl = "2"
                 #   self.ipDouble.append(packet["Source"])
                #else:
                 #  self.ipList.append(packet["Source"])
                  #  lvl = "1"
            if type(packet) == dict:
                self.identifier += 1
                self.packet_analyzer.analyze_packet(packet,self.identifier,time, packet["Source"], packet["Port"])

                
            self.cap_sem.release()

    """
    Used as driver code of the class, starts
    sniffing the network using previous classes
    on differing threads
    """

    
    def run_sniffer(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            # Base directory where all the pcapng files are located
            base_dir = os.path.expanduser("C:\\Users\\User\\Documents\\traffic\\traffic")
            # List of pcapng filenames
            pcap_files = [
                "7-17-EN.pcapng",
                "AA_Day1_Traffic.pcapng",
                "cvi.pcapng",
                "eth0-LDV-wireshark.pcapng",
                "7-17-EN.pcapng",
                "nmap scan.pcapng",
                "sv_day1traffic.pcapng",
                "vd_.07..17.23.pcapng"
            ]

            # Construct full paths
            pcap_file_paths = [os.path.join(base_dir, filename) for filename in pcap_files]

            packet_handler_thread = th.Thread(target=self.packet_handler)
            packet_handler_thread.start()

            for pcap_file in pcap_file_paths:
                capture = pyshark.FileCapture(pcap_file)
                
                for in_packet in capture:
                    self.cap_sem.acquire()
                    packet = self.create_packet(in_packet)
                    self.packet_list.append(packet)
                    self.process_sem.release()
                    self.cap_sem.release()
                    time.sleep(1)


                capture.close()  # Close the capture for this file

            # Notify the packet_handler thread that no more packets are coming
            packet_handler_thread.join()
        finally:
            loop.close()
        
        
        
        
        #pcap_path = "C:\\Users\\jandr\\OneDrive\\Documents\\7-17-EN.pcapng"

        #packet_handler_thread = th.Thread(target=self.packet_handler)
        #packet_handler_thread.start()

        #capture = pyshark.FileCapture(pcap_path)



        #for in_packet in capture:
            #self.cap_sem.acquire()
            #packet = self.create_packet(in_packet)
            #self.packet_list.append(packet)
            #self.process_sem.release()
            #self.cap_sem.release()

        #capture.close()  # Close the capture for this file

        # Notify the packet_handler thread that no more packets are coming
        #packet_handler_thread.join()






        #for in_packet in capture:
         #   self.cap_sem.acquire()
          #  packet = self.create_packet(in_packet)
           # self.packet_list.append(packet)
            #self.process_sem.release()
            #self.cap_sem.release()

        # Notify the packet_handler thread that no more packets are coming
        #packet_handler_thread.join()
        
        
        
        
        #packet_handler_thread = th.Thread(target=self.packet_handler)#asdf adf

        #packet_handler_thread.start()

        #for in_packet in self.capture.sniff_continuously():
         #   self.cap_sem.acquire()
          #  self.create_packet(in_packet)
           # self.process_sem.release()
            #################
            #self.packets_captured += 1
            #if self.packets_captured >= 5:
             #   break
            #################
            #self.cap_sem.release()

        #packet_handler_thread.start()

        #for in_packet in self.capture.sniff_continuously():
         #   self.cap_sem.acquire()
          #  self.create_packet(in_packet)
           # self.process_sem.release()
            #################
            #self.packets_captured += 1
            #if self.packets_captured >= 5:
             #   break
            #################
            #self.cap_sem.release()