from sys import argv, exc_info
from os import name, path
import gos

def getData():
    data = {}

    userPath = path.expanduser('~')
    userName = path.split(userPath)[-1]
    data['userName'] = userName

    data['osName'] = name

    data['usbLabel'] = argv[2]
    # TODO: check label path if its exists else raise

    data['stickPath'] = argv[3]
    # TODO: check stick path if its exists else raise

    if requestedFunc == 'clone' and len(argv) == 5:
        data['targetPath'] = argv[4]
        # TODO: check target path if its exists else raise
    
    return data

def getGosFunc(callFunc, data):
    switcher = {
        'init': gos.s_init,
        'clone': gos.s_clone,
        'push': gos.s_push,
        'pull': gos.s_pull
    }
    return switcher[callFunc](data)

def main(requestedFunc, data):
    return getGosFunc(requestedFunc, data)

if __name__ == "__main__":
    try:
        gosFuncList = dir(gos)
        requestedFunc = argv[1]
        if not(('s_' + requestedFunc) in gosFuncList):
            raise Exception('Incorrect Function Argument!')

        data = getData()
        
    except Exception as err:
        print(err)

    except:
        print("Unexpected error:", exc_info()[0])
        raise

    else:
        main(requestedFunc, data)

    finally:
        print('--END OF LINE--')

# gos init Liquid /Repo/folder
# gos clone Liquid /Repo/folder [target]
# gos pull Liquid /Repo/folder
# gos push 
