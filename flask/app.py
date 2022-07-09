# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Currency rates viewer: Hello World!</h1>'


app.run(debug=True, host='0.0.0.0')