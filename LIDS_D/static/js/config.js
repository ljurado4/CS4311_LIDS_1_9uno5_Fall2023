/*
   ######################################################################
   # File: config.js
   #
   # Version: [5.0]
   #
   # Description: This JavaScript file handles file uploading, storage, and configuration data submission. 
   #

   ######################################################################
*/
let browseButton = document.getElementById("browseButton");

// Check if new local storage exists, create an object to save files
if (window.localStorage.getItem("files") == null) {
    window.localStorage.setItem("files", JSON.stringify(new Object()));
}

// Note: Save objects as strings for storage and later use
const filesAsString = window.localStorage.getItem("files");
const files = JSON.parse(filesAsString);

const previousFilesContainer = document.getElementById("previousFilesSelection");

/* @author Arturo Olmos */
// Function to handle loading old configuration file
function oldFileConfig(fileName) {
    // Implement a function to set up the old configuration
    window.location = "LIDS-D_Start_Server.html";
}

// Create a button for each of the previous files stored
for (let fileName in files) {
    let fileButton = "<button class=\"prevFileButton\" value=\"" + fileName + "\" onclick=\"oldFileConfig(value)\">";
    fileButton += "<img style=\"height:20vh\" src=\"../img/fileImage.jpg\"></img>";
    fileButton += "<p style=\"width:100%;text-align:center;\">" + fileName + "</p>";
    fileButton += "</button>";
    previousFilesContainer.innerHTML += fileButton;
}

/* @author Arturo Olmos */
// Function to handle successful file submission
function successfulFileSubmission(selectedFile, loadedFile) {
    // Store the new file uploaded to storage
    files[selectedFile.name] = loadedFile;
    // Store as a JSON string in local storage
    window.localStorage.setItem("files", JSON.stringify(files));
    
    let parser, xmlDoc;

    // XML parser
    parser = new DOMParser();
    xmlDoc = parser.parseFromString(loadedFile, "text/xml");

    let users = new Object();
    
    // Save data in an object
    for (let i = 0; i < xmlDoc.getElementsByTagName("system").length; i++) {
        let currUser = new Object();
        currUser["name"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("name")[0].childNodes[0].nodeValue;
        currUser["ip"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("ip")[0].childNodes[0].nodeValue;
        currUser["mac"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("mac")[0].childNodes[0].nodeValue;
        currUser["ports"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("ports")[0].childNodes[0].nodeValue;
        currUser["whitelist"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("whitelist")[0].childNodes[0].nodeValue;
        users[i.toString()] = currUser;
    }
    
    // Sends data to the back-end
    fetch('configuration_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(users)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        // Needs work - transferring data to the backend, change any necessary code
        console.log(users);
        // Comment out the line below to not change the screen and stay on the current page to print data
        // Store file name and contents to use on the next page
        window.localStorage.setItem("xmlFileName", selectedFile.name);
        window.localStorage.setItem("xmlFile", loadedFile);
        window.location = "start_server_ui";
    })
    .catch(error => {
        console.error('Error:', error);
    });
    window.location = "start_server_ui";
}

/* @author Arturo Olmos */
// This will only be executed when a user uploads a file
browseButton.onchange = async () => {
    // Get the uploaded file
    const selectedFile = browseButton.files[0];
    let reader = new FileReader();
    reader.readAsText(selectedFile);
    
    // Get everything from the file
    let loadedFile = "";
    
    // Wait for the file to load
    await new Promise(resolve => reader.onload = () => resolve());
    loadedFile = reader.result;
    
    // Check if the file exists
    if (files[selectedFile.name] != null) {
        // If the file exists, ask the user if they want to replace it
        if (confirm(selectedFile.name + " already exists, would you like to replace it?")) {
            txt = "The file has been updated";
            successfulFileSubmission(selectedFile, loadedFile);
        } else {
            txt = "Upload canceled";
            window.location = "LIDS-D_Config_Server_View";
        }
    } else {
        // Case for a new file name
        successfulFileSubmission(selectedFile, loadedFile);
    }
};
