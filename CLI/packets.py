# File: CLI/packets.py
#
# Description: This file contains the implementation of the PackTime class, which is responsible for capturing, processing, and analyzing network packets. It includes methods for capturing live packets, processing PCAP files, and detecting network alerts.
#
# @ Author: Lizbeth Jurado, Seth Velasco
# @ Modifier: 

from menu import Menu
import pyshark
from datetime import datetime
import threading as th
from threading import Semaphore
from flask import Flask, jsonify

class PackTime(Menu):
    packet_list = []
    packets_captured = 0
    cap_sem = Semaphore(1)
    process_sem = Semaphore(0)

# @ Author: Lizbeth Jurado
# @ Modified: Benjamin Hansen (added super init)
    def __init__(self):
<<<<<<< HEAD
        self.pack_time = None
        base_path = "/Users/shas/Git/traffic" 
        # TODO: Find a way to store files in a GitHub repo, giving too large error even with installing Git LFS
        self.files = [
            base_path + "7-17-EN.pcapng",
            base_path + "AA_Day1_Traffic.pcapng",
            base_path + "cvi.pcapng",
            base_path + "eth0-LDV-wireshark.pcapng",
            base_path + "nmap scan.pcapng",
            base_path + "sv_day1traffic.pcapng",
            base_path + "vd_07.17.23.pcapng"
        ]
=======
        super().__init__()


>>>>>>> 72844b86731595f992e6c5b5b1bbd06d5bb39539
# @ Author: Lizbeth Jurado
    def alertDetector(self, packet):
        # TODO: Implement alert detection
        
        return False

# @ Author: Lizbeth Jurado
    def create_packet(self, in_packet):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        if 'IP' in in_packet:
            src = in_packet.ip.src
            dst = in_packet.ip.dst
            # TODO: Packet creation logic

# @ Author: Lizbeth Jurado, Seth Velasco
    def packet_handler(self):
        while True:
            self.process_sem.acquire()
            self.cap_sem.acquire()
            if not self.packet_list:
                self.cap_sem.release()
                break
            packet = self.packet_list.pop(0)

            # Alert detecting logic
            if self.alertDetector(packet):
                # If a packet is suspicious, pull the packet and take appropriate action
                # For demonstration purposes, we'll print an alert message
                print(f"Alert! Suspicious packet detected: {packet}")
                # TODO: Handle this packet accordingly (e.g., move to another list, notify user, etc.)
            else:
                # If the packet is not suspicious, process it as usual
                print("Packet: ", packet)

            self.cap_sem.release()
# @ Author: Lizbeth Jurado
    def process_pcap_files(self):
        for file in self.files:
            cap = pyshark.FileCapture(file)
            for packet in cap:
                # Existing packet handling logic
      
                print(packet)
# @ Author: Lizbeth Jurado, Seth Velasco
    def run_sniffer(self):
        packet_handler_thread = th.Thread(target=self.packet_handler)
        packet_handler_thread.start()

        for in_packet in self.capture.sniff_continuously():
            self.cap_sem.acquire()
            self.create_packet(in_packet)
            self.process_sem.release()
           
            self.packets_captured += 1
            if self.packets_captured >= 5:
                break
          
            self.cap_sem.release()

        # After processing live traffic, process the PCAP files
        self.process_pcap_files()
