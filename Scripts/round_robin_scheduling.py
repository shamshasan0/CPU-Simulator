from resource_allocation_graph import ResourceAllocationGraph

def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = bt[:]
    time = 0
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    time += quantum
                    rem_bt[i] -= quantum
                else:
                    time += rem_bt[i]
                    wt[i] = time - bt[i]
                    rem_bt[i] = 0
        if done:
            break

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt, quantum)
    findTurnAroundTime(processes, n, bt, wt, tat)

    print("Process ID | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"   {processes[i]}     |     {bt[i]}     |      {wt[i]}       |      {tat[i]}")
    print("Average waiting time =", total_wt / n)
    print("Average turn around time =", total_tat / n)

def test_deadlock_scenario():
    rag = ResourceAllocationGraph(3, 2)
    rag.available = [2, 2]  # Initial resources available

    rag.allocate_resources(0, [1, 1])  # Process 0 allocates [1, 1]
    rag.allocate_resources(1, [1, 0])  # Process 1 allocates [1, 0]
    rag.request_resources(2, [1, 1])  # Process 2 requests [1, 1]

    print("\nDeadlock Detection:")
    if rag.detect_deadlock():
        rag.handle_deadlock()

    processes = [1, 2, 3]
    burst_time = [6, 4, 3]
    quantum = 2
    findavgTime(processes, len(processes), burst_time, quantum)

if __name__ == "__main__":
    test_deadlock_scenario()
