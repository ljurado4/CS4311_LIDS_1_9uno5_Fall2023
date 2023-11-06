/* ######################################################################
   # File: alerts_table.js
   #
   # Version: [5.0]
   #
   # Description: This file is esponsible for handling and displaying alerts data in an HTML table format.
   #
   # Modification History:
   # [11/01/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
   #
   ###################################################################### */

// Construct the socket URL based on the current location
var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');

// Connect to the 'lids-d' socket.io namespace
var socket = io.connect(socketUrl + '/lids-d');

// Function to update the HTML table with alert data
function updateTable(data) {
    // Get the table body element
    const tableBody = document.querySelector('#TableID tbody');
    
    // Clear the table body
    tableBody.innerHTML = '';
    
    // Loop through the alert data and create table rows
    data.forEach((alert, index) => {
        const row = tableBody.insertRow(index);
        row.id = `alert${index + 1}`;
        
        // Create table cells for alert properties
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
