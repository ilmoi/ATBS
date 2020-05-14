import os
from PIL import ImageColor, Image, ImageDraw, ImageFont

os.chdir('/Users/ilja/Dropbox/atbs')

print("-------------------- COLORS --------------------")
red = ImageColor.getcolor('red', 'RGBA')
print(red)
choc = ImageColor.getcolor('chocolate', 'RGBA')
print(choc)

# pillow generally expects a tuple with 4 coordinates (x_min, y_min, x_max, y_max)
# NOTE that min is including, but max is excluding the actual pixel!


print("-------------------- BASICS --------------------")
cat = Image.open('automate_online-materials/zophie.png')
print(cat)
print(cat.size)
print(cat.filename)
print(cat.format)
print(cat.format_description)

# save with a different image extension
cat.save('zophie2.jpg')

print("-------------------- NEW --------------------")
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purple.png')


print("-------------------- CROP --------------------")
cropped_cat = cat.crop((355, 345, 565, 560))
cropped_cat.save('cropped_cat.jpg')


print("-------------------- C/P --------------------")
# copy to create a new image
cat2 = cat.copy()

# paste one on top of the other
# NOTE paste modifies an image in place
print(cropped_cat.size)
cat2.paste(cropped_cat, (0, 0))
cat2.paste(cropped_cat, (400, 500))
cat2.save('weird_cat.jpg')

# lets fill the entire image with cat's photos
w, h = cat.size
w2, h2 = cropped_cat.size
cat3 = cat.copy()
for left in range(0, w, w2):
    for top in range(0, h, h2):
        cat3.paste(cropped_cat, (left, top))
cat3.save('a_lot_of_cats.jpg')


print("-------------------- RESIZE, ROTATE, FLIP --------------------")
resized_cat = cat.resize((int(w/20), int(h/10)))
resized_cat.save('resized_cat.png')

rot_cat = cat.rotate(90).save('rot_cat.png')

rot_cat2 = cat.rotate(6).save('rot_cat2.png')

# this will expand the size of the image so that the entire rotated image can be filled in, without cropping parts of it
rot_cat3 = cat.rotate(6, expand=True).save('rot_cat3.png')

flip_cat = cat.transpose(Image.FLIP_LEFT_RIGHT).save('flipped_cat.png')


print("-------------------- CHANGE PIXELS --------------------")
im = Image.new('RGBA', (100, 100))

# get
p = im.getpixel((0, 0))
print(p)

# put
for x in range(50):
    for y in range(75):
        im.putpixel((x, y), (210, 210, 210))
for x in range(25):
    for y in range(25):
        im.putpixel((x, y), ImageColor.getcolor('yellow', 'RGBA'))
im.save('colorz.png')


print("-------------------- DRAWING ON IMAGES --------------------")
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)  # receive the draw object
draw.line([(0, 0), (199, 10), (199, 199), (0, 0)], fill='black')
draw.rectangle([20, 30, 60, 90], fill='blue')
for i in range(100, 200, 10):
    draw.line([i, 0, 200, i-100], fill='green')  # note we can pass in tuples or without
    draw.line([(i-1, 1), (199, i-99)], fill='yellow')  # note we can pass in tuples or without

# add text - standard typeface & size
draw.text((20, 150), 'hello world', fill='purple')

# custom typeface & size
fontsFolder = '/System/Library/Fonts/Supplemental'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)

im.save('drawing.png')
