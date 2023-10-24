#app.py
from flask import Flask, render_template, request, jsonify, flash
from backend import lids_agent_connector
from flask_cors import CORS
from backend import packets,alerts_manager
import threading
import logging
import socketio
import secrets



app = Flask(__name__, template_folder='LIDS_GUI/templates', static_folder='LIDS_GUI/static')

pack_time = packets.PackTime()
thread = threading.Thread(target=pack_time.run_sniffer)
thread.start()


CORS(app)
app.secret_key = secrets.token_urlsafe(16)

sio = socketio.Client()

@app.route('/')
def index():
    return render_template('LIDS_Main.html')


    
    
    
@app.route('/LIDS_Dashboard', methods=['GET', 'POST'])
def dashboard():
    global client_socket
    global alert_data
    if request.method == 'POST':
        logging.debug("POST request received")
        ip_address = request.form.get('IPInput')
        port_number = request.form.get('PortInput')
        print("ip_address",ip_address)
        print("port_number",port_number)
        logging.debug("Attempting to establish socket connection")

        try:
            
            sio.connect(f'http://{ip_address}:{port_number}')
            flash(f'Successfully connection to server at IP: {ip_address} Port: {port_number}.', 'success')
        except Exception as e:
            flash(f'Failed connection server at IP: {ip_address} Port: {port_number}.', 'error')

        
    return render_template('LIDS_Dashboard.html')


@app.route('/get_alerts', methods=['GET'])
def get_latest_alerts():
    getter = alerts_manager.AlertManager().sharedAlerts

    alert_data = [
        {
            'Time': alert.time,
            'Identifier': alert.identifier,
            'Level': alert.level,
            'SourceIP': alert.sourceIP,
            'SourcePort': alert.sourcePort,
            'DestIP': alert.destIP,
            'DestPort': alert.destPort,
            'TypeAlert': alert.typeAlert,
            'Description': alert.description,
        }
        for alert in getter
    ]
    # for alert in getter:
    #     print("alert",alert)
    if sio.connected:
        sio.emit("Alert Data",alert_data)
    return jsonify(alert_data)



@app.route('/LIDS_Main')
def lids_main(): 
    return render_template('LIDS_Main.html')

@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    data = request.json

    return jsonify({"message": "Data processed!"})



@app.route('/disconnect', methods=['POST'])
def disconnect():
    print("Disconnecting from server")
    global sio
    sio.disconnect()
    return render_template('LIDS_Main.html')


if __name__ == "__main__":
    app.run(debug=True)
