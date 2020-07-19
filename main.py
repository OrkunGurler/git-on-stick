from sys import argv, exc_info
from os import path, uname, makedirs, getcwd
from gos import s_init, s_clone, s_push, s_pull

#
#
# 
def getData():
    data = {}

    data['argv'] = argv

    data['requested'] = argv[1]

    userPath = path.expanduser('~')
    userName = path.split(userPath)[-1]
    data['userName'] = userName

    os = uname()
    data['osName'] = os.sysname

    if data['osName'] == 'Linux':
        labelPath = ('/run' if 'arch' in os.release else '') + '/media/' + data['userName'] + '/' + argv[2]
        if path.exists(labelPath):
            data['usbLabel'] =  argv[2]
            data['usbLabelPath'] = labelPath       
        else:
            raise Exception('USB Label Can NOT Found!')

    if not(argv[3][1] == '/'):
        wholeSPath = data['usbLabelPath'] + '/' + argv[3]
    else:
        wholeSPath = data['usbLabelPath'] + argv[3]
    if path.exists(wholeSPath):
        data['stickPath'] = argv[3]
    else:
        print('Source Directory Can NOT Found! ' + argv[3])
        response = input('Do you want to create new directory for source path? [Y,n]: ')
        if response.lower() == 'y':
            makedirs(wholeSPath)
            data['stickPath'] = argv[3]
        else:
            raise Exception('Process Terminated By User')

    if (requestedFunc == 'clone' or requestedFunc == 'init') and len(argv) == 5:
        data['targetPath'] = getcwd() + '/' + argv[4]
        if not path.exists(argv[4]):
            print('Target Directory Can NOT Found! ' + argv[4])
            response = input('Do you want to create new directory for target path? [Y,n]: ')
            if response.lower() == 'y':
                makedirs(argv[4])
            else:
                raise Exception('Process Terminated By User')
    else:
        data['targetPath'] = getcwd()
        print(data['targetPath'])
    
    return data

#
#
#
def getGosFunc(callFunc, data):
    switcher = {
        'init': s_init,
        'clone': s_clone,
        'push': s_push,
        'pull': s_pull
    }
    return switcher[callFunc](data)

#
#
#
def main(requestedFunc, data):
    return getGosFunc(requestedFunc, data)

#
#
#
if __name__ == "__main__":
    try: 
        argvLen = len(argv)
        if argvLen == 1:
            raise Exception('Missing Arguments')

        gosFuncList = ['init', 'clone', 'push', 'pull']
        if argv[1] in gosFuncList:
            requestedFunc = argv[1]
            if not(requestedFunc == 'push') and argvLen < 4:
                raise Exception('Missing Arguments')
            if argvLen > 5:
                raise Exception('Unexpected Argument(s)!')
        else:
            raise Exception('Incorrect Function Argument!')

        data = getData()
        print(data)
    except Exception as err:
        print(err)

    except:
        print("Unexpected error:", exc_info()[0])
        raise

    else:
        main(requestedFunc, data)

    finally:
        print('\n--END OF LINE--\n')

# gos init USB_LABEL /Repo/Folder [target]
# gos clone USB_LABEL /Repo/Folder [target]
# gos pull USB_LABEL /Repo/Folder
# gos push 
