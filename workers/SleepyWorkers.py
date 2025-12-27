import threading
import time

class SleepyWorker(threading.Thread):
    def __init__(self, seconds):
        super(SleepyWorker, self).__init__()
        self.seconds = seconds
        self.start()

    def sleepALittle(self):
        time.sleep(self.seconds)
    
    def run(self):
        self.sleepALittle()