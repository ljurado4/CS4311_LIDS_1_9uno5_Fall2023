var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
var socket = io.connect(socketUrl + '/lids-d');

socket.on('update_devices', function(data) {
    var recognizedDevices = data.recognized_devices;
    var unrecognizedDevices = data.unrecognized_devices;

    // Handling recognized devices
    console.log('Recognized devices:', recognizedDevices);

    var recognizedTbody = document.querySelector('.devicesTable tbody');
    recognizedTbody.innerHTML = "";

    for (var i = 0; i < recognizedDevices.length; i++) {
        var device = recognizedDevices[i];
        var row = recognizedTbody.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        cell1.innerHTML = device.id;
        cell2.innerHTML = device.name;
        cell3.innerHTML = device.ip;
        cell4.innerHTML = device.status;
    }

    // Handling unrecognized devices
    console.log('Unrecognized devices:', unrecognizedDevices);

    var unrecognizedTbody = document.querySelector('#unkownDevices .devicesTable tbody');
    unrecognizedTbody.innerHTML = "";

    for (var j = 0; j < unrecognizedDevices.length; j++) {
        var device = unrecognizedDevices[j];
        var row = unrecognizedTbody.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);

        cell1.innerHTML = device.ip;
        cell2.innerHTML = device.port;
        cell3.innerHTML = device.protocol;


        console.log("device.port",device.port);
        console.log("device.ip",device.ip);

    }
});