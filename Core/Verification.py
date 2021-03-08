from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re

def PasswrdVerify(usr,passwd):
    global driver   
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    time.sleep(1)
    username = driver.find_element_by_name("username")
    passwrd = driver.find_element_by_name("password")
    username.send_keys(usr)
    passwrd.send_keys(passwd+Keys.ENTER)
    time.sleep(5)
    expectedUrl= driver.current_url

    if (driver.find_elements_by_id("slfErrorAlert")):
        print("\033[91mPassword or Username error\033[0m")
        driver.close()
        return "Password Error"
            
    elif (re.findall(r'https://www.instagram.com/accounts/login/two\.*?',expectedUrl)) :
        print("\033[91mOTP Required\033[0m")
        return "OTP"
    elif (re.findall(r'instagram.com/accounts/\.*?',expectedUrl)):
        print("\033[91mDirect Login\033[0m")
        driver.close()
        return "Success"
    elif (re.findall(r'instagram.com\.*?',expectedUrl)):
        print("\033[91mDirect Login\033[0m")
        driver.close()
        return "Success"
def OTP(x):
    driver.find_element_by_name("verificationCode").send_keys(Keys.CONTROL+'a')
    driver.find_element_by_name("verificationCode").send_keys(Keys.DELETE)
    otp = driver.find_element_by_name("verificationCode")
    otp.send_keys(x,Keys.ENTER)
    time.sleep(3)
    if (re.findall(r'instagram.com/accounts/login/two_factor\.*?',driver.current_url)):
        print("\033[91mWrong OTP\033[0m")
        return "Error"
    elif(re.findall(r'instagram.com\.*?',driver.current_url)):
        return "Success"
    
