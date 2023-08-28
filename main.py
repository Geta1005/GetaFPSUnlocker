import os
import sys
import json
import time
import random
import ctypes
import shutil
import pygetwindow
import requests
from datetime import datetime, date

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def getTimeDate():
    getTime = f'{date.today().strftime("%Y-%m-%d")} {datetime.now().strftime("%H:%M:%S")}'
    return getTime

def json_write(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def json_load(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def replace(target,old,new):
    return str(target).replace(old,new)

def createFolder(path):
    try:
        os.mkdir(path)
        return path
    except:
        return False

def isExist(path):
    if os.path.exists(path):
        return True
    else:
        return False
    
def DebugLog(debugpath,content):
    if isExist(debugpath):
        with open(debugpath, 'a') as file:
            file.write(f'{getTimeDate()} | {content}\n')
    
def getCurrentPath():
    return os.path.abspath(sys.argv[0])

def checkRobloxTab():
    roblox_windows = pygetwindow.getWindowsWithTitle('Roblox')
    if len(roblox_windows) > 0:
        roblox_window = roblox_windows[0]
        return roblox_window
    else:
        return False

currentPath = getCurrentPath()
pathtoprogram86 = replace(os.environ["ProgramFiles(x86)"],'\\','/')
pathtoappdatalocal = replace(os.getenv('LOCALAPPDATA'),'\\','/')
pathrobloxcheck = [
    pathtoprogram86+"/Roblox",
    pathtoappdatalocal+"/Roblox"
]
pathtoroblox = None
configsfolderpath = pathtoprogram86+"/GetaFPSUnlocker"
configspath = pathtoprogram86+"/GetaFPSUnlocker"+'/GetaFPSUnlocker_configs.json'
debugpath = pathtoprogram86+"/GetaFPSUnlocker"+'/DebugLog.txt'
source_path = replace(currentPath,'\\','/')
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
destination_path = os.path.join(startup_folder, os.path.basename(source_path))
version_url = 'https://raw.githubusercontent.com/Geta1005/GetaFPSUnlocker/main/version.txt'
versions = {
    'current': '0.0.7',
    'latest': ''
}
robloxfolder = None
runningStartup = False
if not is_admin():
    if sys.platform.startswith('win'):
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        except ctypes.WinError:
            print('> [*] GetaFPSUnlocker needs to Run as administrator')
            input('Press enter to countinue...')
            sys.exit(0)
    else: 
        print('> [*] GetaFPSUnlocker needs to Run as administrator')
        input('Press enter to countinue...')
        sys.exit(0)
try:
    if not isExist(configsfolderpath):
        createFolder(configsfolderpath)
    if not isExist(debugpath):
        with open(debugpath, 'w') as f:
            f.write('')
        DebugLog(debugpath,"Created DebugLog.txt")
except Exception as e:
    DebugLog(debugpath,e)
    print(f'> [*] Something is wrong! Saved ERROR to DebugLog >> {debugpath}')
    input('Press enter to countinue...')
if str(os.name) == "nt":
    if is_admin():
        try:
            if isExist(replace(destination_path,'\\','/')):
                os.remove(replace(destination_path,'\\','/'))
            getlatestVer = requests.get(version_url)
            versions['latest'] = str(getlatestVer.text).replace('\n','')
            if versions['current'] == versions['latest']:
                while not runningStartup:
                    try:
                        os.system('cls')
                        credit = f"""
 _______  _______   __________  ______  
|\   ____\|\  ___ \|\___   ___\\\\   __  \\
\ \  \___|\ \   __/\|___ \  \_\ \  \|\  \ 
 \ \  \  __\ \  \_|/__  \ \  \ \ \   __  \   
  \ \  \|\  \ \  \_|\ \  \ \  \ \ \  \ \  \ 
   \ \_______\ \_______\  \ \__\ \ \__\ \__\ 
    \|_______|\|_______|   \|__|  \|__|\|__|

                    < geta1005 >
            < GetaFPSUnlocker v{versions['current']} >
                        """
                        print(credit)
                        print('---------------------------------------------\n> [Path] DebugLog: '+replace(debugpath,'/','\\'))
                        select = input(f'---------------------------------------------\n> [0] Close\n> [1] Unlock FPS\n> [2] Set FPS to default\n---------------------------------------------\n>>>>> ')
                        if select == '0':
                            break
                        elif select == '1':
                            os.system('cls')
                            print("> [-] Please select the amount of FPS you want to unlock.\n")
                            print("> [0] Back")
                            print("> [1] Custom")
                            print("> [2] 30")
                            print("> [3] 60")
                            print("> [4] 75")
                            print("> [5] 120")
                            print("> [6] 144")
                            print("> [7] 165")
                            print("> [8] 240")
                            print("> [9] 360")
                            print("> [10] None\n")
                            amountfps = input(">>>>> ")
                            fpscap = None
                            if amountfps == "0":
                                pass
                            elif amountfps == "1":
                                os.system('cls')
                                try:
                                    fpscap = int(input("AMOUNT FPS CAP: "))
                                except Exception as e:
                                    DebugLog(debugpath,e)
                            elif amountfps == "2":
                                fpscap = 30
                            elif amountfps == "3":
                                fpscap = 60
                            elif amountfps == "4":
                                fpscap = 75
                            elif amountfps == "5":
                                fpscap = 120
                            elif amountfps == "6":
                                fpscap = 144
                            elif amountfps == "7":
                                fpscap = 165
                            elif amountfps == "8":
                                fpscap = 240
                            elif amountfps == "9":
                                fpscap = 360
                            elif amountfps == "10":
                                fpscap = 5588562
                            else:
                                print(f'> [*] Wrong input!')
                            if fpscap:
                                print('> [-] Checking...')
                                pathtoroblox = None
                                if isExist(pathrobloxcheck[0]):
                                    pathtoroblox = pathrobloxcheck[0]
                                elif isExist(pathrobloxcheck[1]):
                                    pathtoroblox = pathrobloxcheck[1]
                                else:
                                    print("> [*] Unfound Roblox folder.")
                                if pathtoroblox:
                                    if isExist(pathtoroblox):
                                        pathtoversions = pathtoroblox+'/Versions'
                                        if isExist(pathtoversions):
                                            for i in os.listdir(pathtoversions):
                                                if isExist(pathtoversions+'/'+str(i)+'/'+'RobloxPlayerBeta.exe'):
                                                    robloxfolder = pathtoversions+'/'+str(i)
                                            if robloxfolder:
                                                clientpath = robloxfolder+'/'+'ClientSettings'
                                                jsonpath = clientpath+'/'+'ClientAppSettings.json'
                                                if not isExist(clientpath):
                                                    createFolder(clientpath)
                                                newData = {
                                                    "DFIntTaskSchedulerTargetFps": fpscap
                                                }
                                                print('> [-] Start unlocking FPS')
                                                json_write(jsonpath,newData)
                                    print('> [*] FPS unlocked successfully, please rejoin the game to apply.')
                        elif select == '2':
                            print('> [-] Checking...')
                            pathtoroblox = None
                            if isExist(pathrobloxcheck[0]):
                                pathtoroblox = pathrobloxcheck[0]
                            elif isExist(pathrobloxcheck[1]):
                                pathtoroblox = pathrobloxcheck[1]
                            else:
                                print("> [*] Unfound Roblox folder.")
                            if pathtoroblox:
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
                    except Exception as e:
                        DebugLog(debugpath,e)
                        print(f'> [*] Something is wrong! Saved ERROR to DebugLog >> {debugpath}')
                    input('Press enter to countinue...')
            else:
                updatetext = f'''You are using an old version of GetaFPSUnlocker, please download the latest version of GetaFPSUnlocker to be able to apply bug fixes and add new features!
    ==>> Your Version: {versions["current"]}
    ==>> Latest Version: {versions["latest"]}
    Download the latest version at GITHUB: https://github.com/Geta1005/GetaFPSUnlocker/releases
    '''
                print(updatetext)
                input('Press enter to countinue...')
        except Exception as e:
            DebugLog(debugpath,e)
            print(f'> [*] Something is wrong! Saved ERROR to DebugLog >> {debugpath}')
            input('Press enter to countinue...')
else:
    print("> [*] Your OS is not supported! (ONLY WINDOWS OS)")
    input('Press enter to countinue...')
    sys.exit(0)
