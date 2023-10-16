//LIDs_Table.js
document.addEventListener("DOMContentLoaded", function () {
    fetchLatestAlerts();

    setInterval(fetchLatestAlerts, 5000);

    // event listener to the "Sort Alerts" button
    document.getElementById("sortAlertsButton").addEventListener("click", function () {
        sortAlertsByLevel();
    });
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

function sortAlertsByLevel() {
    // Add this code to send a request to the server to sort alerts by level
    fetch("/sort_alerts?sort_by=lvl")
        .then(response => response.json())
        .then(data => {
            // Update the frontend with sorted data (you can call populateTable again)
            populateTable(data);
        })
        .catch(error => {
            console.error("There was an error sorting alerts by level!", error);
        });
}
