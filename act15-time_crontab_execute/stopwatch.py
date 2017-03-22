#! python3
# stopwatch.py - stopwatch

import time, pyperclip

print('input Enter to start,and ctrl+C to quit')
input()
print('start')
startTime = time.time()
lastTime = startTime
lapNum = 1
resultList = []
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('lap #%s: %s (%s)' % (lapNum, str(totalTime).rjust(5), str(lapTime).rjust(4)), end='')
        result = 'lap #%s: %s (%s)' % (lapNum, str(totalTime).rjust(5), str(lapTime).rjust(4))
        resultList.append(result)
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:       #无效，待考证
    pyperclip.copy(resultList)
    print('done')
