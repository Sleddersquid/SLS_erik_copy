# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:37:00 2022

@author: aditi
"""

from flask import Flask, render_template
#instantiated flask application
app = Flask(__name__)
app = Flask(__name__, template_folder='Template')
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
    return "<h1>About page</h1>"
#running the app, debug is true so that we don't need to close web server and refresh to see changes 
if __name__ == '__main__':
        app.run(debug=True)
        