# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
from pyzbar.pyzbar import decode

image = cv2.imread('Barcodes/Big_collection.png')

detectedBarcodes = decode(image)


for barcode in detectedBarcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)

    print(barcode.data)
    print(barcode.type)



cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
