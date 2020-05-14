"""Counts down specified amount of time then plays the sound."""

import subprocess
import time
import datetime

for i in range(5, -1, -1):
    time.sleep(1)
    print(i)

subprocess.Popen(['open', '/Users/ilja/Dropbox/atbs/automate_online-materials/alarm.wav'])
