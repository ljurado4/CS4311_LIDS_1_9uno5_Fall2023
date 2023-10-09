//counter used to keep track of malicious packets
let maliciousPacketCount = 0

//adding initial html to malicious packets found
document.getElementById("mpd").innerHTML = "Malicious Packet Count:\n" + maliciousPacketCount.toString()

//handles the start of th server
function startServer(){
    //needs to be implemented
    window.location = "LIDS-D_Server_Details"
  }
  
var socket = io.connect(window.location.origin);

socket.on('update_client_list', function(clients) {
    let tableBody = document.querySelector('.devicesTable tbody');
    tableBody.innerHTML = '';  // Clear the current rows

    // For each client, create a new row and append it to the table
    clients.forEach(client => {
        let row = tableBody.insertRow();
        
        let idCell = row.insertCell(0);
        idCell.textContent = client.id;

        let nameCell = row.insertCell(1);
        nameCell.textContent = client.name;

        let ipCell = row.insertCell(2);
        ipCell.textContent = client.ip;

        let statusCell = row.insertCell(3);
        statusCell.textContent = client.status;
    });
});

