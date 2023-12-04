import socketio

class LIDSSocketClient:
    def __init__(self, server_url, namespace):
        self.server_url = server_url
        self.sio = socketio.Client()

    def start(self):
        try:
            
            self.sio.connect(self.server_url)
            print(f"Connected to {self.server_url}")
        except Exception as e:
            error_message = str(e)
            print("Failed to connect to server")

    def send_alert_data(self, event, data):
        self.sio.emit(event, data, namespace=self.namespace)
        print(f"Sent event '{event}' with data: {data}")

    def stop(self):
        self.sio.disconnect()
        print("Disconnected from server")


if __name__ == "__main__":
    client = LIDSSocketClient('http://')
    client.start()


    


    client.stop()