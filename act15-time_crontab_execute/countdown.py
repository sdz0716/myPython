#! python3
# countdown.py - a simple countdown script

import time
import subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'C:\\Users\\daize\\Desktop\\pythonTEST\\Automate\\alarm.wav'], shell=True)