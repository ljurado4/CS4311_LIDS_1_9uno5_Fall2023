##################################################################
# File: app.py
#
# Version: [5.0]
#
# Description:
# This script serves as the core application server for a Flask-based
# web interface of a Local Intrusion Detection System (LIDS). It manages
# web routes, handles interactions with the backend for packet sniffing,
# provides a dashboard for real-time alerts, and allows configuration through
# a web GUI. The server also integrates with socket.io for live data streaming.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Set up the Flask application and configure cross-origin resource sharing (CORS).
# - [Task 2]: Initialize the packet sniffer in a separate thread.
# - [Task 3]: Define routes for the main index and dashboard, and handle their logic.
# - [Task 4]: Create a route to retrieve and send the latest alerts via socket.io.
# - [Task 5]: Implement a route for handling configuration data upload.
# - [Task 6]: Establish a route to handle the disconnection logic.
# - [Task 7]: Ensure proper error handling and user feedback 'through flash messages.
# - [Task 8]: Start the Flask server with the necessary debug configuration.
# - [Task 9]: Maintain the server code with logging for debug purposes.
#
##################################################################

import os
from flask import Flask, render_template, request, jsonify, flash
from flask_cors import CORS
from backend import packets,alerts_manager, ipChecker
import threading
import logging
import socketio
import secrets
from config_condition import config_condition



app = Flask(__name__, template_folder='LIDS_GUI/templates', static_folder='LIDS_GUI/static')

pack_time = packets.PackTime()
thread = threading.Thread(target=pack_time.run_sniffer)
thread.start()


CORS(app)
app.secret_key = secrets.token_urlsafe(16)

sio = socketio.Client(ssl_verify=False)


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
            
            sio.connect(f'https://{ip_address}:{port_number}')
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
    with config_condition:
        ipChecker.ip_Checker.configuration = data
        config_condition.notify_all()
   
    # print("config.configuration",config.configuration )
    return jsonify({"message": "Data processed!"})



@app.route('/disconnect', methods=['POST'])
def disconnect():
    print("Disconnecting from server")
    global sio
    sio.disconnect()
    return render_template('LIDS_Main.html')


if __name__ == "__main__":
    app.run(debug=True)
