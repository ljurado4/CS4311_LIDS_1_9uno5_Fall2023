import ipChecker 

#loginCheck.py
class loginCheck:
    def __init__(self,portList):
        self.portList = portList

    def failedPssWrd(self, packet):
        if "SSH" in packet:
            ssh_display = packet.ssh.display.lower()
            return "authentication failed" in ssh_display

        if "RDP" in packet:
            rdp_status = packet.rdp.status.lower()
            return "authentication failure" in rdp_status

        if "FTP" in packet:
            ftp_response_msg = packet.ftp.response_msg.lower()
            return "login failed" in ftp_response_msg

        if not self.ip_in_List(packet.src):
            ip_notIn_list = packet.ip.notIn.list.lower()
            return True