import os

while(True):
    if(os.path.exists("Verification.txt")):
        with open("Verification.txt",'r') as H:
            print(H.read())
        break
    else:
        print(1)