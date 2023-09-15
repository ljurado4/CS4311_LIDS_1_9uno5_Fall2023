const fileInput = document.getElementById('myFile');
fileInput.onchange = () => {
  const selectedFile = fileInput.files[0];
  sessionStorage.setItem("XMLFILE",selectedFile)
  window.location = "LIDS_Dashboard.html"
}