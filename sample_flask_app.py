from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/echo/<name>', methods=['GET'])
def echo(name):
    return jsonify({'name': name})

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/hello', methods=['GET'])
def world():
    return 'Hello World - but from different route!'

if __name__ == '__main__':
    app.run()