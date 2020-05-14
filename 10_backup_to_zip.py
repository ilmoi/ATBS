import shutil
import os
import re

current_archives = os.listdir('./10_backups')
print(current_archives)

max = 0
r = re.compile(r'\d')
for a in current_archives:
    try:
        mo = r.search(a)
        number = int(mo.group())
        if number > max:
            max = number
    except:
        continue
print(max)

shutil.make_archive(f'10_backups/archive{max+1}', 'xztar', '10_dates')
