from subprocess import run
from os import chdir

def s_init(data):
    run(['git', 'init', '--bare', data["usbLabelPath"] + "/" + data["stickPath"]])
    run(['git', 'init', data["targetPath"]])
    chdir(data["targetPath"])
    run(['git', 'remote', 'add', data["usbLabel"], data["usbLabelPath"] + '/' + data["stickPath"]])
    
    return

def s_clone():
    print('hello clone')
    return

def s_push(data):
    run(['git', 'push', data["usbLabel"], data["branch"]])
    
    return

def s_pull():
    print('hello pull')
    return
