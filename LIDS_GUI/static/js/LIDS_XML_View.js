/**
 * @Author Arturo Olmos
 */
let xmlConfigState = "<textarea class = \"xmlFileTextArea\">File Name: " + window.localStorage.getItem("xmlFileName") + "\n" + window.localStorage.getItem("xmlFile") + "</textarea>";
document.getElementById("middleContainer").innerHTML = "xmlConfigState"
middleContainer.innerHTML = xmlConfigState;
// Handles event when the user wants to see the config file
function viewXML(event){
    event.preventDefault();
    window.location = "LIDS_XML_View"
}

// Handles event when the user wants to see alerts displayed
function viewAlerts(event) {
    event.preventDefault();
    window.location = "LIDS_Dashboard"
};