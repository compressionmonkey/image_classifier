from PIL import Image
import os


im = Image.open("File1.jpg")
outpath = 'Datasets'

if not os.path.exists(outpath):
    os.makedirs(outpath)


global left, upper, right, lower
#these specify the position of the file
left =400
upper=10
right=480
lower=120

startingnumber = 0

for px in range(4):
    box = (left,upper,right,lower)
    im2 = im.crop(box)
    differentnum = 'px' + str(startingnumber) + '.jpg'
    startingnumber += 1
    filename = 'Datasets/' + differentnum
    im2.save(filename)
    im2.show()
    left = left + 500
    # upper makes height smaller. Adding value to it reduces the height
    right = right+500
    # # this is the right side of the jpg file. Adding value increases the width
    # lower makes height greater
    box = (left,upper,right,lower)
    im2 = im.crop(box)
    im2.save('px.jpg')
    im2.show()

