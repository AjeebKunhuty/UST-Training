import time
import threading
from workers.SleepyWorkers import SleepyWorker
from workers.SumSquaredWorkers import SumSquaredWorker

def main():
    current_threads = []    # List to keep track of threads
    startTime = time.time()
    for i in range(5):
        t1 = SumSquaredWorker((i+1)*1000000)    # Create thread, args as tuple
        current_threads.append(t1)  # Add thread to the list
    
    # Wait for all threads to complete
    for t in current_threads:
        t.join()
    
    endTime = time.time()
    print(f"Total time taken: {round(endTime - startTime,1)} seconds")

    current_threads = []
    startTime = time.time()
    for i in range(1, 6):
        t2 = SleepyWorker(i)
        current_threads.append(t2)
    
    for t in current_threads:
        t.join()
    
    endTime = time.time()
    print(f"Total time taken for sleep: {round(endTime - startTime,1)} seconds")

if __name__ == "__main__":
    main()