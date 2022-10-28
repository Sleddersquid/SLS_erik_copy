# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, Response
import urllib.request
import os
import cv2
from pyzbar.pyzbar import decode

app = Flask(__name__)
# Create a videocapture called camera
camera = cv2.VideoCapture(0)

# Function to open up camera and read the images
def generate_frames():
    while True:
    # Read from the cameraframe
        # Creates a boolean success and creates continuous frames from video
        success, frame = camera.read()
        if not success:
            break
        else:
            # Check for barcodes in each frame from camera.read()
            for barcode in decode(frame):
                print(barcode.data)
            # Create boolean to see if conversion succesfull
            # Create buffer that stores one jpg
            ret, buffer = cv2.imencode('.jpg', frame)
            # Convert buffer jpg to bytes
            frame = buffer.tobytes()
        # Magic
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def format_barcode(barcode_string):

    return barcode_string

@app.route("/")

# Default landing page is index.html which the function index() calls
def index():
    return render_template("index.html")

# Magic
@app.route("/video")
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5010)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
