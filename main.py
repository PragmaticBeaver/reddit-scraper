from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"/opt/homebrew/bin/tesseract"
pytesseract.tesseract_cmd = path_to_tesseract

path_to_img = "images/the deepest dark.png"
img = Image.open(path_to_img)

text = pytesseract.image_to_string(img)
print(text)
