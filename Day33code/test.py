import pytesseract
from PIL import Image

# 载入图片

image = Image.open("./tesseract/image/2.png")

# 识别图片中的文字

test = pytesseract.image_to_string(image)

print(test)