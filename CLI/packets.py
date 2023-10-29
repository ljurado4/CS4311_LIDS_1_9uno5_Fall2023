#packets.py

import pyshark
from datetime import datetime
import threading as th
from threading import Semaphore
from flask import Flask, jsonify

class PackTime:
    packet_list = []
    packets_captured = 0
    cap_sem = Semaphore(1)
    process_sem = Semaphore(0)

    def __init__(self):
        self.pack_time = None
        base_path = "/Users/lizbethjurado/Git/CS4311_LIDS_19uno5_Fall2023/Traffic/" 
        #TODO: find a way to store files in github repo, giving too larger error even with installing Git LFS
        self.files = [
            base_path + "7-17-EN.pcapng",
            base_path + "AA_Day1_Traffic.pcapng",
            base_path + "cvi.pcapng",
            base_path + "eth0-LDV-wireshark.pcapng",
            base_path + "nmap scan.pcapng",
            base_path + "sv_day1traffic.pcapng",
            base_path + "vd_07.17.23.pcapng"
        ]

    def alertDetector(self, packet):
        # TODO: Implement  alert detection
        
        return False

    def create_packet(self, in_packet):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        if 'IP' in in_packet:
            src = in_packet.ip.src
            dst = in_packet.ip.dst
            # TODO: packet cretaion

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
                # If packet is suspicious, pull packet and move elsewhere
                # For demonstration purposes, we'll print an alert message
                print(f"Alert! Suspicious packet detected: {packet}")
                # TODO: Handle this packet accordingly (e.g., move to another list, notify user, etc.)
            else:
                # If packet is not suspicious, process as usual
                print("Packet: ", packet)

            self.cap_sem.release()

    def process_pcap_files(self):
        for file in self.files:
            cap = pyshark.FileCapture(file)
            for packet in cap:
                # existing packet handling logic
      
                print(packet)

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

        # after processing live traffic process the pcap files
        self.process_pcap_files()
