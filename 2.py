

from PIL import Image, ImageFilter
import os

papka = 'C:\\Lab9\\img\\'
myimg = list(filter(lambda x: x.endswith('.jpg'), os.listdir(papka)))
os.mkdir("C:\\lab9\\img\\filter")
for file in myimg:
    img = Image.open(papka + file)
    img.load()
    new_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    new_img.save("C:\\lab9\\img\\filter\\new" + str(file) + ".jpg")