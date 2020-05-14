"""This simple python script converts any files with american dates in their name to european dates."""

import os
import re
import shutil
from pathlib import Path

# start by making sure we're in the right directory
p = Path('/Users/ilja/Dropbox/ATBS/10_dates')
os.chdir(p)

# Create a regex that can identify the text pattern of American-style dates.
r = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')

# Call os.listdir() to find all the files in the working directory.
# Loop over each filename, using the regex to check whether it has a date.
for file in os.listdir():
    mo = r.search(file)
    s = (p/file).suffix
    try:
        old_file_name = f'{mo.group()}{s}'
        print(f'found {old_file_name}')
        new_file_name = f'{mo.group(2)}-{mo.group(1)}-{mo.group(3)}{s}'
        # If it has a date, rename the file with shutil.move().
        shutil.move(old_file_name, new_file_name)
        print(f'new file name is {new_file_name}')
    except:
        print('file does not match')
