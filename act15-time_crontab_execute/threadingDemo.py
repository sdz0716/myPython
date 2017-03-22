import threading, time

print('start of program')

def takeANap():
    time.sleep(5)
    print('wake up')

threadObj = threading.Thread(target=takeANap)       #target参数为takeANap而不是takeANap（），因为takeANap（）是一个返回值，而要多线程处理的是函数
threadObj.start()
print('end of progrom')
