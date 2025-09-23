# Now we are going to generate a qr code 

'''import qrcode as qr
img = qr.make("https://www.youtube.com/@TheIndianFolks")  # this generate the QR code 

img.save("The_indian_folks.png")'''


# The QR code is generated now we are going to add some details like color and more 

import qrcode 
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)

qr.add_data("https://www.youtube.com/@TheIndianFolks")
qr.make(fit = True)

img = qr.make_image(fill_color = "red",back_color = "white")
img.save("The_indian_folks_youtube.png")