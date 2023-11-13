# alerts.py

#author: Lizbeth Jurado

class Alerts:
    # Hard-coded path to the PCAP file
    PCAP_FILE_PATH = '/Users/lizbethjurado/Git/CS4311_LIDS_19uno5_Fall2023/7-17-EN.pcapng'

    def __init__(self, time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description):
        self.time = time
        self.identifier = identifier
        self.level = level
        self.sourceIP = sourceIP
        self.sourcePort = sourcePort
        self.destIP = destIP
        self.destPort = destPort
        self.typeAlert = typeAlert
        self.description = description

    def __str__(self):
        return (f"Time: {self.time}, Identifier: {self.identifier}, Level: {self.level}, "
                f"SourceIP: {self.sourceIP}, SourcePort: {self.sourcePort}, "
                f"DestinationIP: {self.destIP}, DestinationPort: {self.destPort}, "
                f"Type of Alert: {self.typeAlert}, Description: {self.description}")

    # Method to return the path of the PCAP file
    @classmethod
    def get_pcap_file_path(cls):
        return cls.PCAP_FILE_PATH
