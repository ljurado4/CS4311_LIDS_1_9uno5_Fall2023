##################################################################
# File: PortChecker.py
#
# Version: [5.0]
#
# Description:
# The PortChecker.py module provides functionality for detecting
# potential port scanning activities by tracking the number of
# connection attempts to specific ports from individual source IPs.
# It incorporates threshold-based alerting to identify suspicious
# behavior within a defined timeframe.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Implement the logic to detect potential port scanning
#             activities.
# - [Task 2]: Maintain a count of connections per source IP and
#             destination port combination.
# - [Task 3]: Implement threshold-based alerting for potential
#             port scan detections.
# - [Task 4]: Evaluate the timing of connection attempts to determine
#             if they fall within a suspicious timeframe.
# - [Task 5]: Ensure efficient storage and retrieval of connection
#             data and timestamps.
# - [Task 6]: Test the detection logic under various network scenarios
#             to ensure reliable alerting.
# - [Task 7]: Document the design and functionality for ease of
#             maintenance and future updates.
# - [Task 8]: Optimize the data structures used for tracking connections
#             to handle large scale data efficiently.
# - [Task 9]: Review and refactor the alerting mechanism to align with
#             overall system alert management.
#
##################################################################

class PortDetection:
    def __init__(self):
        self.connection_count = {}  # Tracks counts of connections for srcIP
        self.timeChecker = {}       # Stores the initial timestamp for a srcIP
        self.comboChecker = set()   # Maintains unique srcIP and destinationPort combos

    def port_Checking(self, srcIP, destinationPort, timeOF, timeAllowed, threshold1, threshold2):
        key = f"{srcIP}:{destinationPort}"

        # Initialize the connection count and timestamp if new srcIP
        if srcIP not in self.connection_count:
            self.connection_count[srcIP] = [0, timeOF]
            self.timeChecker[srcIP] = timeOF

        # Increment connection count if the srcIP:destinationPort combo is new
        if key not in self.comboChecker:
            self.connection_count[srcIP][0] += 1
            self.connection_count[srcIP][1] = timeOF
            self.comboChecker.add(key)

        # Check if the count exceeds threshold2 and the time difference is within allowed limits
        if self.connection_count[srcIP][0] >= threshold2:
            time1, time2 = self.connection_count[srcIP][1], self.timeChecker[srcIP]
            if (time1 - time2).total_seconds() <= timeAllowed:
                return "threshold2"

        # Check if the count exceeds threshold1 and the time difference is within allowed limits
        elif self.connection_count[srcIP][0] >= threshold1:
            time1, time2 = self.connection_count[srcIP][1], self.timeChecker[srcIP]
            if (time1 - time2).total_seconds() <= timeAllowed:
                return "threshold1"
