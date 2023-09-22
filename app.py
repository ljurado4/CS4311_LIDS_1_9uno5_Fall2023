from flask import Flask, render_template

# Command  .\env\Scripts\activate.bat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('LIDS_Main.html')



if __name__ == "__main__":
    app.run(debug=True)