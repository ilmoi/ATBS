"""finds all images in current folders that are wider than 300px and adds a small cat logo in bottom rhs"""

from PIL import Image
import os

os.chdir('/Users/ilja/Dropbox/atbs')

images = [f for f in os.listdir() if f.endswith('jpg') or f.endswith('.png')]
print(images)

logo = Image.open('automate_online-materials/catlogo.png')
logo_w, logo_h = logo.size
logo_k = logo_w/100
logo = logo.resize((int(logo_w/logo_k), int(logo_h/logo_k)))
logo.save(f'modified_imgs/logo.png')

modified_images = []
for img in images:
    img_f = Image.open(img)
    w, h = img_f.size
    if max(w, h) > 300:
        k = w/300
        img_f = img_f.resize((int(w/k), int(h/k)))

        new_w, new_h = img_f.size

        # need to pass twice, as first and as third argument if you want to have transparent pixels around the cat preserved!
        img_f.paste(logo, (new_w-100, new_h-100), logo)

        img_f.save(f'modified_imgs/{img}.png')
