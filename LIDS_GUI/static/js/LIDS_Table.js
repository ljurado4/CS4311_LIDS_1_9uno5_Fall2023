/*##################################################################
# File: LIDS_Table.js
#
# Version: [5.0]
#
# Description: This JavaScript file is responsible for handling the 
display of alerts in a table format within the LIDS Dashboard web application.
#
# Modification History:
# [11/01/23] - [3.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Initialize and fetch the latest alerts when the document is loaded.
# - [Task 2]: Set up a periodic interval to refresh and fetch the latest alerts every 20 seconds.
# - [Task 3]: Implement an event listener for the "Sort Alerts" button, enabling the sorting of alerts by level.
# - [Task 4]: Fetch the latest alerts from the backend server.
# - [Task 5]: Populate the table with the fetched alert data.
# - [Task 6]: Provide functionality to open PCAP (Packet Capture) data in a separate window for each alert.
# - [Task 7]: Handle potential errors that may occur during the alert fetching process.
#
################################################################## */
document.addEventListener("DOMContentLoaded", function () {
    fetchLatestAlerts();

    setInterval(fetchLatestAlerts, 20000);

    // Event listener for the "Sort Alerts" button
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

        let timeCell = row.insertCell(0);
        let identifierCell = row.insertCell(1);
        let levelCell = row.insertCell(2);
        let sourceIPCell = row.insertCell(3);
        let sourcePortCell = row.insertCell(4);
        let DestinationIPCell = row.insertCell(5);
        let DestinationPortCell = row.insertCell(6);
        let typeAlertCell = row.insertCell(7);
        let descriptionCell = row.insertCell(8);

        timeCell.textContent = alert.Time;
        identifierCell.textContent = alert.Identifier
        levelCell.textContent = alert.Level;
        sourceIPCell.textContent = alert.SourceIP
        sourcePortCell.textContent = alert.SourcePort
        DestinationIPCell.textContent = alert.DestIP
        DestinationPortCell.textContent = alert.DestPort
        typeAlertCell.textContent = alert.TypeAlert
        descriptionCell.textContent = alert.Description;

        if(alert.Level === 1){
            levelCell.classList.add('level1')
        } else if (alert.Level === 2){
            levelCell.classList.add('level2')
        } else if (alert.Level === 3){
            levelCell.classList.add('level3')
        }

  

        // Add a "Show PCAP" button to open PCAP data in a separate window
        let pcapCell = row.insertCell(9);
        let showPcapButton = document.createElement("button");
        showPcapButton.textContent = "Show PCAP";
        showPcapButton.addEventListener("click", function () {
            showPcapData(alert.PCAPData); // Pass the PCAP data here
        });
        pcapCell.appendChild(showPcapButton);
    });
}

function sortAlertsByLevel() {
    // send a request to the server to sort alerts by level
    fetch("/sort_alerts?sort_by=lvl")
        .then(response => response.json())
        .then(data => {
            //frontend with sorted data (you can call populateTable again)
            populateTable(data);
        })
        .catch(error => {
            console.error("There was an error sorting alerts by level!", error);
        });
}

function showPcapData(pcapData) {
    // Open a new window
    const pcapWindow = window.open("", "PCAP Data", "width=600,height=400");
    
    // Check if the pcapData is a string (text)
    if (typeof pcapData === 'string') {
        // Display the text in the new window
        pcapWindow.document.write("<pre>" + pcapData + "</pre>");
    } else {
        // Handle other data types or formats if needed
        pcapWindow.document.write("Invalid PCAP Data");
    }
}
