##################################################################
# File: loginCheck.py
#
# Version: [5.0]
#
# Description: 
# This module provides the loginCheck class which is used to check
# for failed login attempts over various protocols such as SSH, RDP,
# and FTP by analyzing packet data.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Define the class constructor to accept a list of ports
#             relevant to the protocols to be checked.
# - [Task 2]: Implement the failedPssWrd method to parse packet data
#             for failed login attempts.
# - [Task 3]: Ensure the method accounts for different protocol packet
#             structures and authentication failure messages.
# - [Task 4]: Expand the method to cover more protocols if necessary.
# - [Task 5]: Add error handling and input validation to prevent
#             crashes and ensure secure operations.
# - [Task 6]: Create a logging mechanism to record detected authentication
#             failures for further analysis.
# - [Task 7]: Optimize performance to handle a high volume of packets.
# - [Task 8]: Document the class and its methods clearly for future maintenance.
# - [Task 9]: Write unit tests to verify the functionality under various scenarios.
# - [Task 10]: Consider integration with alerting systems to notify admins of
#              detected authentication failures in real-time.
#
##################################################################

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
