from datetime import datetime, timedelta
import datetime
from pynput.keyboard import Listener



def Convert_String_DateTime(list):
    F = datetime.time(0, 0, 0)
    T = datetime.time(0, 0, 0)
    D = datetime.time(0, 0, 0)
    I = datetime.time(0, 0, 0)
    S = datetime.time(0, 0, 0)
    for s in list:
        if s[0] == 'F':
            s = s.replace('F', '')
            h, m = s.split(":")
            h = int(h)
            m = int(m)
            F = datetime.time(h, m, 0)
        if s[0] == 'T':
            s = s.replace('T', '')
            h, m = s.split(":")
            h = int(h)
            m = int(m)
            T = datetime.time(h, m, 0)
        if s[0] == 'D':
            s = s.replace('D', '')
            m = int(s)
            D = datetime.time(int(m/60), m%60, 0)
        if s[0] == 'I':
            s = s.replace('I', '')
            m = int(s)
            I = datetime.time(int(m/60), m%60, 0)
        if s[0] == 'S':
            s = s.replace('S', '')
            m = int(s)
            S = datetime.time(int(m/60), m%60, 0)
    return (F, T, D, I, S)
def ReadFile(f):
    
    using_time = []
    lines = f.read().splitlines()
    for line in lines:
        using_time.append(Convert_String_DateTime(line.split(" ")))
    return using_time
def Check_using_time_for_children(using_time):
    curtime = datetime.datetime.now().time()
    for t in using_time: 
        if curtime >= t[0] and curtime <= t[1]:
            return True 
    return False 
def Find_Next_Time(using_time):
    curtime = datetime.datetime.now().time()
    for t in using_time: 
        if t[0] >= curtime:
            return t[0]
    return "Next day"   
def Find_How_Many_Minute_Left(using_time):
    curtime = datetime.datetime.now().time()
    for t in using_time: 
        if curtime >= t[0] and curtime <= t[1]:
            return 60 * t[1].hour + t[1].minute - 60 * curtime.hour - curtime.minute
def Time_End(using_time):
    curtime = datetime.datetime.now().time()
    for t in using_time: 
        if curtime >= t[0] and curtime <= t[1]:
            return t[1]






 



    
      
    
    #print(using_time)
    #print(Find_How_Many_Minute_Left(using_time))
    #print(Find_Next_Time(using_time))
    # Check_using_time_for_children(datetime.datetime.now(), using_time)

def To_Second(time):
    return time.hour*3600+time.minute*60+time.second

def Check_In_Schedule():
    curtime = To_Second(datetime.datetime.now().time())
    k = int(curtime/60)
    if (curtime-28)/60 <= k and k < (curtime-2)/60:
        return True
    else:
        return False