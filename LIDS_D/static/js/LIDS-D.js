//counter used to keep track of malicious packets
let maliciousPacketCount = 0

//adding initial html to malicious packets found
document.getElementById("mpd").innerHTML = "Malicious Packet Count:\n" + maliciousPacketCount.toString()

//handles the start of th server
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

  
// function createSocket() {
//     var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
//     var socket = io.connect(socketUrl);

//     socket.on('update_agent_count', function(count) {
//         document.getElementById('agent_count').innerText = count;
//     });
// }


// window.onload = createSocket;

// var socket = io.connect(window.location.origin);

// socket.on('update_client_list', function(clients) {
//     let tableBody = document.querySelector('.devicesTable tbody');
//     tableBody.innerHTML = '';  // Clear the current rows

//     // For each client, create a new row and append it to the table
//     clients.forEach(client => {
//         let row = tableBody.insertRow();
        
//         let idCell = row.insertCell(0);
//         idCell.textContent = client.id;

//         let nameCell = row.insertCell(1);
//         nameCell.textContent = client.name;

//         let ipCell = row.insertCell(2);
//         ipCell.textContent = client.ip;

//         let statusCell = row.insertCell(3);
//         statusCell.textContent = client.status;
//     });
// });



function socketConnection() {
    var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
    var socket = io.connect(socketUrl);

    socket.on('update_agent_count', function(count) {
        document.getElementById('agent_count').innerText = count;
    });

    socket.on('update_client_list', function(clients) {
        let tableBody = document.querySelector('.devicesTable tbody');
        tableBody.innerHTML = ''; 

        
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
}

window.onload = socketConnection;