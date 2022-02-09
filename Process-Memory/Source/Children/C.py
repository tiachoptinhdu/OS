import multiprocessing
import datetime
import time
import os
from Time import Check_using_time_for_children, Find_How_Many_Minute_Left, Find_Next_Time, ReadFile, Time_End, Check_In_Schedule
from Process import  Count_15_sec, Check_1_min_left, KeyListener, ScreenCapture, CaptureAndKeyListener



def Parent():
    check_process = False 
    count = 0
    using_time = ReadFile(open("C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/time.txt", 'r'))
    while True:
        if Check_In_Schedule() == True:
            using_time = ReadFile(open("C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/time.txt", 'r'))
        print("Input your Password")
        password = input("Password:")
        if password == "Parent":
            if check_process == True:
                p1.terminate()
            print("Hello Parent you have 60min!!")
            time.sleep(3600) #Sleep 60 minute 
            continue 
        else:
            if Check_using_time_for_children(using_time) == False:
                print(f"Raise: The next time you can use computer: {Find_Next_Time(using_time)}")
                datetime_start = datetime.datetime.now()
                if check_process == False:
                    p1 = multiprocessing.Process(target=Count_15_sec, args=(datetime_start, ))
                    p1.start()
                    check_process = True 
            else:
                if password != "Children":
                    count += 1
                    if count > 3:  
                        print("Bạn sẽ bị cấm 10 phút")
                        time.sleep(600)
                        os.system("shutdown /s /t 1")  #Shutting down OS
                else:
                    if check_process == True:
                        p1.terminate()
                    print("Hello Children")
                    if Check_In_Schedule() == True:
                        using_time = ReadFile(open("C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/time.txt", 'r'))
                    print(f"Time Left: {Find_How_Many_Minute_Left(using_time)}")
                    time_end = Time_End(using_time)
                    time_end = datetime.datetime.combine(datetime.date.today(), time_end)
                    p2 = multiprocessing.Process(target=Check_1_min_left, args=(time_end,))
                    p3 = multiprocessing.Process(target=CaptureAndKeyListener)
                    p2.start()
                    p3.start()
                    while True:
                        if Check_In_Schedule() == True:
                            if using_time != ReadFile(open("C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/time.txt", 'r')):
                                using_time = ReadFile(open("C:/Users/ASUS/OneDrive - VNU-HCMUS/Desktop/OneDrive - VNU-HCMUS/Desktop/ShareFolder/time.txt", 'r'))
                                print(f"Time Left: {Find_How_Many_Minute_Left(using_time)}")
                                time_end = Time_End(using_time)
                                time_end = datetime.datetime.combine(datetime.date.today(), time_end)
                                p2.terminate()
                                p3.terminate()
                                p2 = multiprocessing.Process(target=Check_1_min_left, args=(time_end,))
                                p3 = multiprocessing.Process(target=CaptureAndKeyListener)
                                p2.start()
                                p3.start()

if __name__ == "__main__":
    Parent()






                    

                    
                    
                
                    



                


                   





