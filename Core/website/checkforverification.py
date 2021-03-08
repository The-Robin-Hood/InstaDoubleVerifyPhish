import os
import time

while(True):
    if(os.path.exists("Verification.txt")):
        time.sleep(1.5)
        with open("Verification.txt",'r') as H:
            print(H.read())
        break
    else:
        print(1)
