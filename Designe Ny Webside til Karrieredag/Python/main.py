'''
import asyncio
import websockets

async def webcam_handler(websocket, path):
    while True:
        img_data = await websocket.recv()
        # Do something with the received image data, such as saving it to a file or displaying it on the server
        # ...

start_server = websockets.serve(webcam_handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
'''

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import base64


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('message')
def handle_message(data):
    print("received message: " + data)
    emit("message", "Hello from the server")
    image = base64.b64decode(data)
    emit("image", image)

@socketio.on('snapshot')
def handle_snapshot(data):
    with open("snapshot.jpg", "wb") as f:
        f.write(data.split(",")[1].decode("base64"))
        print("snapshot")

@app.route('/landing')
def landing():
    user_name = "John Doe"
    items = [
        {"name": "Item 1", "identifier": "A1", "stock": 10},
        {"name": "Item 2", "identifier": "B2", "stock": 5},
        {"name": "Item 3", "identifier": "C3", "stock": 2},
    ]
    print("landing page")
    return render_template('landing.html', user_name=user_name, items=items)


@app.route('/')
def index():
    print("index page")
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5010)
    #app.run(host='0.0.0.0', port=5010, debug="FALSE")
