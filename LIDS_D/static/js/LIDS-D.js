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

   ######################################################################
*/

// Counter used to keep track of malicious packets
let maliciousPacketCount = 0

// Adding initial HTML to display malicious packets found
document.getElementById("mpd").innerHTML = "Malicious Packet Count:\n" + maliciousPacketCount.toString()

// Author Arturo Olmos and modified Benjamin Hansen
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
    let alertsToText = ""
    var table = document.getElementById("alertsTable");
    console.log(fileType.value)
    if(fileType.value == "csv"){
      alertsToText  += "Time,Identifier,Level,SourceIP,SourcePort,DestIP,DestPort,Description\n"
      for (var i = 0, row; row = table.rows[i]; i++) {
        console.log("hhhh")
      //iterate through rows
      //rows would be accessed using the "row" variable assigned in the for loop
        let rowContent = ""
        rowContent += row.cells[0].innerHTML + ","  + row.cells[1].innerHTML + "," + row.cells[2].innerHTML + "," + row.cells[3].innerHTML + "," +row.cells[4].innerHTML + "," +row.cells[5].innerHTML + "," +row.cells[6].innerHTML + "," + row.cells[7].getElementsByTagName("button")[0].innerHTML
        alertsToText += rowContent + "\n"
      }
      console.log(alertsToText)
    }else if(fileType.value == "json"){
      for (var i = 0, row; row = table.rows[i]; i++) {
       
        //iterate through rows
        //rows would be accessed using the "row" variable assigned in the for loop

        let jsonObject = {
          "Time":row.cells[0].innerHTML,
          "Identifier":row.cells[1].innerHTML,
          "Level":row.cells[2].innerHTML,
          "SourceIP":row.cells[3].innerHTML,
          "SourcePort":row.cells[4].innerHTML,
          "DestIP":row.cells[5].innerHTML,
          "DestPort":row.cells[6].innerHTML,
          "Description":row.cells[7].getElementsByTagName("button")[0].innerHTML,
        }
        alertsToText += JSON.stringify(jsonObject) + "\n"
      }
    }else if(fileType.value == "xml"){//xml export
      alertsToText = "<?xml version=\"1.0\"?>\n"
      alertsToText += "<Alerts>\n"
      for (var i = 0, row; row = table.rows[i]; i++) {

        //iterate through rows
        //rows would be accessed using the "row" variable assigned in the for loop
        alertsToText += "  <Alert " + i.toString() + ">\n"
        alertsToText += "    <Time>" + row.cells[0].innerHTML + "</Time>\n"
        alertsToText += "    <Identifier>" + row.cells[1].innerHTML + "</Identifier>\n"
        alertsToText += "    <Level>" + row.cells[2].innerHTML + "</Level>\n"
        alertsToText += "    <SourceIP>" + row.cells[3].innerHTML + "</SourceIP>\n"
        alertsToText += "    <SourcePort>" + row.cells[4].innerHTML + "/<SourcePort>\n"
        alertsToText += "    <DestIP>" + row.cells[5].innerHTML + "/<DestIP>\n"
        alertsToText += "    <DestPort>" + row.cells[6].innerHTML + "/<DestPort>\n"
        alertsToText += "    <Description>" + row.cells[7].getElementsByTagName("button")[0].innerHTML + "/<Description>\n"
        alertsToText += "  </Alert " + i.toString() + ">\n"
      }
      alertsToText += "</Alerts>\n"
    }
    //create file object with desired file contents and extension type
    file = new File([alertsToText], exportAlertsFileName, {
      type: 'text/' + fileType.value,
    })
    //function used to download alert locally
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
