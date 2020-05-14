"""Finds all pdfs in cur dir > sorts alphabetically > merges together taking the first page only once."""

import PyPDF2
import os
import re

# prep the files list
files = os.listdir()
chosen = []
r = re.compile(r'.*\.pdf')
for file in files:
    try:
        mo = r.search(file)
        # print(mo.group())
        chosen.append(mo.group())
    except:
        pass
chosen.sort()

# manually removing the encrypted file (cba)
chosen.pop(1)
chosen.pop(1)
print(chosen)

# create writer
writer = PyPDF2.PdfFileWriter()

# iterate through files and pages and write them all down
for i, file in enumerate(chosen):
    with open(file, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)

        # for first doc - add the first page too
        if i == 0:
            pageObj = reader.getPage(0)
            writer.addPage(pageObj)

        # for all docs
        for p in range(1, reader.numPages):
            pageObj = reader.getPage(p)
            writer.addPage(pageObj)

        # finally write
        # NOTE this one needs to sit inside of the with open statement or the pages will be blank!
        with open('longfile.pdf', 'wb') as f:
            writer.write(f)

# lets check number of pages matches
for file in chosen:
    with open(file, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        print(reader.numPages)

print('compare that to ----->')
with open('longfile.pdf', 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    print(reader.numPages)
# sounds correct!
