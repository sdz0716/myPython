
def combineIntoDict(ip='1-ip.txt', name='1-name.txt'):
    fileDict = {}
    fileName = []
    fileIp = []
    with open('C:\\Users\\daize\\Desktop\\%s' % ip) as serverIps:
        for ip in serverIps.readlines():
            fileIp.append(ip.strip('\n, '))
    with open('C:\\Users\\daize\\Desktop\\%s' % name) as serverNames:
        for name in serverNames.readlines():
            fileName.append(name.strip('\n, '))

    for i in range(len(fileIp)):
        fileDict[fileIp[i]] = fileName[i]
    return fileDict

if __name__ == '__main__':
    print(combineIntoDict('1-ip.txt', '1-name.txt'))

