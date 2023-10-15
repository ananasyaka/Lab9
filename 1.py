

from PIL import Image, ImageFilter
import os

papka = 'C:\\Lab9\\img\\'
myimg = list(os.listdir(papka))
print(myimg)
os.mkdir("C:\\lab9\\img\\filter")
for file in myimg:
    img = Image.open(papka + file)
    img.load()
    new_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    new_img.save("C:\\lab9\\img\\filter\\new" + str(file) + ".jpg")
