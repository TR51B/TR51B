from PIL import Image, ImageEnhance, ImageFilter
import os
path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).rotate(-90)

    print(edit.format, edit.size,edit.mode)
    edit = edit.crop((0,300,3000,3000))
    
    print(edit.format, edit.size, edit.mode)
    factor = 1.001
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)


    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.png')