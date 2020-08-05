# 对图片进行阈值过滤和降噪处理

# 导入模板

import pytesseract
from PIL import Image

# 载入图片

code_image1 = Image.open("./tesseract/image/code-4.png")

# 显示图片
code_image1.show()

# 灰度处理
# 利用image对象的concert()方法，传入“L”，这样图像就转为灰色图像
code_image_L = code_image1.convert("L")
code_image_L.show()

# 二值化（阈值过滤和降噪处理）

# 设置二值化阈值100
threshold = 120

table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

print(table)

code_image_point = code_image_L.point(table, "1")

code_image_point.show()

text1 = pytesseract.image_to_string(code_image_point)

print(text1)
