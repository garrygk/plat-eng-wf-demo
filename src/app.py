from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message': "You're doing great! :)",
        'hostname': socket.gethostname(),
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'ok'
    }), 200

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')


# '/api/v1/details'
# '/api/v1/healthz'