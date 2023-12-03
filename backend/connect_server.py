import socketio

class LIDSSocketClient:
    def __init__(self, server_url, namespace):
        self.server_url = server_url
        self.namespace = namespace
        self.sio = socketio.Client()

    def start(self):
        self.sio.connect(self.server_url, namespaces=[self.namespace])
        print(f"Connected to {self.server_url} with namespace {self.namespace}")

    def send_alert_data(self, event, data):
        self.sio.emit(event, data, namespace=self.namespace)
        print(f"Sent event '{event}' with data: {data}")

    def stop(self):
        self.sio.disconnect()
        print("Disconnected from server")


if __name__ == "__main__":
    client = LIDSSocketClient('http://', '/lids-d')
    client.start()


    client.send_event('your_event', {'data': 'data'})


    client.stop()