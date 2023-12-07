import socketio
import time
# @ Author: Benjamin Hansen
class LIDSSocketClient:
    
    """
    A client class for connecting to a server via Socket.IO.
    """

    # @ Author: Benjamin Hansen
    def __init__(self, server_url):
        """
        Initialize the client with the given server URL.
        
        Args:
        server_url (str): The URL of the server to connect to.
        """
        self.server_url = server_url
        self.sio = socketio.Client(ssl_verify=False)
        self.connected_server = False
# @ Author: Benjamin Hansen
    def start(self):
        """
        Connects to the server and sets the connection status.
        """


        try:
            self.sio.connect(self.server_url)
            print(f"Connected to {self.server_url}")
            self.connected_server = True
        except Exception as e:
            error_message = str(e)
            print(f'Failed to connect to server {error_message}')

# @ Author: Benjamin Hansen
    def send_alert_data(self,alerts_data):
        """
        Sends alert data to the server.

        Args:
        alerts_data: Data to be sent as an alert.
        """
        if not self.connected_server:
            print("Cannot send alert data: Agent is not connected to LIDS-D")
            return
        self.sio.emit("Alert Data", alerts_data)
        print(f"Sent event Alert Data with data: {alerts_data}")
# @ Author: Benjamin Hansen
    def stop(self):
        """
        Disconnects from the server.
        """
        self.sio.disconnect()
        print("Disconnected from server")

# @ Author: Benjamin Hansen
if __name__ == "__main__":
    # Example usage of the LIDSSocketClient
    client = LIDSSocketClient('https://192.168.1.136:5001')
    client.start()

    if client.connected_server:

        client.send_alert_data("CLI")
        time.sleep(10)
        client.stop()
        