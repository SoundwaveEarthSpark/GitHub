from PIL import Image #стандартная работа с изображением
from PIL import ImageFilter #наложение фильтров
from PIL import ImageDraw #рисование

image = Image.open('img.jpg')
print(image.size)
print(image.format)
print(image.mode)

image.rotate(85).show()
image.filter(ImageFilter.BLUR).show()


with Image.open("img.jpg") as im:

    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=165)
    draw.line((0, im.size[1], im.size[0], 0), fill=165)
    im.show()




