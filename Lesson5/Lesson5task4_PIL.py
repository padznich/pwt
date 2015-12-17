# http://www.pythonware.com/products/pil/
# http://effbot.org/imagingbook/introduction.htm
#
# PIL module
#
# out = im.resize((128, 128))
# out = im.rotate(45)
# out = im.transpose(Image.FLIP_LEFT_RIGHT)
# out = im.transpose(Image.FLIP_TOP_BOTTOM)
# out = im.transpose(Image.ROTATE_90)
# out = im.transpose(Image.ROTATE_180)
# out = im.transpose(Image.ROTATE_270)
# out = im.size
# out = im.format
# out = im.mode
# img.save('test.gif')
#
# import ImageEnhance
# enh = ImageEnhance.Contrast(im)
# enh.enhance(1.3).show("30% more contrast")

import Image
import ImageEnhance

img = Image.open('cat.jpg')

format = img.format

img90 = img.transpose(Image.ROTATE_90)
img90.save('rotated_cat.jpg')

img_size = img.size
img2x = img.resize((img_size[0] * 2, img_size[1] * 2))
img2x.save('resized_cat.jpg')

enh = ImageEnhance.Contrast(img)
img_conrast = enh.enhance(2.0)
img_conrast.save('cotrasted_cat.jpg')


