//config.js

let browseButton = document.getElementById("browseButton")

//if new local storage create object to save files
if (window.localStorage.getItem("files") == null){

    window.localStorage.setItem("files",JSON.stringify(new Object()))
}
//note save objects as strings for storage and later use
const filesAsString = window.localStorage.getItem("files")
const files = JSON.parse(filesAsString)

const previousFilesContainer = document.getElementById("previousFilesSelection")
//skeleton for function
//file contents is a string of the xml
function oldFileConfig(fileName){
    //needs function to set up old config
    window.location = "LIDS-D_Start_Server.html"
}

//create button for each of the previous files stored
for(let fileName in files){
    let fileButton = "<button class = \"prevFileButton\" value = \"" + fileName + "\" onclick = \"oldFileConfig(value)\">"
    fileButton += "<img style = \"height:20vh\" src= fileImage.jpg ></img>"
    fileButton += "<p style = \"width:100%;text-align:center;\">" + fileName +"</p>"
    fileButton += "</button>"
    previousFilesContainer.innerHTML += fileButton
}

function succesfulFileSubmition(selectedFile,loadedFile){
  //store new file uploaded to storage
  files[selectedFile.name] = loadedFile
  //store as JSON string in local storage
  window.localStorage.setItem("files",JSON.stringify(files))
  let parser, xmlDoc;

  //xml parser
  parser = new DOMParser();
  xmlDoc = parser.parseFromString(loadedFile,"text/xml");

  let users = new Object()
  //save data in an object
  for(let i = 0;i < xmlDoc.getElementsByTagName("system").length;i++){
    let currUser = new Object()
    currUser["name"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("name")[0].childNodes[0].nodeValue
    currUser["ip"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("ip")[0].childNodes[0].nodeValue
    currUser["mac"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("mac")[0].childNodes[0].nodeValue
    currUser["ports"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("ports")[0].childNodes[0].nodeValue
    currUser["whitelist"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("whitelist")[0].childNodes[0].nodeValue
    users[i.toString()] = currUser 
    
  }
    // Sends data to back-end 
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
    
    
    // needs work - tranferring data to the backend, change any code necessary
    console.log(users)
    // comment line below to not change screen and stay in corruent page to print data
    //store file name and contents to use in next page
    window.localStorage.setItem("xmlFileName",selectedFile.name)
    window.localStorage.setItem("xmlFile",loadedFile)

    window.location = "start_server_ui"

  })
  .catch(error => {
      console.error('Error:', error);
  });
  window.location = "start_server_ui"
}

//this will only be done when a user inputs file
browseButton.onchange = async () => {
  //get uploaded file
  const selectedFile = browseButton.files[0];
  let reader = new FileReader()
  reader.readAsText(selectedFile)
  //get everything from the file
  let loadedFile = ""
  //wait for the file to load
  await new Promise(resolve => reader.onload = () => resolve());
  loadedFile = reader.result
  //check if file exists
  if(files[selectedFile.name] != null){
  //if file exists ask user if they want to replace
    if (confirm(selectedFile.name + " already exists, would you like to replace?")) {
      txt = "The file has been updated";
      succesfulFileSubmition(selectedFile,loadedFile)
    } else {
      txt = "Upload canceled";
      window.location = "LIDS-D_Config_Server_View"
    }
  }else{
    //case if new file name
    succesfulFileSubmition(selectedFile,loadedFile)
  }
}