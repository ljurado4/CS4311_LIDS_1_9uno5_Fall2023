//network_info.js
// Connect to the Flask SocketIO server
var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
var socket = io.connect(socketUrl);

// Listen for 'update_data' event from the server
socket.on('update_data', function(data) {
    // Clear the existing rows in the table
    var tbody = document.querySelector('.devicesTable tbody');
    tbody.innerHTML = "";

    // Add new rows to the table
    for (var i = 0; i < data.length; i++) {
        var device = data[i];
        var row = tbody.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        cell1.innerHTML = device.id;
        cell2.innerHTML = device.name;
        cell3.innerHTML = device.ip;
        cell4.innerHTML = device.status;
    }
});