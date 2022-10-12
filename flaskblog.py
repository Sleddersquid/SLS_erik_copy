# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:37:00 2022
inspiration: https://www.youtube.com/watch?v=QnDWIZuWYW0&ab_channel=CoreySchafer
To launch: go to terminal, to where the python file is, and write 
@author: aditi
"""

from flask import Flask, render_template
import cv2
#from pyzbar.pyzbar import decode
#instantiated flask application
app = Flask(__name__)
app = Flask(__name__, template_folder='Template')


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
        app.run(debug=True)


    

    
    
    
        