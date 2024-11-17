def findWaitingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)

    print("Process ID | Burst Time | Waiting Time | Turnaround Time")
    
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"   {processes[i]}     |     {bt[i]}     |      {wt[i]}       |      {tat[i]}")

    print("\nAverage Waiting Time =", total_wt / n)
    print("Average Turnaround Time =", total_tat / n)

if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]
    
    findavgTime(processes, n, burst_time)
