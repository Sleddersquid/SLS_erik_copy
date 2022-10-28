from flask import Flask, redirect, url_for, render_template, request
from pyzbar.pyzbar import decode
from PIL import Image
import pymysql

'''
B00964ou    24'skjerm   Hp          1206
f00964ou    Mega        Arduino     1229
B50964oP    Uno         Arduino     2261
N00964ou    Headphones  Koss        1229
'''

headings = ("Brand", "Product", "ID", "Room")
data = (
    ("Arduino", "Uno", "B50964oP", "2261"),
    ("Arduino", "Mega", "f00964ou", "1229"),
    ("Shahin", "Oscar", "6969", "Your moms house"),
    ("Ole", "Seljordslia", "45678", "Heklo"),
    ("Arduino", "Uno", "B50964oP", "2261"),
    ("Arduino", "Mega", "f00964ou", "1229"),
    ("Shahin", "Oscar", "6969", "Your moms house"),
    ("Ole", "Seljordslia", "45678", "Heklo")
)

def return_item(id_stud, id_item):
    connection, cur = sql_connect()
    sql = f"UPDATE `final` SET `Status`=`Paa lager` WHERE `Student_id`={id_stud} AND `Product_id`={id_item}"
    cur.execute(sql)
    return

def check_out_item(id_stud, id_item):
    connection, cur = sql_connect()
    sql = f"UPDATE `final` SET `Status`=`Utlaant` WHERE `Student_id`={id_stud} AND `Product_id`={id_item}"
    cur.execute(sql)
    return

def sql_connect():
    connection = pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        passwd="password",
        database="SLS_website"
    )
    cur = connection.cursor()
    return connection, cur

def db_fetch(id_stud):
    db, db_cur = sql_connect()
    f_sql = f"SELECT `Fornavn` FROM `student` WHERE `Student_id`={id_stud}"
    l_sql = f"SELECT `Etternavn` FROM `student` WHERE `Student_id`={id_stud}"
    tlf_sql = f"SELECT `telefon_nr` FROM `student` WHERE `Student_id`={id_stud}"
    epost_sql = f"SELECT `email` FROM `student` WHERE `Student_id`={id_stud}"
    db_cur.execute(f_sql)
    f_name = db_cur.fetchone()
    db_cur.execute(l_sql)
    l_name = db_cur.fetchone()
    db_cur.execute(tlf_sql)
    tlf = db_cur.fetchone()
    db_cur.execute(epost_sql)
    epost = db_cur.fetchone()
    return f_name, l_name, tlf, epost





app = Flask(__name__)


def string_short(stud_nr):
    return stud_nr.replace('USNS', '')


def scan(img):
    identifier = decode(img)[0]
    return identifier


def open_img(file):
    img = Image.open(file.stream)
    return img

def remove_char(chars):
    seq_type = type(chars)
    return seq_type().join(filter(seq_type.isdigit, chars))


@app.route("/")
def home():
    return   render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files["stud"]
        img = open_img(file)
        return redirect(url_for("user", usr=scan(img).data))
    else:
        return   render_template("upload.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/my-page", methods=["POST", "GET"])
def my_page():
    if request.method == "POST":
        file = request.files["inventory"]
        img = open_img(file)
        usr = scan(img).data
        new_usr = usr.decode('utf-8')
        f_name, l_name, tlf, epost = db_fetch(new_usr)
        print(type(f_name), type(l_name), type(tlf), type(epost))
        #print(remove_char(f_name), remove_char(l_name), remove_char(tlf), remove_char(epost))
        return   redirect(url_for("user", usr=f_name))
    else:
        return   render_template("borrow.html")


@app.route("/overview", methods=["POST", "GET"])
def overview():
    if request.method == "POST":
        item_id = request.files["item_id"]
        print("hello")
        # If check-out
        return render_template("overview.html")
    else:
        return render_template("overview.html", headings=headings, data=data)

@app.route("/sql")
def sql_test():
    db, db_cur = sql_connect()
    f_sql = f"SELECT `Fornavn` FROM `student` WHERE `Student_id`={238145}"
    l_sql = f"SELECT `Etternavn` FROM `student` WHERE `Student_id`={238145}"
    tlf_sql = f"SELECT `telefon_nr` FROM `student` WHERE `Student_id`={238145}"
    epost_sql = f"SELECT `email` FROM `student` WHERE `Student_id`={238145}"
    db_cur.execute(f_sql)
    f_name = db_cur.fetchone()
    db_cur.execute(l_sql)
    l_name = db_cur.fetchone()
    db_cur.execute(tlf_sql)
    tlf = db_cur.fetchone()
    db_cur.execute(epost_sql)
    epost = db_cur.fetchone()


    print("printing from sql",f_name,l_name,tlf,epost)
    return   redirect(url_for("user", usr=f_name))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5010)
