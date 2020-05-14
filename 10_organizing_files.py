# shell utility
import send2trash
import shutil
import os
from pathlib import Path

print("-------------------- COPY / MOVE --------------------")
# copies single file
# shutil.copy('dir1/to_be_moved.txt', 'dir2/')

# copies entire directory and all of its contents
# shutil.copytree('dir1', 'dir3')

# move the file
# shutil.move('dir1/to_be_moved.txt', 'dir2/')
# if specify filename in destination, will also rename, as expected
# NOTE: if you specific 'dir2' as destination folder, but dir2 doesn't exist, shutil will rename the file into dir2 instead


print("-------------------- SAFE DEL --------------------")

with open('someFile.txt', 'w') as f:
    f.write('bacon is not a veg')

# you should always use this function instead of perm delete. it's reversible!!
# send2trash.send2trash('someFile.txt')
# send2trash.send2trash('dir1')


print("-------------------- WALK --------------------")
for folderName, subfolders, filenames in os.walk('dir3'):
    print(f'CURRENT FOLDER: {folderName}')
    print(f'renaming all SUBFOLDERS: {subfolders}')
    print(f'doing smthn else to all FILES: {filenames}')
