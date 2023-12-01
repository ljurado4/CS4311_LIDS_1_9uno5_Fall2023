# File: PortChecker.py
#
# Description: Detection and monitoring of network port connections and their associated timestamps. The class includes methods for checking port-related events and maintaining connection count and time records for source IP addresses. 
#
# @ Author:Alejandro Hernandez
# @ Modifier:


from datetime import datetime


class portDetection:
    def __init__(self):
        self.connection_count = {}
        self.timeChecker = {}
        self.comboChecker = []

# @ Author:Alejandro Hernandez
    def port_Checking(self,srcIP, destinationPort, timeOf, timeAllowed, threshold1, threshold2, packetList):
        
        unique_destination_ports = set(d["DestinationPort"] for d in packetList if d["SourceIP"] == srcIP)
        different_Destination = len(unique_destination_ports)


        firstTime = None

        for d in packetList:
            if d["SourceIP"] == srcIP and firstTime is None:
                firstTime = d["Time"]
                break 
        
        
        firstTimeFR = datetime.strptime(firstTime,"%Y-%m-%d %H:%M:%S.%f")
        timeDifference = timeOf - firstTimeFR
        timeDifferenceSeconds = int(timeDifference.total_seconds())


        if different_Destination >= threshold2 and timeDifferenceSeconds <= timeAllowed:
            return "threshold2"
        
        elif different_Destination >= threshold1 and timeDifferenceSeconds <= timeAllowed:
            return "threshold1"

        else:
            return False


        
        
        """
        key = f"{srcIP}:{destinationPort}"

        if srcIP not in self.connection_count:
            self.connection_count[srcIP] = [0,timeOF]
            self.timeChecker[srcIP] = timeOF
        if key not in self.comboChecker:
            self.connection_count[srcIP][0] += 1
            self.connection_count[srcIP][1] = timeOF

        self.comboChecker.append(key)
        
        if self.connection_count[srcIP][0] >= threshold2:
            time1 = self.connection_count[srcIP][1] 
            time2 = self.timeChecker[srcIP]
            time_difference = time1 - time2
            time_difference_seconds = int(time_difference.total_seconds())
            # print(time_difference_seconds)
            if time_difference_seconds <= timeAllowed:
                # print("Thresh")
                return threshold2
        elif self.connection_count[srcIP][0] >= threshold1:
            time1 = self.connection_count[srcIP][1] 
            time2 = self.timeChecker[srcIP]
            time_difference = time1 - time2
            time_difference_seconds = int(time_difference.total_seconds())
            # print(time_difference_seconds)
            if time_difference_seconds <= timeAllowed:
                # print("thresh2")
                return threshold1

        """
    
    
    