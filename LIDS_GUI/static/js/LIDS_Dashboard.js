//get forms for event listeners
const middleContainer = document.getElementById("middleContainer")
const configFileForm = document.querySelector("#configFileForm")
const alertsTableFrom = document.querySelector("#alertsTableForm")
const disconnectForm = document.querySelector("#disconnectButtonForm")

//state variables for html
let alertsTableState = middleContainer.innerHTML
//formatting xml file output
let xmlConfigState = "<textarea class = \"xmlFileTextArea\">File Name: "  + window.localStorage.getItem("xmlFileName") + "\n" + window.localStorage.getItem("xmlFile") + "</textarea>"

//froms for event listeners

//handles event when user wants to see config file
configFileForm.addEventListener("submit", (event) => {
    event.preventDefault()
    
    alertsTableState = middleContainer.innerHTML
    middleContainer.innerHTML = xmlConfigState
})
//handles event when user wants to see alerts displayed
alertsTableFrom.addEventListener("submit", (event) => {
    event.preventDefault()
    xmlConfigState = middleContainer.innerHTML
    middleContainer.innerHTML = alertsTableState
    
})
//hadles the disconnection of the device
disconnectForm.addEventListener("submit", (event) => {
    event.preventDefault()
    window.location = "LIDS_Main"
})
function toggleDropdown() {
    let dropdownContent = document.getElementById("sortByDropdownContent");
    if (dropdownContent.style.display === "none" || !dropdownContent.style.display) {
        dropdownContent.style.display = "block";
    } else {
        dropdownContent.style.display = "none";
    }
}

function sortTable(n) {
    let table = document.getElementById("alertBoxTable");
    let rows = Array.from(table.rows).slice(1);  // skip the header
    rows.sort((r1, r2) => r1.cells[n].textContent.localeCompare(r2.cells[n].textContent));
    rows.forEach(row => table.tBodies[0].appendChild(row));
}

$(document).ready(function () {
    $.getJSON("https://api.ipify.org?format=json", data => {
        $("#headerTitle").text((i, originalText) => originalText += " " + data.ip);
    });
});

function removeSort() {
    location.reload();
}