# File: loginCheck.py
#
# Description:This file contains functionality for monitoring and identifying failed login attempts in network packets, but the detailed use case and context may depend on how this class is used within a larger system.
#
# @ Author: Alejandro Hernandez
# @ Modifier:

class LoginCheck:
    
    def __init__(self):
        self.timeList = []

# @ Author: Alejandro Hernandez

    def failedPssWrd(self, packet, protocol,timeOF,destPort,threshold):
        if protocol == "TCP":
            if destPort == '3389':
                self.timeList.append(timeOF)
                time1 = self.timeList[len(self.timeList)-1]
                time2 = self.timeList[len(self.timeList)-2]
                time_difference = time2 - time1
                time_difference_seconds = int(time_difference.total_seconds())
                if time_difference_seconds <= threshold:
                    return True
        
        if protocol == "SSH":
            ssh_display = packet.ssh.display.lower()
            if "authentication failed" in ssh_display or'51' in ssh_display or '51'in packet.ssh.get('msg_code','N/A') or "SSH_MSG_USERAUTH_FAILURE" in packet.ssh.get('msg_code','N/A'):
                return True

        if protocol == "RDP":
            rdp_status = packet.rdp.status.lower()
            if "authentication failure" in rdp_status:
                return True

        if protocol == "FTP":
            ftp_response_msg = packet.ftp.response_msg.lower()
            if "login failed" in ftp_response_msg or '530' in ftp_response_msg or '530' in packet.ftp.get('response_code','N/A'):
                return True
        
    