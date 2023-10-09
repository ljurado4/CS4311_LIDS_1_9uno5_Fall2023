from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)

configuration = {}
connected_agents = 0

@app.route('/')
def index():
    return render_template('LIDS-D_Config_server_View.html')


@app.route('/LIDS-D_Config_Server_View')
def config_server():
    return render_template('LIDS-D_Config_server_View.html')

@app.route('/LIDS-D_Start_Server')
def start_server():
    return render_template('LIDS-D_Start_Server.html')

@app.route('/LIDS-D_Server_Details')
def server_details():
    return render_template('LIDS-D_Server_Details.html')

@app.route('/LIDS-D_Network_Info_View')
def network_info_view():
    return render_template('LIDS-D_Network_Info_View.html') 

@app.route('/LIDS-D_Alerts_View')
def alerts_view():
    return render_template('LIDS-D_Alerts_View.html')



@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    global configuration
    configuration = request.json
    print(configuration)
    
    return jsonify({"Data processed"})

@socketio.on('connect')
def handle_connect():
    global connected_agents
    is_ip_whitelisted = False
    client_ip = request.remote_addr
    print("Attempting to connect",client_ip)
    for k,dic in configuration.items():
        white_lst = dic['whitelist']
        if client_ip in white_lst:
            print("Found IP")
            is_ip_whitelisted = True  
    
    if not is_ip_whitelisted:
        return False
    
    connected_agents += 1
    print(f'Client {client_ip} connected')
    socketio.emit('update_agent_count', connected_agents)

@socketio.on('disconnect')
def handle_disconnect():
    global connected_agents

    connected_agents -= 1

    socketio.emit('update_agent_count', connected_agents)


if __name__ == '__main__':
    app.run(debug=True,port=5001)
