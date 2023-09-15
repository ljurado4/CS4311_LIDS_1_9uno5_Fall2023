//get forms
const configFileForm = document.querySelector("#configFileForm")
const middleBlockForm = document.querySelector("#middleBlockDisplayForm")
const disconnectForm = document.querySelector("#disconnectButtonForm")
//handles event when user wants to see config file in middle block of gui
configFileForm.addEventListener("submit",(event)=>{
    event.preventDefault()
    console.log("Hello1")
    //get uplloaded file
    const fileUploaded = sessionStorage.getItem("XMLFILE")
    console.log(fileUploaded)
    var middleBlock = document.getElementById("middleBlock")
    middleBlock.src = fileUploaded
})
//handles event when user wants to see intrusions displayed
middleBlockForm.addEventListener("submit",(event)=>{
    event.preventDefault()
    console.log("Hello2")
})
//hadles the disconnection of the device
disconnectForm.addEventListener("submit",(event)=>{
    event.preventDefault()
    window.location = "LIDS_Main.html"
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

function removeSort() {
    location.reload();
}