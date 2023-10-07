from flask import Flask, render_template



app = Flask(__name__,template_folder='LIDS_D/templates',static_folder='LIDS_D/static')

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True,port=5001)
