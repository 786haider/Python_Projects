from pyzbar.pyzbar import decode
from PIL import Image

file_name = input("Enter file name: ")
img = Image.open('{file_name}.png'.format(file_name=file_name))
result = decode(img)
print(result)