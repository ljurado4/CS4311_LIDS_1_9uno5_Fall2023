/* ######################################################################
   # File: alerts_table.js
   #
   # Version: [5.0]
   #
   # Description: This file is esponsible for handling and displaying alerts data in an HTML table format.
   #

   ###################################################################### */
// Author and modified Benjamin Hansen
// Construct the socket URL based on the current location
var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
// Author and modified Benjamin Hansen
// Connect to the 'lids-d' socket.io namespace
var socket = io.connect(socketUrl + '/lids-d');
// Author and modified Benjamin Hansen
// Function to update the HTML table with alert data
function updateTable(data) {
    // Get the table body element
    const tableBody = document.querySelector('#TableID tbody');
    
    console.log("Before foor loop"+data)
    // Clear the table body
    tableBody.innerHTML = '';
    
    // Loop through the alert data and create table rows
    data.forEach((alert, index) => {
       

        const row = tableBody.insertRow(index);
        row.id = `alert${index + 1}`;
        
        // Create table cells for alert properties
        const timeCell = row.insertCell(0);
        timeCell.id = `alert${index + 1}-time`;
        timeCell.textContent = alert.Time; 
    
        const identifierCell = row.insertCell(1);
        identifierCell.id = `alert${index + 1}-identifier`;
        identifierCell.textContent = alert.Identifier; 
    
        const levelCell = row.insertCell(2);
        levelCell.id = `alert${index + 1}-level`;
        levelCell.textContent = alert.Level; 
    
        const sourceIpCell = row.insertCell(3);
        sourceIpCell.id = `alert${index + 1}-sourceIp`;
        sourceIpCell.textContent = alert.SourceIP; 
    
        const sourcePortCell = row.insertCell(4);
        sourcePortCell.id = `alert${index + 1}-sourcePort`;
        sourcePortCell.textContent = alert.SourcePort;
    
        const destIpCell = row.insertCell(5);
        destIpCell.id = `alert${index + 1}-destIp`;
        destIpCell.textContent = alert.DestIP; 
    
        const destPortCell = row.insertCell(6);
        destPortCell.id = `alert${index + 1}-destPort`;
        destPortCell.textContent = alert.DestPort;
    
        const typeAlertCell = row.insertCell(7);
        typeAlertCell.id = `alert${index + 1}-typeAlert`;
        typeAlertCell.textContent = alert.TypeAlert; 
    
        const descriptionCell = row.insertCell(8);
        descriptionCell.id = `alert${index + 1}-description`;
        descriptionCell.innerHTML = `<button id="alert${index + 1}-button" class="alertDescriptionButton" onclick="displayAlert(this.id)">${alert.Description}</button>`; 
     });
}
// Author and modified Benjamin Hansen
// Socket.IO event listener for the 'new_alert_data' event
socket.on('new_alert_data', function(data) {
    updateTable(data);
});
