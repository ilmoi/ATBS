# What is an RGBA value?
# red green blue opacity (alpha)
# 2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?
# ImageColor.getcolor()
# 3. What is a box tuple?
# min_x, min_y, max_x, max_y

# 4. What function returns an Image object for, say, an image file named zophie.png?
# Image.open()

# 5. How can you find out the width and height of an Image object’s image?
# w,h = img.size

# 6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
# image.crop()

# 7. After making changes to an Image object, how could you save it as an image file?
# image.save()
#
# 8. What module contains Pillow’s shape-drawing code?
# from PIL import ImageDraw
#
# 9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
# draw = ImageDraw.Draw(im)
# draw.line()
