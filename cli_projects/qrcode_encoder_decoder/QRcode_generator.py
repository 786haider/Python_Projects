import qrcode
from PIL import Image


data = input("Enter your text to generate QR code: ")
file_name = input("Create file name to save: ")
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
img.save('{file_name}.png'.format(file_name=file_name))
