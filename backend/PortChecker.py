#PortChecker.py

#append source ip to dict if if it is not already in the dict
#ip will be key in dict and value will start at 0
#have a set of all combos (ip and port)
#if the combo is not in set then increment the value of of the key(ip) by one
#if key is greater than 500 then raise an alert

#add in the timestamp as a value in the dict
#once the value of 500 is reached subtract the newest time from the oldest time and see if it meets time requirement

class portDetection:
    def __init__(self):
        self.connection_count = {}
        self.timeChecker = {}
        self.comboChecker = []

    def port_Checking(self,srcIP,destinationPort, timeOF, timeAllowed, threshold1, threshold2):
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


    
    
    
    
    #def update_connection_count(self, ip, port, threshold,threshold2):
     #   key = f"{ip}:{port}"
      #  if key in self.connection_count:
       #     self.connection_count[key] += 1
        #    if self.connection_count[key] > threshold2:
         #       return "threshold2"
          #  if self.connection_count[key] > threshold:
           #     return "threshold1"
        #else:
         #   self.connection_count[key] = 1
        #return False
