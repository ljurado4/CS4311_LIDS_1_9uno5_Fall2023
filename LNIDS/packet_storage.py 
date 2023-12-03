# File: packet_storage.py
#
# Description:  Moves PCAP files from a local storage directory to an external hard drive at regular intervals.
# 
# @Author: Lizbeth Jurado

import os
import shutil
import time
from datetime import datetime

class PacketStorage:
    def __init__(self, local_storage_path, external_storage_path, storage_interval):
        self.local_storage_path = local_storage_path
        self.external_storage_path = external_storage_path
        self.storage_interval = storage_interval

    def start_storage_process(self):
        while True:
            time.sleep(self.storage_interval)
            self.move_files_to_external_storage()

    def move_files_to_external_storage(self):
        for filename in os.listdir(self.local_storage_path):
            if filename.endswith('.pcap'):
                local_file_path = os.path.join(self.local_storage_path, filename)
                external_file_path = os.path.join(self.external_storage_path, filename)
                shutil.move(local_file_path, external_file_path)
                print(f'Moved {filename} to external storage.')


local_storage_path = '/path/to/local/pcap/storage'  # Replace with your actual local storage path
external_storage_path = '/path/to/external/hard/drive'  # Replace with your actual external storage mount point
storage_interval = 120  # Time interval in seconds for moving files

packet_storage = PacketStorage(local_storage_path, external_storage_path, storage_interval)
packet_storage.start_storage_process()
