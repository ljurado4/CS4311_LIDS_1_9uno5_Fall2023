document.addEventListener("DOMContentLoaded", function() {
    
    fetchLatestAlerts();

    
    setInterval(fetchLatestAlerts, 5000);
});

function fetchLatestAlerts() {
    fetch('/get_alerts')
        .then(response => response.json())
        .then(data => {
            populateTable(data);
        })
        .catch(error => {
            console.error("There was an error fetching the alerts!", error);
        });
}

function populateTable(alerts) {
    const tbody = document.getElementById("alertBoxTable").getElementsByTagName("tbody")[0];
    tbody.innerHTML = ""; // Clear previous rows

    alerts.forEach(alert => {
        let row = tbody.insertRow();

        let levelCell = row.insertCell(0);
        let timeCell = row.insertCell(1);
        let ipCell = row.insertCell(2);
        let portCell = row.insertCell(3);
        let identifierCell = row.insertCell(4);
        let descriptionCell = row.insertCell(5);
        

        levelCell.textContent = alert.Level;
        timeCell.textContent = alert.Time;
        ipCell.textContent = alert.Source;
        portCell.textContent = alert.Port;
        descriptionCell.textContent = alert.Description;
        identifierCell.textContent = alert.identifier;
    });
}