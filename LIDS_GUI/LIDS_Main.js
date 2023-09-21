const fileInput = document.getElementById('myFile');
fileInput.onchange = async () => {

  //get uploaded file
  const selectedFile = fileInput.files[0];
  let reader = new FileReader()
  reader.readAsText(selectedFile)
  //get everything from the file
  let loadedFile = ""
  //wait for the file to load
  await new Promise(resolve => reader.onload = () => resolve());
  loadedFile = reader.result
  let parser, xmlDoc;

  //xml parser
  parser = new DOMParser();
  xmlDoc = parser.parseFromString(loadedFile,"text/xml");

  let users = new Object()
 
  for(let i = 0;i < xmlDoc.getElementsByTagName("system").length;i++){
    let currUser = new Object()
    currUser["name"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("name")[0].childNodes[0].nodeValue
    currUser["ip"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("ip")[0].childNodes[0].nodeValue
    currUser["mac"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("mac")[0].childNodes[0].nodeValue
    currUser["ports"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("ports")[0].childNodes[0].nodeValue
    currUser["whitelist"] = xmlDoc.getElementsByTagName("system")[i].getElementsByTagName("whitelist")[0].childNodes[0].nodeValue
    users[i.toString()] = currUser 
    //needs work - tranferring data to the backend, change any code necessary
    //console.log(users)
    //comment line below to not change screen and stay in corruent page to print data
    window.location = "LIDS_Dashboard.html"
  }
}