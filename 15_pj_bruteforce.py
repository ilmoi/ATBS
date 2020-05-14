"""This first encrypts a doc with a random english word, then brute force finds it."""


import PyPDF2
import random


# ==============================================================================
# PART 1 - ENCRYPTING THE DOC (DO EONCE)

# # picking a random word (even I won't know!)
# with open('automate_online-materials/dictionary.txt', 'r') as f:
#     txt = f.readlines()
#     random_line = random.choice(txt)[:-1]
#     # print(random_line)
#     # print(len(random_line))
#
# # copying an existing doc and encrypting it
# writer = PyPDF2.PdfFileWriter()
# writer.encrypt(random_line)
#
# with open('combinedminutes.pdf', 'rb') as f:
#     reader = PyPDF2.PdfFileReader(f)
#
#     for p in range(reader.numPages):
#         writer.addPage(reader.getPage(p))
#
#     with open('english-crypted.pdf', 'wb') as f:
#         writer.write(f)


# ==============================================================================
# PART 2 - DECRYPTING THE DOC

pdf = open('english-crypted.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf)

pws = open('automate_online-materials/dictionary.txt', 'r')
txt = pws.readlines()

status = 0
for i, line in enumerate(txt):
    attempt = line[:-1]
    # print(attempt)
    status = reader.decrypt(attempt)

    if i % 1000 == 0:
        print(f'attempted {i} passwords.')

    if status == 1:
        break

print(attempt)

pdf.close()
pws.close()
