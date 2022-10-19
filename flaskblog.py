# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:37:00 2022
inspiration: https://www.youtube.com/watch?v=QnDWIZuWYW0&ab_channel=CoreySchafer
To launch: go to terminal, to where the python file is, and type : python "flaskblog.py"
click on the website shown
@author: aditi
"""

from flask import Flask, render_template,url_for
#from pyzbar.pyzbar import decode
#instantiated flask application
app = Flask(__name__,template_folder='Template')


posts = [
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
    return render_template('home.html',posts=posts)



#about page
@app.route("/about")
def about():
    return render_template('about.html',title='About')



#running the app, debug is true so that we don't need to close web server and refresh to see changes 
if __name__ == '__main__':
        app.run(debug=True)


    

    
    
    
        