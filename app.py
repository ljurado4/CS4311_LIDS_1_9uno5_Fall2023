from flask import Flask, render_template

# Command  .\env\Scripts\activate.bat

app = Flask(__name__,template_folder='LIDS_GUI/templates',static_folder='LIDS_GUI/static')

@app.route('/')
def index():
    return render_template('LIDS_Main.html')

@app.route('/LIDS_Dashboard')
def dashboard():
    return render_template('LIDS_Dashboard.html')


@app.route('/LIDS_Main')
def lids_main():
    return render_template('LIDS_Main.html')


if __name__ == "__main__":
    app.run(debug=True)