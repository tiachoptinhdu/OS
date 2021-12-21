import copy
from queue import PriorityQueue

class Process:
    def __init__(self, Id, ArrivalTime, Burst, Piority):
        self.Id = Id 
        self.ArrivalTime = int(ArrivalTime)
        self.Burst = int(Burst) 
        self.Piority = int(Piority)
        self.Visited = False
    def __lt__(self, other):
        return False
    def __le__(self, other):
        return False 

def FCFS(list_process):
    # deep copy process 
    deep_copy_list_process = copy.deepcopy(list_process)
    deep_copy_list_process.sort(key = lambda x: x.ArrivalTime)
    # Luu string tien trinh chay
    Scheduling_chart = ""

    #con trỏ thời gian
    curtime = 0
    # list để lưu TT WT theo thứ tự list process
    TT = []
    WT = []
    for i, process in enumerate(deep_copy_list_process):
        if i == 0: # Trường hợp process đầu tiên được chạy
            Scheduling_chart+=(str(process.ArrivalTime) + "~")
            Scheduling_chart+=process.Id
            Scheduling_chart+=("~" + str(process.ArrivalTime + process.Burst))
            curtime = process.ArrivalTime + process.Burst
            WT.append(0)
            TT.append(process.Burst)
        else: 
            if process.ArrivalTime < curtime:
                Scheduling_chart+="~" + process.Id
                Scheduling_chart+=("~" + str(curtime + process.Burst))
                WT.append(curtime - process.ArrivalTime)
                TT.append(WT[-1]+process.Burst)
                curtime += process.Burst
            else: 
                curtime = process.ArrivalTime
                Scheduling_chart+=("~-~" + str(process.ArrivalTime) + "~")
                Scheduling_chart+=process.Id
                Scheduling_chart+=("~" + str(process.ArrivalTime + process.Burst))
                WT.append(curtime - process.ArrivalTime)
                TT.append(WT[-1]+process.Burst)
                curtime = process.ArrivalTime + process.Burst
    with open("FCFS.txt", "w") as f:
        f.write(f"Scheduling chart: {Scheduling_chart} \n")
        for i, process in enumerate(deep_copy_list_process):
            f.write(f'{process.Id}: TT={TT[i]} WT = {WT[i]} \n')
        f.write(f"Average: TT={sum(TT) / len(TT)}   WT= {sum(WT) / len(WT)}\t")
def RR(list_process, quantum_time):
    deep_copy_list_process = copy.deepcopy(list_process)
    deep_copy_list_process.sort(key = lambda x: x.ArrivalTime)
    list_process_clone = copy.deepcopy(deep_copy_list_process)
    Scheduling_chart = ""
    curtime = 0
    TT = [0]*len(deep_copy_list_process)
    WT = [0]*len(deep_copy_list_process)
    Queue = []
    Queue.append(deep_copy_list_process[0])
    k = 0
    check = False  
    while Queue != []:
        process = Queue.pop(0)
        process.Visited = True 
        index = deep_copy_list_process.index(process)
        if k == 0:
            Scheduling_chart+=(str(process.ArrivalTime))
            curtime = process.ArrivalTime
            WT[0] = 0
            k = 1
        if check == True: 
            if check == True:
                Scheduling_chart+=  "~-~"
                Scheduling_chart+= (str(process.ArrivalTime)+"~")
                Scheduling_chart+=str(process.Id)
                Scheduling_chart += ("~"+ str(curtime + process.Burst))
        Scheduling_chart+=("~"+process.Id)
        if process.Burst < quantum_time:
            Scheduling_chart+= ("~"+str(curtime + process.Burst))
            curtime += process.Burst
            process.Burst = 0
        else:
            Scheduling_chart+= ("~"+str(curtime+quantum_time))
            curtime += quantum_time
            process.Burst -= quantum_time

        if process.Burst == 0: 
            WT[index] = curtime - list_process_clone[index].ArrivalTime - list_process_clone[index].Burst
            TT[index] = curtime - list_process_clone[index].ArrivalTime
        deep_copy_list_process[index] = process 
        for i, p in enumerate(deep_copy_list_process):
            if i != index and p.Burst > 0 and p.Visited == False and p.ArrivalTime <= curtime:
                Queue.append(p)
                p.Visited = True 
        check = False 
        if deep_copy_list_process[index].Burst > 0:
            Queue.append(deep_copy_list_process[index])

        if Queue == []:
            for i, p in enumerate(deep_copy_list_process):
                if p.Visited == False:
                    Queue.append(p)
                    p.Visited = True 
                    curtime = p.ArrivalTime 
                    check = True 
        
    with open("RR.txt", "w") as f:
        f.write(f"Scheduling chart: {Scheduling_chart} \n")
        for i, process in enumerate(deep_copy_list_process):
            f.write(f'{process.Id}: TT={TT[i]} WT = {WT[i]} \n')
        f.write(f"Average: TT={sum(TT) / len(TT)}   WT= {sum(WT) / len(WT)}\t")
