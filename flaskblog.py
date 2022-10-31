# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:37:00 2022
inspiration: https://www.youtube.com/watch?v=QnDWIZuWYW0&ab_channel=CoreySchafer
To launch: go to terminal, to where the python file is, and type : python "flaskblog.py"
click on the website shown
@author: aditi
"""

from flask import Flask, render_template,url_for,request
from pyzbar.pyzbar import decode
from PIL import Image
#instantiated flask application
app = Flask(__name__,template_folder='Template')

#routes are what we type into our browser
#adds additional functionality
#home page

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



#about page
@app.route("/about")
def about():
    return render_template('about.html',title='About')
#upload page with barcode
@app.route("/upload", methods=("POST", "GET"))
def upload():
    if request.method == "POST":
        file = request.files['stud']
        img = Image.open(file.stream)
        print (type(file.stream))
        decoded_img = decode(img)[0]
        studnr = decoded_img.data
        return redirect(url_for("user", usr=studnr))
    else:
        return render_template("upload.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


#running the app, debug is true so that we don't need to close web server and refresh to see changes 
if __name__ == '__main__':
        app.run(debug=True)


    

    
    
    
        