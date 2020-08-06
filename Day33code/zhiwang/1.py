from PIL import Image
import pytesseract


# 载入图片
image = Image.open('./images/CheckCode2.jpeg')

# 处理图片（灰度处理和二值化）

# 灰度处理，可以使图片背景的干扰线和干扰点被淡化

image_L = image.convert("L")

image_L.show()

# 二值化，就是把图片的RGB256个颜色全部设置1和0，简单说就是图片进行黑白处理

threshold = 130  # 阈值（为了区分黑白）

table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image_P = image_L.point(table, "1")


# 识别图片上的文字
text = pytesseract.image_to_string(image_P)

print(text)



