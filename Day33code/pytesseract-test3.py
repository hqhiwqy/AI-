# 识别图像中的中文字符

# 导入模块

import pytesseract
from PIL import Image

# 载入图片
chinese_image = Image.open("./tesseract/image/test-chinese.png")

# 显示图片
chinese_image.show()

text = pytesseract.image_to_string(chinese_image, lang="chi_sim")

print(text)