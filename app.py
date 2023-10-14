from flask import Flask, render_template, request, jsonify
from backend import lids_agent_connector
from flask_cors import CORS
from CLI.packets import PackTime
import pyshark

# Command  .\env\Scripts\activate.bat

app = Flask(__name__,template_folder='LIDS_GUI/templates',static_folder='LIDS_GUI/static')

CORS(app)

@app.route('/')
def index():
    return render_template('LIDS_Main.html')

@app.route('/LIDS_Dashboard')
def dashboard():
    print("before threads")
    #Ideally, gets the packet list to be displayed
    #TODO: Confirm if we want packets or alerts
        #PackTime.packet_list
    
    packet_manager = PackTime()
    packet_manager.thread1.start()
    packet_manager.thread2.start()

    print("after threads")
    pkt_list = packet_manager.export_packets()
    print(pkt_list)
    #TODO: Make the list from packets work here
    """
    alert_data = pkt_list
    [
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
    """
                                                #data_packet=alert_data
    return render_template('LIDS_Dashboard.html',data_packet=pkt_list)


@app.route('/LIDS_Main')
def lids_main(): 
    return render_template('LIDS_Main.html')


@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    data = request.json
    print(data)
    # connect_agent = lids_agent_connector.AgentConnector(data)
    
    return jsonify({"message": "Data processed!"})


if __name__ == "__main__":
    app.run(debug=True)