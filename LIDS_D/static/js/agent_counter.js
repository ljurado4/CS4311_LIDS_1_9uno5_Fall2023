/* ######################################################################
   # File: agent_counter.js
   #
   # Version: [5.0]
   #
   # Description: This JavaScript file is responsible for creating a socket connection to a specific
   # namespace ('lids-d') and listening for the 'update_agent_count' event. When the event is received,
   # it updates the agent count displayed in the HTML document.
   #

   ###################################################################### */

// Author and modified Benjamin Hansen
// Function to create a socket connection
function createSocket() {
    // Construct the socket URL based on the current location
    var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
    var socket = io.connect(socketUrl + '/lids-d');

    // Listen for 'update_agent_count' event and update agent count in the document
    socket.on('update_agent_count', function(count) {
        console.log('Received agent count:', count);
        document.getElementById('agent_count').innerText = count;
    });
}
// Author and modified Benjamin Hansen
// Call the createSocket function when the window loads
window.onload = createSocket();
