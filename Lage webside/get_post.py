from flask import Flask, redirect, url_for, render_template, request
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files["stud"]
        img = Image.open(file.stream)
        #user = decode(img)
        decoded_img = decode(img)[0]
        studnr = decoded_img.data
        return redirect(url_for("user", usr=studnr))
    else:
	    return render_template("upload.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5010)