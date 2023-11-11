/*
   ######################################################################
   # File: LIDS-D.js
   #
   # Version: [5.0]
   #
   # Description: This JavaScript file manages various functionalities related to LIDS-D, including:
   #   - Counting malicious packets
   #   - Starting the server
   #   - Exporting alerts
   #   - Displaying alert details
   #
   # Modification History:
   # [11/01/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
   #
   ######################################################################
*/

// Counter used to keep track of malicious packets
let maliciousPacketCount = 0

// Adding initial HTML to display malicious packets found
document.getElementById("mpd").innerHTML = "Malicious Packet Count:\n" + maliciousPacketCount.toString()

// Function to start the server
function startServer() {
    fetch('/start_socket_server', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Server started") {
            alert("Server started successfully!");
            window.location = "LIDS-D_Server_Details";  // Redirects to the new page
        } else {
            alert("There was an issue starting the server.");
        }
    })
    .catch(error => {
        console.error("There was an error starting the server:", error);
    });
}

/* @author Arturo Olmos */
// Function to display a popup
function pop(){
    var popup = document.getElementById("popup");
    console.log(popup.classList)
    popup.classList.add("show");
  
    console.log("f")
}

/* @author Arturo Olmos */
// Function to open a form
function openForm() {
    document.getElementById("myForm").style.display = "block";
}

/* @author Arturo Olmos */
// Function to close a form
function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

/* @author Arturo Olmos */
// Function to export alerts
function exportAlerts(event){
    event.preventDefault()
    let file = null
    const fileType = document.querySelector('#FileType');
    let exportAlertsFileName = "ExportedAlerts." + fileType.value
    if(fileType.value == "csv"){
        var table = document.getElementById("alertsTable");
        console.log(table)
        let csvTableContents = ""
        for (var i = 0, row; row = table.rows[i]; i++) {
            if(i == 0){
                continue
            }
            // Iterate through rows
            // Rows would be accessed using the "row" variable assigned in the for loop
            let rowContent = ""
            rowContent += row.cells[0].innerHTML + ","  + row.cells[1].innerHTML + "," + row.cells[2].innerHTML + "," + row.cells[3].innerHTML + "," +row.cells[4].innerHTML
        }
        file = new File([csvTableContents], exportAlertsFileName, {
            type: 'text/' + fileType.value,
        })
    } else if(fileType.value == "json"){
        let objects = ""
        var table = document.getElementById("alertsTable");
        for (var i = 0, row; row = table.rows[i]; i++) {
            if(i == 0){
                continue
            }
            // Iterate through rows
            // Rows would be accessed using the "row" variable assigned in the for loop
            let jsonObject = {
                "Level":row.cells[0].innerHTML,
                "Time":row.cells[1].innerHTML,
                "IP":row.cells[2].innerHTML,
                "Port":row.cells[3].innerHTML,
                "Protocol":row.cells[4].innerHTML,
            }
            objects += JSON.stringify(jsonObject) + "\n"
        }
        file = new File([objects], exportAlertsFileName, {
            type: 'text/' + fileType.value,
        })
    } else if(fileType.value == "xml"){ // XML export
        let xmlText = "<?xml version=\"1.0\"?>\n"
        xmlText += "<Alerts>\n"
        var table = document.getElementById("alertsTable");
        for (var i = 0, row; row = table.rows[i]; i++) {
            if(i == 0){
                continue
            }
            // Iterate through rows
            // Rows would be accessed using the "row" variable assigned in the for loop
            xmlText += "  <Alert " + i.toString() + ">\n"
            xmlText += "    <Level>" + row.cells[0].innerHTML + "</Level>\n"
            xmlText += "    <Time>" + row.cells[1].innerHTML + "</Time>\n"
            xmlText += "    <IP>" + row.cells[2].innerHTML + "</IP>\n"
            xmlText += "    <Port>" + row.cells[3].innerHTML + "</Port>\n"
            xmlText += "    <Protocol>" + row.cells[4].innerHTML + "/<Protocol>\n"
            xmlText += "  </Alert " + i.toString() + ">\n"
        }
        xmlText += "</Alerts>\n"
        file = new File([xmlText], exportAlertsFileName, {
            type: 'text/' + fileType.value,
        })
    }
    function download() {
        const link = document.createElement('a')
        const url = URL.createObjectURL(file)
        link.href = url
        link.download = file.name
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
        window.URL.revokeObjectURL(url)
    }
    download()
}

/* @author Arturo Olmos */
// Function to display alert details
function displayAlert(alertID){
    const alertInfo = alertID.split("-")
    let row = document.getElementById(alertInfo[0])
    let descriptionCell = row.cells[5]
    let button = descriptionCell.getElementsByTagName("button")
    let myWindow = window.open("", "MyWindow", "");
    let alertDisplay = "Level: " +  row.cells[0].innerHTML + "<br>Time: " + row.cells[1].innerHTML	+ "<br>IP: " + row.cells[2].innerHTML + "<br>Port: " + row.cells[3].innerHTML +	"<br>Protocol: " + row.cells[4].innerHTML + "<br>Description: " + button[0].innerHTML
    myWindow.innerHTML = ""
    myWindow.document.write("<p>" + alertDisplay + "</p>");
    // Delete myWindow
    window.location.reload()
}
