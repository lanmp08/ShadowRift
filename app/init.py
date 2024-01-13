import socket
from flask import Flask, render_template

app = Flask(__name__)
sockets = socket.socket(app)

@app.route('/')
def index():
    return render_template('index.html')

def message_received(client, message):
    pass # Implementar a lógica de recebimento de mensagens aqui

@sockets.route('/subscribe')
def subscribe_socket(ws):
    ws.send('Connected')
    for message in ws:
        message_received(ws, message)