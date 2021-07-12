'''
Made by Arpit.

Python bot to attend google meets.


What it does?
1. Joins Meet.
2. Mutes Mic and Disables camera.
3.Sends a message that "Pls mark me Present."
3. Include voice recognition to check if name called and then response.(in future)
4.You tell what more to add ¯\_ʘ‿ʘ_/¯


Packages required:
See the import statements xD

'''

#Enter you meeting link.
link = ''
#Enter your email id.
email = ''
#Enter you email password.
password = ''

#You can enter using secure environment and adding secret variable using os.getenv('pass') or you may host it locally on your computer!

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
import time
import Xlib
from pynput.keyboard import Key, Controller
from datetime import datetime
#import pandas as pd
#import random

#Setting up browser.
firefox_options = Options()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--private")
driver = webdriver.Firefox(options=firefox_options)
opt = Options() 

opt.add_argument('--disable-blink-features=AutomationControlled') 

opt.add_argument('--start-maximized') 

opt.add_experimental_option("prefs", { 

    "profile.default_content_setting_values.media_stream_mic": 1, 

    "profile.default_content_setting_values.media_stream_camera": 1, 

    "profile.default_content_setting_values.geolocation": 0, 

    "profile.default_content_setting_values.notifications": 1
}) 

#Finds current time.
def findTime():
    now = datetime.now().time()
    return (now.hour,now.minute)

#Press and release keyboard key.
def press_and_release(key):
    keyboard.press(key)
    keyboard.release(key)
    
#Looks whether the time has come to join the class.
def lookup_time():
  findTime()
  if now == "7:40":
    Glogin()
    driver.get(link)
    turnOffMicCam()
    #AskToJoin()
    #Ask to join and join now have same xpaths.
    joinNow()
    time.sleep(65)#5 seconds taken extra just to avoid error, computer is very fasty boi.
    background_process()
  else:
    background_process()
    
  
#To keep it always running.   
def background_process():
    lookup_time()
    time.sleep(1)


#Gmail Login process.

def Glogin(): 

    

    driver.get( 

        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ') 



    # input Gmail id

    driver.find_element_by_id("identifierId").send_keys(email) 

    driver.find_element_by_id("identifierNext").click() 

    driver.implicitly_wait(10) 

  

    # input Password 

    driver.find_element_by_xpath( 

        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password) 

    driver.implicitly_wait(10) 

    driver.find_element_by_id("passwordNext").click() 

    driver.implicitly_wait(10) 



    # go to google home page 

    driver.get('https://google.com/') 

    driver.implicitly_wait(100) 

  

  

def turnOffMicCam(): 

    # turn off Microphone.

    time.sleep(2) 

    driver.find_element_by_xpath( 

        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click() 

    driver.implicitly_wait(3000) 

  

    # turn off camera.

    time.sleep(1) 

    driver.find_element_by_xpath( 

        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click() 

    driver.implicitly_wait(3000) 

  

  

def joinNow(): 

    # Join meet 

    print(1) 

    time.sleep(5) 

    driver.implicitly_wait(2000) 

    driver.find_element_by_css_selector( 

        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click() 
        
    print(1) 
    #Following code is for sending message.
    for i in range(0,40):
        press_and_release(Key.tab)
        elem = driver.switch_to.active_element
        class_name = elem.get_attribute("class")
		#the following block of strings are the respective ids for the people and message icon within gmeet so this could vary.
        if "uArJ5e UQuaGc kCyAyd" in class_name and not passed_everyone: passed_everyone = True
        elif "uArJ5e UQuaGc kCyAyd" in class_name:
            press_and_release(Key.enter)
            time.sleep(1)
            break
        time.sleep(0.4)

    time.sleep(2)
    keyboard.type("Ma'am pls mark me present!")
    time.sleep(1)
    press_and_release(Key.enter)

    keyboard.press(Key.ctrl)
    keyboard.press('e')
    keyboard.release(Key.ctrl)
    keyboard.release('e')


def AskToJoin(): 

    # Ask to Join meet 

    time.sleep(5) 

    driver.implicitly_wait(2000) 

    driver.find_element_by_css_selector( 

        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click() 


while True: background_process()