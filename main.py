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
pathtoroblox = pathtoprogram86+"/Roblox"
configsfolderpath = pathtoprogram86+"/GetaTool"
configspath = pathtoprogram86+"/GetaTool"+'/GetaTool_configs.json'
debugpath = pathtoprogram86+"/GetaTool"+'/DebugLog.txt'
source_path = replace(currentPath,'\\','/')
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
destination_path = os.path.join(startup_folder, os.path.basename(source_path))
version_url = 'https://raw.githubusercontent.com/Geta1005/GetaFPSUnlocker/main/version.txt'
versions = {
    'current': '0.0.5',
    'latest': ''
}
robloxfolder = None
runningStartup = False

if not is_admin():
    print('> [*] GetaFPSUnlocker needs to Run as administrator')
    input('Press enter to countinue...')
else:
    try:
        getlatestVer = requests.get(version_url)
        versions['latest'] = str(getlatestVer.text).replace('\n','')
        if versions['current'] == versions['latest']:
            try:
                if not isExist(configsfolderpath):
                    createFolder(configsfolderpath)
                if not isExist(configspath):
                    newData = {
                        "enabled": False,
                        "startup": False
                    }
                    json_write(configspath,newData)
                if not isExist(debugpath):
                    file = open(debugpath, 'w')
                    file.close()
                    DebugLog(debugpath,"Created DebugLog.txt")
            except Exception as e:
                runningStartup = True
                DebugLog(debugpath,e)
                print(f'> [*] Something is wrong! Saved ERROR to DebugLog >> {debugpath}')
                input('Press enter to countinue...')
            try:
                if 'Start-up' in currentPath.split('\\'):
                    runningStartup = True
                if runningStartup:
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
                                json_write(jsonpath,newData)
            except Exception as e:
                DebugLog(debugpath,e)
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
                    print('---------------------------------------------\n> [Path] Configs: '+replace(configspath,'/','\\')+'\n> [Path] DebugLog: '+replace(debugpath,'/','\\')+'\n> [Path] Start-up Folder: '+startup_folder)
                    select = input(f'---------------------------------------------\n> [0] Close\n> [1] Unlock FPS\n> [2] Set FPS to default\n> [3] Start-up Toggle\n---------------------------------------------\n>>>>> ')
                    if select == '0':
                        break
                    elif select == '1':
                        print('> [-] Checking...')
                        time.sleep(random.randint(1,20)/10)
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
                        time.sleep(random.randint(1,20)/10)
                        print('> [*] FPS unlocked successfully, please rejoin the game to apply.')
                        robloxTab = checkRobloxTab()
                        if robloxTab:
                            closeRoblox = input('[Y/N] Close Roblox?\n>>>>> ')
                            if closeRoblox.lower() == 'y':
                                robloxTab.close()
                                print('[*] Closed roblox tab')
                    elif select == '2':
                        print('> [-] Checking...')
                        time.sleep(random.randint(1,20)/10)
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
                        time.sleep(random.randint(1,20)/10)
                        print('> [*] FPS has been set to default, please rejoin the game to apply')
                        robloxTab = checkRobloxTab()
                        if robloxTab:
                            closeRoblox = input('[Y/N] Close Roblox?\n>>>>> ')
                            if closeRoblox.lower() == 'y':
                                robloxTab.close()
                                print('> [-] Closed roblox tab')
                    elif select == '3':
                        configs = json_load(configspath)
                        if configs['startup'] == False:
                            select2 = input('[Y/N] Turn on Start-up?\n>>>>> ')
                            if select2.lower() == 'y':
                                configs["startup"] = True
                                json_write(configspath,configs)
                                print('> [*] Settings saved')
                                if isExist(replace(destination_path,'\\','/')):
                                    os.remove(replace(destination_path,'\\','/'))
                                try:
                                    if not isExist(source_path):
                                        print(f"> [*] File not found (GetaFPSUnlocker.exe)")
                                    else:
                                        try: 
                                            shutil.copy2(source_path, destination_path)
                                            print(f"> [*] Saved file to Start-up Folder")
                                        except Exception as e:
                                            DebugLog(debugpath,e)
                                            print(f"> [*] Failed to save the file to the Start-up folder")
                                except Exception as e:
                                    DebugLog(debugpath,e)
                        elif configs['startup'] == True:
                            select2 = input('[Y/N] Turn off Start-up?\n>>>>> ')
                            if select2.lower() == 'y':
                                configs["startup"] = False
                                json_write(configspath,configs)
                                print('> [*] Settings saved')
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
