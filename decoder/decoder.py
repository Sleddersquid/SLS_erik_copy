import pyzbar.pyzbar as pyzbar
from PIL import Image

def decode_barcode(image_file):
    # Open the image file
    image = Image.open(image_file)

    # Decode the barcode
    barcodes = pyzbar.decode(image)

    # Get the barcode data
    for barcode in barcodes:
        data = barcode.data.decode("utf-8")
        return ''.join(filter(str.isdigit, data))

barcode_data = decode_barcode("barcode.png")
print(barcode_data)
