import os
import subprocess
import pyautogui

os.chdir('/Users/ilja/Dropbox/atbs')

# create the two docs

with open('copy_from.txt', 'w') as f:
    f.write('this text is to be copied!')

with open('copy_to.txt', 'w') as f:
    pass

# open a doc
subprocess.Popen(['open', 'copy_from.txt'])

# select all text
pyautogui.sleep(1)
pyautogui.hotkey('command', 'a')

# copy all text
pyautogui.sleep(1)
pyautogui.hotkey('command', 'c')

# close the doc
pyautogui.sleep(1)
pyautogui.hotkey('command', 'q')

# open a second doc
subprocess.Popen(['open', 'copy_to.txt'])

# paste the text
pyautogui.sleep(1)
pyautogui.hotkey('command', 'v')
pyautogui.sleep(1)
pyautogui.write(['return'])
pyautogui.sleep(1)
pyautogui.write('this should do it!', 0.1)

# save
pyautogui.sleep(1)
pyautogui.hotkey('command', 's')

# close
pyautogui.sleep(1)
pyautogui.hotkey('command', 'q')
