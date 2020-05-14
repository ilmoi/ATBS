"""Takes a bunch of names from csv file and prepares invitation cards for them"""

import os
import csv
from PIL import Image, ImageDraw, ImageFont

os.chdir('/Users/ilja/Dropbox/atbs')

# with open('invitee_names.csv', 'w') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(['first', 'last'])
#     csv_writer.writerow(['ilja', 'moisejevs'])
#     csv_writer.writerow(['margarita', 'moisejeva'])
#     csv_writer.writerow(['nikolaj', 'maslov'])

names = []
with open('invitee_names.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        first = row['first']
        last = row['last']
        names.append((first, last))

print(names)

for name in names:
    first = name[0]
    last = name[1]
    card = Image.open('invitation_card.jpg')
    w, h = card.size
    draw = ImageDraw.Draw(card)

    fontsFolder = '/System/Library/Fonts/Supplemental'
    comicFont = ImageFont.truetype(os.path.join(fontsFolder, 'Courier new.ttf'), 50)

    draw.text(
        (w/3, h/3), f'Dear {first} {last}\n\n\n\nYou are invited\nto hackerfest!\n\n\n\nBring cookies!', fill='purple', font=comicFont)

    card.save(f'invite_{first}{last}.jpg')
