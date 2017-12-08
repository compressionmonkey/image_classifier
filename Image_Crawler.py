from PIL import Image
import os

im = Image.open("File1.jpg")
outpath = 'Datasets'
width, height = im.size
print(im.size)
if not os.path.exists(outpath):
    os.makedirs(outpath)

global left, upper, right, lower
#these specify the position of the file
left =400 #+ 1500 #400
upper=10 + 320
right=480 #+ 1500
lower=120 + 320
box = (left,upper,right,lower)
im2 = im.crop(box)
im2.save('px.jpg')
im2.show()
startingnumber = 0
YMovement = int("19" + "00")
XMovement = int("10" + "320")
print(box)
if (left, right <= width and upper, lower <= height):

    for px in range(4):
        if (left != 1900 and right != 1980):
            differentnum = 'px' + str(startingnumber) + '.jpg'

            filename = 'Datasets/' + differentnum
            box = (left, upper, right, lower)
            im2 = im.crop(box)
            im2.save(filename)
            im2.show()
            print(box)

            left = left + 500
            # upper makes height smaller. Adding value to it reduces the height
            right = right+500
            # # this is the right side of the jpg file. Adding value increases the width
            # lower makes height greater
            startingnumber += 1
            differentnum = 'px' + str(startingnumber) + '.jpg'

            filename = 'Datasets/' + differentnum
            box = (left,upper,right,lower)
            im2 = im.crop(box)
            im2.save(filename)
            im2.show()
            print(box)
        if (left >= 1900 and right >= 1980):
            print(left,right)
            left = 400
            upper = 10 + 320
            right = 480
            lower = 120 + 320
            for Yposition in range(4):
                startingnumber = 4
                differentnum = 'px' + str(startingnumber) + '.jpg'

                filename = 'Datasets/' + differentnum
                box = (left, upper, right, lower)
                im2 = im.crop(box)
                im2.save(filename)
                im2.show()
                print(box)

                left = left + 500
                # upper makes height smaller. Adding value to it reduces the height
                right = right + 500
                # # this is the right side of the jpg file. Adding value increases the width
                # lower makes height greater
                startingnumber += 1
                differentnum = 'px' + str(startingnumber) + '.jpg'

                filename = 'Datasets/' + differentnum
                box = (left, upper, right, lower)
                im2 = im.crop(box)
                im2.save(filename)
                im2.show()
                print(box)



