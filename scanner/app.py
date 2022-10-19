
from flask import Flask, redirect, url_for, render_template, request
import cv2
from pyzbar.pyzbar import decode

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            print("camera fail")
            break
        else:
                        
            for code in decode(frame):
                print(code.data)

        
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["student_nr"]

        if request.form.get("Submit") == "Submit" :
            return redirect(url_for("user", usr=user))
        
        if request.form.get("Scan") == "Scan" :
            return render_template("camera.html")
    else:
        return render_template("login.html")



@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


#===
@app.route("/<usr>", methods=["GET", "POST"])
def user(usr):
    
    if request.method == 'POST':
        if    request.form.get('VALUE1') == 'Låne':
            pass # åpner camera og ber brukeren scanne utstyr
        elif  request.form.get('VALUE2') == 'Levere':
            pass # vise side med lån hvor man kan velge hva man vil levere tilbake
        elif  request.form.get('Se lån') == 'Se lån':
            return render_template("show_loans.html") # vise side med brukerens lån
            
    elif request.method == 'GET':
        return render_template('user.html', usr=usr)
    
    return render_template("index.html")
#===


if __name__=="__main__":
    app.run(debug=False)