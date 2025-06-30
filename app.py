from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'yo yo yo, the server is up and running'

@app.route('/health')
def health():
    return 'Server is up and running'
