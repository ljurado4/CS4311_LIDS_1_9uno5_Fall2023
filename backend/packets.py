#packets.py

import pyshark
from datetime import datetime
import threading as th
from threading import Semaphore
import os
import asyncio
import webbrowser
from . import packet_analyzer
import time

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

    def packet_handler(self):
        while True:
            self.process_sem.acquire()
            self.cap_sem.acquire()
            if not self.packet_list:
                self.cap_sem.release()
                break
            packet = self.packet_list.pop(0)
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            if type(packet) == dict:
                self.identifier += 1
                self.packet_analyzer.analyze_packet(packet,time, self.identifier,packet["SourceIP"],packet["SourcePort"],packet["DestinationIP"],packet["DestinationPort"])
            self.cap_sem.release()

    def run_sniffer(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            base_dir = os.path.expanduser("C:\\Users\\jandr\\OneDrive\\Documents\\traffic")
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

                capture.close()

            packet_handler_thread.join()
        finally:
            loop.close()

def show_pcap_data(pcap_data):
    with open('temp_pcap.html', 'w') as temp_file:
        temp_file.write(f'<pre>{pcap_data}</pre>')

    webbrowser.open('temp_pcap.html')
