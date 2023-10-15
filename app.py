#app.py
from flask import Flask, render_template, request, jsonify
from backend import lids_agent_connector
from flask_cors import CORS
from backend import packets,alerts_manager
import threading


app = Flask(__name__, template_folder='LIDS_GUI/templates', static_folder='LIDS_GUI/static')

pack_time = packets.PackTime()
thread = threading.Thread(target=pack_time.run_sniffer)
thread.start()


CORS(app)


@app.route('/')
def index():
    return render_template('LIDS_Main.html')

@app.route('/get_alerts', methods=['GET'])
def get_latest_alerts():
    getter = alerts_manager.AlertManager().sharedAlerts
    # print("inside get_latest_alerts")
    # print("getter",getter)
    alert_data = [
        {
            'Time': alert.time,
            'Source': alert.IP,
            'Port': alert.Port,
            'Description': alert.description,
            'Level': alert.level
        }
        for alert in getter
    ]
    return jsonify(alert_data)


@app.route('/LIDS_Dashboard')
def dashboard():
    return render_template('LIDS_Dashboard.html')
    
@app.route('/LIDS_Main')
def lids_main(): 
    return render_template('LIDS_Main.html')

@app.route('/configuration_data', methods=['POST'])
def upload_xml_data():
    data = request.json
    # For future connection purposes
    # connect_agent = lids_agent_connector.AgentConnector(data)
    
    return jsonify({"message": "Data processed!"})

if __name__ == "__main__":
    app.run(debug=True)
