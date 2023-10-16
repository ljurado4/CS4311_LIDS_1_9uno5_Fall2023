document.addEventListener("DOMContentLoaded", function () {
    fetchLatestAlerts();

    setInterval(fetchLatestAlerts, 5000);

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

        // Add a "Show PCAP" button to open PCAP data in a separate window
        let pcapCell = row.insertCell(6);
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
