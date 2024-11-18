class ResourceAllocationGraph:
    def __init__(self, num_processes, num_resources):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self.allocation = [[0] * num_resources for _ in range(num_processes)]
        self.request = [[0] * num_resources for _ in range(num_processes)]
        self.available = [0] * num_resources
        self.finished = [False] * num_processes

    def request_resources(self, process_id, resources):
        self.request[process_id] = resources

    def allocate_resources(self, process_id, resources):
        self.allocation[process_id] = resources
        for i in range(self.num_resources):
            self.available[i] -= resources[i]

    def release_resources(self, process_id):
        for i in range(self.num_resources):
            self.available[i] += self.allocation[process_id][i]
            self.allocation[process_id][i] = 0

    def detect_deadlock(self):
        work = self.available[:]
        finish = [False] * self.num_processes

        while True:
            progress_made = False
            for i in range(self.num_processes):
                if not finish[i]:
                    if all(self.request[i][j] <= work[j] for j in range(self.num_resources)):
                        finish[i] = True
                        progress_made = True
                        for j in range(self.num_resources):
                            work[j] += self.allocation[i][j]
                        break

            if not progress_made:
                deadlocked = [i for i in range(self.num_processes) if not finish[i]]
                if deadlocked:
                    print(f"Deadlock detected! Deadlocked processes: {deadlocked}")
                    return True
                return False

    def handle_deadlock(self):
        print("Handling deadlock by releasing resources from Process 0.")
        self.release_resources(0)
