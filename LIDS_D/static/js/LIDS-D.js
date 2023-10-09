//counter used to keep track of malicious packets
let maliciousPacketCount = 0

//adding initial html to malicious packets found
document.getElementById("mpd").innerHTML = "Malicious Packet Count:\n" + maliciousPacketCount.toString()

//handles the start of th server
function startServer(){
    //needs to be implemented
    window.location = "LIDS-D_Server_Details"
  }
  

var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
var socket = io.connect(socketUrl);
    socket.on('update_agent_count', function(count) {
        // Update the displayed count when the event is received
        document.getElementById('agent_count').innerText = count;
    });
