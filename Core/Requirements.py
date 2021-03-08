import os
import sys

RED = "\033[91m"
RESET = "\033[0m"
YELLOW = "\033[93m"

def hasPHP():
    php = os.popen("php -v 2>temp").read()
    if (php == ''):
            print(RED+"\n[X]"+YELLOW+" PHP not installed."+RED+"\nExiting...\n"+RESET)
            sys.exit() 
    else:
        return True

def hasngrok():
    ngrok = os.popen("ngrok 2>temp").read()
    if (ngrok == ''):
            print(RED+"\n[X]"+YELLOW+" Ngrok not installed."+RED+"\nExiting...\n"+RESET)
            sys.exit() 
    else:
        return True

def haschrome():
    chrome = os.popen("chromedriver -v 2>temp").read()
    if (chrome ==''):
        print(RED+"\n[X]"+YELLOW+" Chrome-Driver not installed or set in the path."+RED+"\nExiting...\n"+RESET)
        sys.exit()
    else:
        return True

def hasXterm():
    if os.name == 'nt':
        return True
    else:
        xterm = os.popen("xterm -v 2>temp").read()
        if xterm == '':
            print(RED+"\n[X]"+YELLOW+" Xterm not installed. Try:apt install xterm "+RED+"\nExiting...\n"+RESET)
            sys.exit()
        else:
            return True