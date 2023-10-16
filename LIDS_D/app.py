#app.py

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app, resources={r"/*": {"origins": "*"}})

configuration = {}
connected_agents = -1
start_server = False
device_connected = []
alert_data = []


@socketio.on('Alert Data')
def handle_response(alert):
    global alert_data
    alert_data.append(alert)


@app.route('/update_alert_data_table', methods=['GET'])
def update_alert_table():
    global alert_data
    flattened_data = [alert for sublist in alert_data for alert in sublist]

    return jsonify(flattened_data)


@app.route('/sort_alerts', methods=['GET'])
def sort_alerts():
    global alert_data
    sort_by = request.args.get('sort_by', default="none", type=str)
    
    flattened_data = [alert for sublist in alert_data for alert in sublist]
    
    if sort_by == "lvl":
        flattened_data.sort(key=lambda x: x.get('level', 0))
    elif sort_by == "time":
        flattened_data.sort(key=lambda x: x.get('time', 0))
    elif sort_by == "ip":
        flattened_data.sort(key=lambda x: x.get('ip', ''))
    
    return jsonify(flattened_data)


@socketio.on('request_data')
def send_device_connected_data():
    global device_connected
    socketio.emit('update_data', device_connected)


@app.route('/')
def index():
    return render_template('LIDS-D_Config_server_View.html')


@app.route('/LIDS-D_Config_Server_View')
def config_server():
    return render_template('LIDS-D_Config_server_View.html')


@app.route('/start_server_ui')
def start_server_interface():
    return render_template('LIDS-D_Start_Server.html')


@app.route('/start_socket_server', methods=['POST'])
def start_socket_server_action():
    global start_server
    start_server = True
    return jsonify({"message": "Server started"})


@app.route('/LIDS-D_Server_Details')
def server_details():
    return render_template('LIDS-D_Server_Details.html')


@app.route('/LIDS-D_Network_Info_View')
def network_info_view():
    global device_connected
    print("On LIDS-D_Network")
    print("device_connected", device_connected)
    return render_template('LIDS-D_Network_Info_View.html', clients=device_connected)


@app.route('/LIDS-D_Alerts_View')
def alerts_view():
    return render_template('LIDS-D_Alerts_View.html')


@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    global configuration
    configuration = request.json
    print(configuration)

    return "Data Processed"


@socketio.on('connect')
def handle_connect():
    global connected_agents
    global device_connected
    global start_server
    
    if not start_server:
        return False

    is_ip_whitelisted = False
    client_ip = request.remote_addr
    print("Attempting to connect", client_ip)
    for k, dic in configuration.items():
        white_lst = dic['whitelist']
        if client_ip in white_lst:
            print("Found IP")
            is_ip_whitelisted = True  
    
    if not is_ip_whitelisted:
        return False
    
    connected_agents += 1
    print(f'Client {client_ip} connected')
    print(f'Agents connected {connected_agents}')
    device_connected.append({
        "id": str(len(device_connected) + 1),
        "name": f"Client {len(device_connected) + 1}",
        "ip": client_ip,
        "status": "connected"
    })
    
    socketio.emit('update_agent_count', connected_agents)
    socketio.emit('update_data', device_connected)


@socketio.on('disconnect')
def handle_disconnect():
    print("Disconnecting")
    global device_connected
    global connected_agents
    
    client_ip = request.remote_addr
    device_connected = [client for client in device_connected if client['ip'] != client_ip]

    connected_agents -= 1

    socketio.emit('update_agent_count', connected_agents)
    socketio.emit('update_data', device_connected)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
