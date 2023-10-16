function createSocket() {
    var socketUrl = window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port : '');
    var socket = io.connect(socketUrl);


    socket.on('update_agent_count', function(count) {
        console.log('Received agent count:', count);
        document.getElementById('agent_count').innerText = count;
    });
}



window.onload = createSocket()


