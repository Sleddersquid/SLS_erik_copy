# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:37:00 2022
inspiration: https://www.youtube.com/watch?v=QnDWIZuWYW0&ab_channel=CoreySchafer
To launch: go to terminal, to where the python file is, and type : python "flaskblog.py"
click on the website shown
@author: aditi
"""

from flask import Flask, render_template,Response
from pyzbar.pyzbar import decode
import cv2
#from pyzbar.pyzbar import decode
#instantiated flask application
app = Flask(__name__)
app = Flask(__name__, template_folder='Template')
cap=cv2.VideoCapture(0)
cap.set(3, 640) # 3 -width
cap.set(4, 480) # 4 -Height


Index = [
    {'Creators' : 'Aditi Deshpande, Theo Magnor',
     'title' : 'Post 1',
     'content' : 'lorem ipsum',
     'date_posted' : 'September 25 2022'
     } ,
    {
     'Creators' : 'Hannes Weigel, Nathaneal',
      'title' : 'Post 2',
      'content' : 'lorem ipsum lorem ipsum',
      'date_posted' : 'September 23 2022'
     }
    ]

def generate_frames():
    camera=True
    while camera == True:
        success, frame = cap.read()

        for code in decode(frame):
            print(code.type)
            print(code.data.decode)

        cv2.imshow("scan",frame)
        cv2.waitKey(0)
    '''
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    '''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')




#routes are what we type into our browser
#adds additional functionality
#home page

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',Index=Index)



#about page
@app.route("/about")
def about():
    return render_template('about.html')



#running the app, debug is true so that we don't need to close web server and refresh to see changes 
if __name__ == '__main__':
        app.run(debug=False)


    

    
    
    
        