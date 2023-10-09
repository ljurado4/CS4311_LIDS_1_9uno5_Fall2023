//counter used to keep track of malicious packets
let maliciousPacketCount = 0

//adding initial html to malicious packets found
document.getElementById("mpd").innerHTML = "Malicious Packet Count:\n" + maliciousPacketCount.toString()

//handles the start of th server
function startServer(){
    //needs to be implemented
    window.location = "LIDS-D_Server_Details"
  }
  