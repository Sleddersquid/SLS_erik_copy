
# Får ikke til å laste ned zbarlight

import zbarlight

def decode_barcode(image_file):
    # Open the image file in binary mode
    with open(image_file, 'rb') as image_file:
        image = image_file.read()
    
    # Decode the barcode
    barcodes = zbarlight.scan_codes('qrcode', image)
    
    # Return the decoded barcode data
    return barcodes

# Call the function
barcode_data = decode_barcode("barcode.jpg")

# Print the barcode data
print(barcode_data)