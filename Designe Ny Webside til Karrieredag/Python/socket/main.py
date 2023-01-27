from flask import Flask, request
import cv2
import numpy as np
import asyncio
import websockets


app = Flask(__name__)

@app.route("/display_image", methods=["POST"])
def display_image():
    # Get the image data from the request
    image_data = request.data

    # Convert the image data to a numpy array
    nparr = np.fromstring(image_data, np.uint8)

    # Decode the image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Display the image
    cv2.imshow("Webcam Feed", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return "Image displayed"

async def handle_websocket(websocket, path):
    while True:
        image_data = await websocket.recv()
        # do something with the image data
        print("received image")


start_server = websockets.serve(handle_websocket, "localhost", 5020)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

