# File: app.py
#
# Description: This script serves as the core application server for a Flask-based web interface of a Local Intrusion Detection System (LIDS). It manages web routes, handles interactions with the backend for packet sniffing, provides a dashboard for real-time alerts, and allows configuration through a web GUI. The server also integrates with socket.io for live data streaming.
# 
#  @ Author: Benjamin Hansen
#  @ Modified: Lizbeth Jurado

import os
import csv
from flask import Flask, render_template, request, jsonify, flash
from flask_cors import CORS
from backend import packets,alerts_manager, ipChecker
import threading
import logging
import socketio
import secrets
import pyshark
from config_condition import config_condition
from flask import send_file, abort
from backend.Alerts import Alerts
from flask import jsonify
from backend.packet_analyzer import PacketAnalyzer


basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(basedir, 'LIDS_GUI', 'templates')
static_dir = os.path.join(basedir, 'LIDS_GUI', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

pack_time = packets.PackTime()
thread = threading.Thread(target=pack_time.run_sniffer)
thread.start()


CORS(app)
app.secret_key = secrets.token_urlsafe(16)

sio = socketio.Client(ssl_verify=False)

#  @ Author: Benjamin Hansen
#  @ Modified: Benjamin Hansen
@app.route('/')
def index():
    return render_template('LIDS_Main.html')


    
    
#  @ Author: Benjamin Hansen
#  @ Modified: Benjamin Hansen 
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
            error_message = str(e)
            logging.error(f'Failed to connect to server at IP: {ip_address} Port: {port_number}. Error: {error_message}')
            flash(f'Failed to connect to server at IP: {ip_address} Port: {port_number}. Error: {error_message}', 'error')

        
    return render_template('LIDS_Dashboard.html')

#  @ Author: Benjamin Hansen
#  @ Modified: Benjamin Hansen
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


#  @ Author: Benjamin Hansen
#  @ Modified: Benjamin Hansen
@app.route('/LIDS_Main')
def lids_main(): 
    return render_template('LIDS_Main.html')

#  @ Author: Benjamin Hansen
#  @ Modified: Benjamin Hansen
@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    data = request.json
    with config_condition:
        ipChecker.ip_Checker.configuration = data
        config_condition.notify_all()
   
    # print("config.configuration",config.configuration )
    return jsonify({"message": "Data processed!"})


#  @ Author: Benjamin Hansen
#  @ Modified: Benjamin Hansen
@app.route('/disconnect', methods=['POST'])
def disconnect():
    print("Disconnecting from server")
    global sio
    sio.disconnect()
    return render_template('LIDS_Main.html')


# @ Author: Lizbeth Jurado 
# Created to handle pcap data
@app.route('/display_pcap')
def display_pcap():
    pcap_path = Alerts.get_pcap_file_path()
    try:
        return send_file(pcap_path, as_attachment=True)
    except FileNotFoundError:
        abort(404)  # File not found
        
# @ Author: Lizbeth Jurado 
@app.route('/get_pcap_data')
def get_pcap_data():
    analyzer = PacketAnalyzer()
    pcap_data = analyzer.read_pcap() 
    formatted_data = analyzer.format_for_frontend(pcap_data)
    return jsonify(formatted_data)

# @ Author: Lizbeth Jurado Showing filtered alerts on a new page
@app.route('/filtered_alerts', methods=['GET', 'POST'])
def filtered_alerts():
    if request.method == 'POST':
        level = request.form.get('level')
        filtered_alerts = [alert for alert in alerts_manager.AlertManager().sharedAlerts if alert.level == level]
        session['filtered_alerts'] = [alert.to_dict() for alert in filtered_alerts]  # Convert to dict for serialization
        return render_template('filtered_alerts.html', alerts=filtered_alerts)
    else:
        # If it's a GET request, just display the page with filtering options
        return render_template('filter_alerts.html')  

# @ Author: Lizbeth Jurado New route for exporting filtered alerts
@app.route('/export_filtered_alerts', methods=['POST'])
def export_filtered_alerts():
    # Get the filtered alerts from the session or recreate them from the form submission
    filtered_alerts_dicts = session.get('filtered_alerts', [])
    # Define the path for the new CSV file
    csv_file_path = os.path.join(basedir, 'static', 'exports', 'filtered_alerts.csv')
    
    # Check if we have any alerts to export
    if not filtered_alerts_dicts:
        flash('No alerts to export.', 'warning')
        return redirect(url_for('dashboard'))
    
    fieldnames = ['time', 'identifier', 'level', 'sourceIP', 'sourcePort', 'destIP', 'destPort', 'typeAlert', 'description']
    
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for alert_dict in filtered_alerts_dicts:
            writer.writerow(alert_dict)
    
    return send_file(csv_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
