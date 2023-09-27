from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Command  .\env\Scripts\activate.bat

app = Flask(__name__,template_folder='LIDS_GUI/templates',static_folder='LIDS_GUI/static')

CORS(app)

@app.route('/')
def index():
    return render_template('LIDS_Main.html')

@app.route('/LIDS_Dashboard')
def dashboard():
    alert_data =     [
    {
        "Time": "2023-09-16 12:01:23.456789",
        "Source": "192.168.1.2",
        "Destination": "192.168.1.100",
        "Protocol": "TCP",
        "Length": 64,
        "Description": "TCP Handshake SYN"
    },
    {
        "Time": "2023-09-16 12:01:23.456990",
        "Source": "192.168.1.100",
        "Destination": "192.168.1.2",
        "Protocol": "UDP",
        "Length": 64,
        "Description": "UDP Handshake SYN, ACK"
    },
    {
        "Time": "2023-09-16 12:02:00.000000",
        "Source": "192.168.1.3",
        "Destination": "192.168.1.101",
        "Protocol": "ICMP",
        "Length": 32,
        "Description": "Ping Request"
    },
    {
        "Time": "2023-09-16 12:02:00.100000",
        "Source": "192.168.1.101",
        "Destination": "192.168.1.3",
        "Protocol": "ICMP",
        "Length": 32,
        "Description": "Ping Reply"
    },
    {
        "Time": "2023-09-16 12:02:05.678910",
        "Source": "192.168.1.4",
        "Destination": "192.168.1.5",
        "Protocol": "TCP",
        "Length": 128,
        "Description": "HTTP GET Request"
    },
    {
        "Time": "2023-09-16 12:02:05.789123",
        "Source": "192.168.1.5",
        "Destination": "192.168.1.4",
        "Protocol": "TCP",
        "Length": 256,
        "Description": "HTTP 200 OK Response"
    }
]
    return render_template('LIDS_Dashboard.html',data_packet=alert_data)


@app.route('/LIDS_Main')
def lids_main(): 
    return render_template('LIDS_Main.html')


@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    data = request.json
    print("DATA",data)
 
    return jsonify({"message": "Data processed!"})

if __name__ == "__main__":
    app.run(debug=True)