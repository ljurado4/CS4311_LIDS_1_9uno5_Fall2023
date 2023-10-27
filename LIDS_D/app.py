from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app, resources={r"/*": {"origins": "*"}})

configuration = {}
connected_agents = 0
start_server = False
recognized_device_connected = []
unrecognized_device_connected = []
alert_data = []


@socketio.on('Alert Data')
def handle_response(alert):
    global alert_data
    alert_data.append(alert)
    socketio.emit('new_alert_data', alert, namespace='/lids-d')




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

    print("On LIDS-D_Network")
  
    return render_template('LIDS-D_Network_Info_View.html')


@app.route('/LIDS-D_Alerts_View')
def alerts_view():
    return render_template('LIDS-D_Alerts_View.html')


@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    global configuration
    configuration = request.json
    # print(configuration)

    return "Data Processed"



@socketio.on('connect', namespace='/lids-d')
def lids_client_namespace_connect():
    global connected_agents
    global recognized_device_connected, unrecognized_device_connected
    
    print("LIDS-D socket connection")
    
    devices = {
        'recognized_devices': recognized_device_connected,
        'unrecognized_devices': unrecognized_device_connected
    }
    socketio.emit('update_agent_count', connected_agents, namespace='/lids-d')
    socketio.emit('update_devices', devices, namespace='/lids-d')

    return True


@socketio.on('connect')
def handle_LIDS_connect():
    global connected_agents 
    global start_server
    global recognized_device_connected, unrecognized_device_connected
    
    if not start_server:
        return False

    is_ip_whitelisted  = False
    
    client_ip = request.remote_addr
    print("Attempting to connect", client_ip)
    
    for k, dic in configuration.items():
        
        white_lst = dic['whitelist']
        
        if client_ip in white_lst:
            is_ip_whitelisted  = True
            recognized_device_connected.append({
                "id": str(len(recognized_device_connected) + 1),
                "name": dic["name"],
                "ip": client_ip,
                "status": "connected"
            })
            break
    
    client_protocol = request.environ.get('REMOTE_PORT')
    if not is_ip_whitelisted:
        unrecognized_device_connected.append({
                "ip": request.remote_addr,
                "port": "NA" if not client_protocol else client_protocol,
                "protocol": request.environ.get('HTTP_UPGRADE', 'http')
                
            })
                
    connected_agents += 1
    print(f'Client {client_ip} connected')
    print(f'Agents connected {connected_agents}')

    
    devices = {
        'recognized_devices': recognized_device_connected,
        'unrecognized_devices': unrecognized_device_connected
    }
    print("devices",devices)
    socketio.emit('update_agent_count', connected_agents, namespace='/lids-d')
    socketio.emit('update_devices', devices, namespace='/lids-d')
    
    
    return True


@socketio.on('disconnect')
def handle_disconnect():
    print("Disconnecting")
    global recognized_device_connected, unrecognized_device_connected
    global connected_agents
    
    client_ip = request.remote_addr
    
    recognized_device_connected = [client for client in recognized_device_connected if client['ip'] != client_ip]

    unrecognized_device_connected = [client for client in unrecognized_device_connected if client['ip'] != client_ip]

    connected_agents -= 1
    
    
    
    devices = {
        'recognized_devices': recognized_device_connected,
        'unrecognized_devices': unrecognized_device_connected
    }
    print("devices",devices)
    socketio.emit('update_agent_count', connected_agents, namespace='/lids-d')
    socketio.emit('update_devices', devices, namespace='/lids-d')
    


@app.route('/shutdown', methods=['POST'])
def shutdown():
    global start_server, configuration ,connected_agents
    global recognized_device_connected, unrecognized_device_connected
    global alert_data
    
    configuration = {}
    connected_agents = 0
    start_server = False
    recognized_device_connected = []
    unrecognized_device_connected = []
    alert_data = []
    start_server = False 

    print("shutting down")
    return render_template('LIDS-D_Config_server_View.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
