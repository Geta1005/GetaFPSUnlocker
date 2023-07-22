import os
import json
import pygetwindow as gw
import time
import random

def json_write(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def replace(target,old,new):
    return str(target).replace(old,new)

def createFolder(path):
    if os.mkdir(path):
        return path
    else:
        return False

def isExist(path):
    if os.path.exists(path):
        return True
    else:
        return False

def checkRobloxTab():
    roblox_windows = gw.getWindowsWithTitle('Roblox')
    if len(roblox_windows) > 0:
        roblox_window = roblox_windows[0]
        return roblox_window
    else:
        return False
    
pathtoroblox = replace(os.environ["ProgramFiles(x86)"],'\\','/')+"/Roblox"
robloxfolder = None

while True:
    try:
        os.system('cls')
        credit = """
 _______  _______   __________  ______  
|\   ____\|\  ___ \|\___   ___\\\\   __  \\
\ \  \___|\ \   __/\|___ \  \_\ \  \|\  \ 
 \ \  \  __\ \  \_|/__  \ \  \ \ \   __  \   
  \ \  \|\  \ \  \_|\ \  \ \  \ \ \  \ \  \ 
   \ \_______\ \_______\  \ \__\ \ \__\ \__\ 
    \|_______|\|_______|   \|__|  \|__|\|__|

                < geta1005 >
         < GetaFPSUnlocker v0.0.3 >
        """
        print(credit)
        select = input(f'---------------------------------------------\n> [0] Close\n> [1] Unlock FPS\n> [2] Set FPS to default\n---------------------------------------------\n>>>>> ')
        if select == '0':
            break
        elif select == '1':
            print('> [-] Checking...')
            if isExist(pathtoroblox):
                pathtoversions = pathtoroblox+'/Versions'
                if isExist(pathtoversions):
                    for i in os.listdir(pathtoversions):
                        if isExist(pathtoversions+'/'+str(i)+'/'+'COPYRIGHT.txt'):
                            robloxfolder = pathtoversions+'/'+str(i)
                    if robloxfolder:
                        clientpath = robloxfolder+'/'+'ClientSettings'
                        jsonpath = clientpath+'/'+'ClientAppSettings.json'
                        if not isExist(clientpath):
                            createFolder(clientpath)
                        newData = {
                            "DFIntTaskSchedulerTargetFps": 5588562
                        }
                        print('> [-] Start unlocking FPS')
                        json_write(jsonpath,newData)
            print('> [*] FPS unlocked successfully, please rejoin the game to apply.')
            robloxTab = checkRobloxTab()
            if robloxTab:
                closeRoblox = input('[Y/N] Close Roblox?\n>>>>> ')
                if closeRoblox.lower() == 'y':
                    robloxTab.close()
                    print('[*] Closed roblox tab')
        elif select == '2':
            print('> [-] Checking...')
            pathtoversions = pathtoroblox+'/Versions'
            if isExist(pathtoversions):
                for i in os.listdir(pathtoversions):
                    if isExist(pathtoversions+'/'+str(i)+'/'+'COPYRIGHT.txt'):
                        robloxfolder = pathtoversions+'/'+str(i)
                if robloxfolder:
                    clientpath = robloxfolder+'/'+'ClientSettings'
                    jsonpath = clientpath+'/'+'ClientAppSettings.json'
                    if isExist(jsonpath):
                        os.remove(jsonpath)
                    print('> [-] Start adjusting FPS to default')
            print('> [*] FPS has been set to default, please rejoin the game to apply')
            robloxTab = checkRobloxTab()
            if robloxTab:
                closeRoblox = input('[Y/N] Close Roblox?\n>>>>> ')
                if closeRoblox.lower() == 'y':
                    robloxTab.close()
                    print('> [-] Closed roblox tab')
    except:
        print('> [*] try Run as Administrator or contact geta1005 via discord...')
    input('Press enter to countinue...')
