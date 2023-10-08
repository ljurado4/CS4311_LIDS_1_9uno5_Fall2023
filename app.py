#app.py
from flask import Flask, render_template, request, jsonify
from backend.db import db, migrate
from backend import lids_agent_connector
from flask_cors import CORS

app = Flask(__name__, template_folder='LIDS_GUI/templates', static_folder='LIDS_GUI/static')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lids.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def index():
    return render_template('LIDS_Main.html')

@app.route('/LIDS_Dashboard')
def dashboard():
    alert_data = [
        {
            "Time": "2023-09-16 12:01:23.456789",
            "Source": "192.168.1.2",
            "Destination": "192.168.1.100",
            "Protocol": "TCP",
            "Length": 64,
            "Description": "TCP Handshake SYN"
        },
        # ... [Other alerts here] ...
    ]
    return render_template('LIDS_Dashboard.html', data_packet=alert_data)

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
