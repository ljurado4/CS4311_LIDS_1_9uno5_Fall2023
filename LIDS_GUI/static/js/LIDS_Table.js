/*
# File: LIDS_Table.js
#
# Description: This JavaScript file is responsible for handling the display of alerts in a table format within the LIDS Dashboard web application.
#
# @ Author: Benjamin Hansen
# @ Modifier: Benjamin Hansen
# @ Modifier: Lizbeth Jurado PCAP
*/

document.addEventListener("DOMContentLoaded", function () {
    fetchLatestAlerts();

    setInterval(fetchLatestAlerts, 20000);

    // Event listener for the "Sort Alerts" button
    // document.getElementById("sortAlertsButton").addEventListener("click", function () {
    //     sortAlertsByLevel();
    // });
});
// @ Author: Benjamin Hansen
// @ Modifier: Benjamin Hansen
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
// @ Author: Benjamin Hansen
// @ Modifier: Benjamin Hansen
// @modifier: Arturo Olmos
function populateTable(alerts) {
    const tbody = document.getElementById("alertBoxTable").getElementsByTagName("tbody")[0];
    tbody.innerHTML = ""; // Clear previous rows
    let idNum = 1
    alerts.forEach(alert => {
        let row = tbody.insertRow();
        row.id = "Alert" + idNum.toString()
        

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
        identifierCell.textContent = alert.Identifier;
        levelCell.textContent = alert.Level;
        sourceIPCell.textContent = alert.SourceIP;
        sourcePortCell.textContent = alert.SourcePort;
        DestinationIPCell.textContent = alert.DestIP;
        DestinationPortCell.textContent = alert.DestPort;
        typeAlertCell.textContent = alert.TypeAlert;
        descriptionCell.textContent = alert.Description;

        if(alert.Level === 1){
            levelCell.classList.add('level1')
        } else if (alert.Level === 2){
            levelCell.classList.add('level2')
        } else if (alert.Level === 3){
            levelCell.classList.add('level3')
        }

  

        // Add a "Show PCAP" button to open PCAP data in a separate window
        let pcapCell = row.insertCell(9)
        let displayPCAPButton = "<button class = \"alertDescriptionButton\" value = \"" + row.id.toString() + "\" onclick = \"displayAlert(value)\">PCAP</button>"
        pcapCell.innerHTML = displayPCAPButton

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
//@ Author: Lizbeth Jurado
function showPcapData(identifier) {
    fetch(`/show_pcap/${identifier}`) // Use path parameter to match the Flask route
        .then(response => response.text())
        .then(pcapData => {
            let pcapTab = window.open("", "_blank");
            pcapTab.document.write(`<pre>${pcapData}</pre>`);
        })
        .catch(error => {
            console.error("There was an error fetching the PCAP data!", error);
        });
}
/* @author Arturo Olmos */
// Function to display alert details
function displayAlert(alertID){
    let row = document.getElementById(alertID)
    let myWindow = window.open("");
    //contents alert, ready to be displayed in new window
    let alertDisplay =  "Time:" + row.cells[0].innerHTML + 
    "<br>Identifier:" + row.cells[1].innerHTML + 
    "<br>Level:" + row.cells[2].innerHTML + 
    "<br>SourceIP:" + row.cells[3].innerHTML +
    "<br>SourcePort:" + row.cells[4].innerHTML + 
    "<br>DestIP:" + row.cells[5].innerHTML +
    "<br>DestPort:" + row.cells[6].innerHTML +
    "<br>AlertType:" + row.cells[7].innerHTML + 
    "<br>Description:" + row.cells[8].innerHTML
    let style = "font-size: 48px;" + 
    "text-align: center;" +
    "background-color: #CCCCCC;"
    //add attributes to new window
    myWindow.document.title = alertID.toString()
    myWindow.document.body.style = style
    myWindow.document.body.innerHTML = alertDisplay   
}


