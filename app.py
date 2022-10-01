import os
from flask import  Flask
from flask_cors import CORS
from routes.animes import animes
app  =Flask(__name__)

envmode = os.environ['envmode'] 
@app.route('/')
def index():
    return "si"

CORS(app)   

app.register_blueprint(animes)
if __name__ == '__main__':
    if envmode == 'prod':
        app.run(ssl_context="adhoc", host='0.0.0.0', port=80)
    app.run(debug=True, port=5000)