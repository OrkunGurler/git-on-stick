from sys import platform, argv, exit
from gos import *

def genData():
    cList = {}
    arguments = argv
    argsCount = len(argv)
    if not((argsCount == 1) or (argsCount > 5)):
        for i in range(1, argsCount):
            argSplitted = arguments[i].split('=')
            if not(argSplitted):
                cList[argSplitted[0]] = argSplitted[1]
    else:
        print('Missing or Much Arguments!')
        exit()

    platformList = {'AIX': 'aix', 'FreeBSD': 'freebsd', 'Linux': 'linux', 'Windows': 'win32', 'Windows/Cygwin': 'cygwin', 'macOS': 'darwin'}
    platformName = platform
    flag = 1
    for value in platformList.values():
        if platformName == value:
            cList['--platform'] = platformName
            flag = 0
            break
    if flag:
        print('Unfortunately Your Platform Is NOT Supported!')
    return cList

def getGosFunc(garg):
    switcher = {
        'clone':s_clone(),
        'init':s_init(),
        'pull':s_pull(),
        'push':s_push()
    }
    return switcher.get(garg)

def main(data):
    getGosFunc(argv[1])
    return 1
    

if __name__ == "__main__":
    data = genData()
    main(data)
