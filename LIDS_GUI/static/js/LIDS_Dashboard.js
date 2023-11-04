/*######################################################################
# File: LIDS_Dashboard.js
#
# Version: [5.0]
#
# Description: JavaScript file for managing the LIDS Dashboard web application.
#
# Modification History:
# [11/01/23] - [3.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Get forms and define state variables
# - [Task 2]: Handle events for showing the configuration file
# - [Task 3]: Handle events for displaying alerts table
# - [Task 4]: Define functions for toggling dropdowns
# - [Task 5]: Define a function to filter alerts by level
# - [Task 6]: Define a function for sorting the alerts table
# - [Task 7]: Fetch the user's IP address and display it in the header
# - [Task 8]: Define a function to remove sorting and reload the page
# - [Task 9]: Expose necessary functions globally
#
######################################################################*/

// Get forms for event listeners
const middleContainer = document.getElementById("middleContainer");
const configFileForm = document.querySelector("#configFileForm");
const alertsTableFrom = document.querySelector("#alertsTableForm");
const disconnectForm = document.querySelector("#disconnectButtonForm");

// State variables for HTML
let alertsTableState = middleContainer.innerHTML;
// Formatting XML file output
let xmlConfigState = "<textarea class = \"xmlFileTextArea\">File Name: " + window.localStorage.getItem("xmlFileName") + "\n" + window.localStorage.getItem("xmlFile") + "</textarea>";

// Forms for event listeners

// Handles event when user wants to see config file
configFileForm.addEventListener("submit", (event) => {
    event.preventDefault();
    alertsTableState = middleContainer.innerHTML;
    middleContainer.innerHTML = xmlConfigState;
});

// Handles event when user wants to see alerts displayed
alertsTableFrom.addEventListener("submit", (event) => {
    event.preventDefault();
    xmlConfigState = middleContainer.innerHTML;
    middleContainer.innerHTML = alertsTableState;
});

function toggleDropdown() {
    let dropdownContent = document.getElementById("sortByDropdownContent");
    if (dropdownContent.style.display === "none" || !dropdownContent.style.display) {
        dropdownContent.style.display = "block";
    } else {
        dropdownContent.style.display = "none";
    }
}

function filterByLevel(level) {
    let table = document.getElementById("alertBoxTable");
    let rows = Array.from(table.rows).slice(1);  // skip the header

    rows.forEach(row => {
        const alertLevel = parseInt(row.cells[2].textContent.trim());
        if (alertLevel <= level || level === 5) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}

function toggleFilterDropdown() {
    let dropdownContent = document.getElementById("filterByDropdownContent");
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

// Fetch the IP of the user when the document is ready
$(document).ready(() => {
    $.getJSON("https://api.ipify.org?format=json", (data) => {
        $("#headerTitle").text((i, originalText) => originalText + " " + data.ip);
    });
});

// Function to remove sorting and reload the page
function removeSort() {
    location.reload();
}

// Expose functions that you need globally.
window.toggleDropdown = toggleDropdown;
window.sortTable = sortTable;
window.removeSort = removeSort;
window.filterByLevel = filterByLevel;
window.toggleFilterDropdown = toggleFilterDropdown;
