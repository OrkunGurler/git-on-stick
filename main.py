from sys import argv, exc_info
from os import path, uname, makedirs
from gos import s_init, s_clone, s_push, s_pull

def getData():
    data = {}

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
        response = input('Do you want to create new directory? [Y,n]: ')
        if response.lower() == 'y':
            makedirs(wholeSPath)
            data['stickPath'] = argv[3]
        else:
            raise Exception('Process Terminated By User')


    if (requestedFunc == 'clone' or requestedFunc == 'init') and len(argv) == 5:
        if path.exists(argv[4]):
            data['targetPath'] = argv[4]
        else:
            print('Target Directory Can NOT Found! ' + argv[4])
            response = input('Do you want to create new directory? [Y,n]: ')
            if response.lower() == 'y':
                makedirs(argv[4])
                data['targetPath'] = argv[4]
            else:
                raise Exception('Process Terminated By User')
    
    return data

def getGosFunc(callFunc, data):
    switcher = {
        'init': s_init,
        'clone': s_clone,
        'push': s_push,
        'pull': s_pull
    }
    return switcher[callFunc](data)

def main(requestedFunc, data):
    return getGosFunc(requestedFunc, data)

if __name__ == "__main__":
    try:
        gosFuncList = ['init', 'clone', 'push', 'pull']
        if argv[1] in gosFuncList:
            requestedFunc = argv[1]
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
        print('--END OF LINE--')

# gos init USB_LABEL /Repo/Folder [target]
# gos clone USB_LABEL /Repo/Folder [target]
# gos pull USB_LABEL /Repo/Folder
# gos push 
