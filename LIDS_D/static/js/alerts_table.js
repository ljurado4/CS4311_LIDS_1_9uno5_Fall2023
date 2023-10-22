
var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
var socket = io.connect(socketUrl + '/lids-d');

function updateTable(data) {
    const tableBody = document.querySelector('#TableID tbody');
    tableBody.innerHTML = '';
    data.forEach((alert, index) => {
        const row = tableBody.insertRow(index);
        row.id = `alert${index + 1}`;
        
        const levelCell = row.insertCell(0);
        levelCell.id = `alert${index + 1}-level`;
        levelCell.textContent = alert.Level; 
        
        const timeCell = row.insertCell(1);
        timeCell.id = `alert${index + 1}-time`;
        timeCell.textContent = alert.Time; 
        
        const ipCell = row.insertCell(2);
        ipCell.id = `alert${index + 1}-ip`;
        ipCell.textContent = alert.Source; 
        
        const portCell = row.insertCell(3);
        portCell.id = `alert${index + 1}-port`;
        portCell.textContent = alert.Port; 

        const identifierCell = row.insertCell(4);
        identifierCell.id = `alert${index + 1}-identifier`;
        identifierCell.textContent = alert.Port; 

        const descriptionCell = row.insertCell(5);
        descriptionCell.innerHTML = `<button id="alert${index + 1}-button" class="alertDescriptionButton" onclick="displayAlert(this.id)">${alert.Description}</button>`; 
    });
}

// Socket.IO event listener for the 'new_alert_data' event
socket.on('new_alert_data', function(data) {
    updateTable(data);
});

// Initial fetch to get the latest alerts
fetchLatestAlerts();