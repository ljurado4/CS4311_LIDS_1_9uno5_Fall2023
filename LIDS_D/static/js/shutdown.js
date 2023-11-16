/*
   ######################################################################
   # File: shutdown.js
   #
   # Version: [5.0]
   #
   # Description: This JavaScript file contains a function to send a POST request to shut down the server in the LIDS-D application.
   #

   ######################################################################
*/
// Author and modified Benjamin Hansen
// Function to send a POST request to shut down the server
function shutdownServer() {
    fetch('/shutdown', {
        method: 'POST'
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
