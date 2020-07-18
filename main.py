from sys import argv, exc_info
from os import name, path
import gos

def getGosFunc(callFunc, data):
    switcher = {
        'init': gos.s_init,
        'clone': gos.s_clone,
        'push': gos.s_push,
        'pull': gos.s_pull
    }
    return switcher[callFunc](data)

def main(requestedFunc, data):
    getGosFunc(requestedFunc, data)
    return 1
    

if __name__ == "__main__":
    try:
        gosFuncList = dir(gos)
        requestedFunc = argv[1]
        if not(('s_' + requestedFunc) in gosFuncList):
            raise Exception('Incorrect Function Argument!')

        getData = {}

        osName = name
        getData['osName'] = osName

        userPath = path.expanduser('~')
        userName = path.split(userPath)[-1]
        getData['userName'] = userName

        getData['usbLabel'] = argv[2]
        # TODO: check label path if its exists else raise

        getData['stickPath'] = argv[3]
        # TODO: check stick path if its exists else raise

        if requestedFunc == 'clone' and len(argv) == 5:
            getData['targetPath'] = argv[4]
            # TODO: check target path if its exists else raise

    except Exception as err:
        print(err)

    except:
        print("Unexpected error:", exc_info()[0])
        raise

    else:
        main(requestedFunc, getData)

    finally:
        print('--END OF LINE--')

# gos init Liquid /Repo/folder
# gos clone Liquid /Repo/folder [target]
# gos pull Liquid /Repo/folder
# gos push 
