//counter used to keep track of malicious packets
let maliciousPacketCount = 0;

//adding initial html to malicious packets found
document.getElementById("mpd").innerHTML = "Malicious Packet Count:\n" + maliciousPacketCount.toString();



//handles the start of the server
function startServer() {
    fetch('/start_socket_server', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Server started") {
            alert("Server started successfully!");
            window.location = "LIDS-D_Server_Details";  // Redirects to the new page
        } else {
            alert("There was an issue starting the server.");
        }
    })
    .catch(error => {
        console.error("There was an error starting the server:", error);
    });
}

function createSocket() {
    var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
    var socket = io.connect(socketUrl);


    socket.on('update_agent_count', function(count) {
        console.log('Received agent count:', count);
        document.getElementById('agent_count').innerText = count;
    });
}



window.onload = createSocket()

