import qrcode as qr
from PIL import Image

qr = qrcode.QRCode(version =1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://github.com/Tripathi-Ashu")
qr.make(file=True)
img=qr.make_image(file_color="red", back_color="blue")
img.save("ashu.png")