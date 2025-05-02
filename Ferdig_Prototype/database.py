import datetime

from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = [
    {
        "db": "mydatabase",
        "host": "127.0.0.1",
        "port": 27017,
    }
]
db = MongoEngine(app)

class AllInventory(db.Document):
    barcode = db.StringField()
    ownedByUser = db.StringField()
    product_brand = db.StringField()
    product_name = db.StringField()
    rom_nr = db.IntField()
    datetime_ms = db.DateTimeField(default=datetime.datetime.now())


def createindex():
    AllInventory(barcode="0001", ownedByUser="",product_brand="HP", product_name="24' Skjerm", rom_nr=1206).save()
    AllInventory(barcode="0002", ownedByUser="",product_brand="Arduino", product_name="Mega", rom_nr=1226).save()
    AllInventory(barcode="0003", ownedByUser="",product_brand="Arduino", product_name="Uno", rom_nr=1226).save()
    AllInventory(barcode="0004", ownedByUser="",product_brand="Koss", product_name="Headphones", rom_nr=1226).save()
    AllInventory(barcode="0005", ownedByUser="",product_brand="Biltema", product_name="Multimeter", rom_nr=1226).save()
    AllInventory(barcode="0006", ownedByUser="",product_brand = "Lego", product_name = "Technic", rom_nr=1226).save()

if __name__ == "__main__":
    print("Succes in creating database")
    createindex()

