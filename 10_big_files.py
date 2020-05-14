"""This simple script locates all files above 100mb in a certain folder and its subfolders.
Then deletes them.
"""

import os
import send2trash
from pathlib import Path

# if you add big files inside of the first path, this breaks down
p = Path('/Users/ilja/Downloads/') / "big files"
for dir, folders, files in os.walk(p):
    for file in files:
        file_p = p / dir / file
        file_s = os.path.getsize(file_p)
        if file_s > 10**8:
            print(file_p, file_s)
            print('moving to trash')
            # send2trash.send2trash(str(file_p)) #UNCOMMENTING ON PURPOSE
    # print(dir, folders, files)