def SJF(list_process):
    deep_copy_list_process = copy.deepcopy(list_process)
    deep_copy_list_process.sort(key = lambda x: x.ArrivalTime)
    Scheduling_chart = ""
    curtime = 0
    TT = [0]*len(deep_copy_list_process)
    WT = [0]*len(deep_copy_list_process)
    Queue = PriorityQueue()
    
    #Bỏ các Process có thời gian Arrival Time giống nhau vào Queue
    for p in deep_copy_list_process:
            if p.Visited == False and p.ArrivalTime == deep_copy_list_process[0].ArrivalTime: 
                Queue.put((p.Burst, p))
                p.Visited = True
    

    k = 0
    check = False
    while Queue.empty() == False:
        process = Queue.get()[1]
        index = deep_copy_list_process.index(process)
        if k == 0:
            curtime = process.ArrivalTime
            Scheduling_chart += (str(process.ArrivalTime)+"~")
            Scheduling_chart+= process.Id 
            Scheduling_chart += ("~" + str(curtime+process.Burst))
            k = 1
            WT[0] = 0
            TT[0] = WT[-1]+process.Burst
        else:
            if check == True:
                Scheduling_chart+=  "~-~"
                Scheduling_chart+= (str(process.ArrivalTime)+"~")
                Scheduling_chart+=str(process.Id)
                Scheduling_chart += ("~"+ str(curtime + process.Burst))
            else:
                Scheduling_chart+=  ("~" + process.Id)
                Scheduling_chart += ("~"+ str(curtime + process.Burst))
            WT[index] = (curtime-process.ArrivalTime)
            TT[index] = (WT[index]+process.Burst)
        curtime = curtime+process.Burst
        process.Visited = True
        for p in deep_copy_list_process:
            if p.Visited == False and p.ArrivalTime < curtime: 
                Queue.put((p.Burst, p))
                p.Visited = True
        check = False 
        if Queue.empty() == True:
            for p in deep_copy_list_process:
                if p.Visited == False:
                    curtime = p.ArrivalTime
                    Queue.put((p.Burst, p))
                    check = True
                    break 
    with open("SJF.txt", "w") as f:
        f.write(f"Scheduling chart: {Scheduling_chart} \n")
        for i, process in enumerate(deep_copy_list_process):
            f.write(f'{process.Id}: TT={TT[i]} WT = {WT[i]} \n')
        f.write(f"Average: TT={sum(TT) / len(TT)}   WT= {sum(WT) / len(WT)}\t")
def PQ(list_process):
    fake_list_process = copy.deepcopy(list_process)
    fake_list_process.sort(key=lambda x: x.ArrivalTime)            
    deep_copy_list_process = copy.deepcopy(list_process)
    deep_copy_list_process.sort(key = lambda x: x.ArrivalTime)

    end = deep_copy_list_process[0].ArrivalTime + sum(x.Burst for x in deep_copy_list_process)
    Scheduling_chart = ""
    TT = [0]*len(deep_copy_list_process)
    WT = [0]*len(deep_copy_list_process)
    Queue = PriorityQueue()

    process = Process(0,0,0,0)
    start = deep_copy_list_process[0].ArrivalTime
    for time in range(start, end + 1): 
        # Them vao cac process voi ArrivalTime = time hien tai 
        for p in deep_copy_list_process:
            if p.Visited == False and p.ArrivalTime == time: 
                Queue.put((p.Piority, p))
                p.Visited = True 
        
        #Lay process dau tien
        if time == start: 
            process = Queue.get()[1]
            Scheduling_chart = str(process.ArrivalTime)+"~"+process.Id+"~" 
        
        if time == end:
            Scheduling_chart+=str(time)
            for i, p in enumerate(deep_copy_list_process):
                        if p.Id == process.Id:
                            index = i
            TT[index] = time - deep_copy_list_process[index].ArrivalTime
            WT[index] = TT[index] - fake_list_process[index].Burst
            break
        if Queue.empty() == False: # Kiem tra Queue
            if process.Piority > Queue.queue[0][1].Piority: # Xem Queue có phần tử tốt hơn không
                if process.Burst != 0:
                    Queue.put((process.Piority, process)) 
                else: 
                    for i, p in enumerate(deep_copy_list_process):
                        if p.Id == process.Id:
                            index = i
                    TT[index] = time - deep_copy_list_process[index].ArrivalTime 
                    WT[index] = TT[index] - fake_list_process[index].Burst

                process = Queue.get()[1]
                Scheduling_chart += (str(time)+"~"+process.Id+"~")
            else: 
                if process.Burst == 0:
                    for i, p in enumerate(deep_copy_list_process):
                        if p.Id == process.Id:
                            index = i
                            
                    TT[index] = time - deep_copy_list_process[index].ArrivalTime
                    WT[index] = TT[index] - fake_list_process[index].Burst
    
                    process = Queue.get()[1]
                    Scheduling_chart += (str(time)+"~"+process.Id+"~")
        else:
            if process.Burst == 0:
                for i, p in enumerate(deep_copy_list_process):
                    if p.Id == process.Id:
                        index = i
                TT[index] = time - deep_copy_list_process[index].ArrivalTime
                WT[index] = TT[index] - fake_list_process[index].Burst

                Scheduling_chart += (str(time)+"~"+process.Id+"~-~")

        process.Burst -= 1

    with open("Piority.txt", "w") as f:
        f.write(f"Scheduling chart: {Scheduling_chart} \n")
        for i, process in enumerate(deep_copy_list_process):
            f.write(f'{process.Id}: TT={TT[i]} WT = {WT[i]} \n')
        f.write(f"Average: TT={sum(TT) / len(TT)}   WT= {sum(WT) / len(WT)}\t")        
