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
        

        
        const descriptionCell = row.insertCell(4);
        descriptionCell.innerHTML = `<button id="alert${index + 1}-button" class="alertDescriptionButton" onclick="displayAlert(this.id)">${alert.Description}</button>`; 
    });
}

function fetchLatestAlerts() {
    fetch('/update_alert_data_table')
        .then(response => response.json())
        .then(data => {
            updateTable(data);
        })
        .catch(error => console.error(error));
}

fetchLatestAlerts();

setInterval(fetchLatestAlerts, 5000);
