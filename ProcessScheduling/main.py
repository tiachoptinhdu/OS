from ProcessScheduling import FCFS, RR, SJF, Process, PQ
import copy
from queue import PriorityQueue 

        

with open('Input.txt') as f:
    n, quantum_time = list(map(int, f.readline().split(" ")))
    list_process = []
    for line in f: 
        Id, ArrivalTime, Brust, Piority = line.split(" ")
        p = Process(Id, ArrivalTime, Brust, Piority)
        list_process.append(p)


FCFS(list_process)
PQ(list_process)
RR(list_process, quantum_time)
SJF(list_process)


    
                    

                



