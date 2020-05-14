"""This simple script finds all txt files in a folder tree and moves them
to a specified location"""

from pathlib import Path
import os
import re
import shutil

p = Path.cwd() / 'dir1'
new_p = Path.cwd() / 'dir2'

r = re.compile(r'.*\.txt')

for dirpath, dirnames, filenames in os.walk(p):
    for file in filenames:
        # print(dirpath)
        try:
            mo = r.search(file)
            old_p = Path(dirpath) / mo.group()
            shutil.move(str(old_p), str(new_p))  # this needs to take in strings
        except:
            pass
