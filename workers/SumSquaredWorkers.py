import threading
class SumSquaredWorker(threading.Thread):
    def __init__(self, n):
        super(SumSquaredWorker, self).__init__()
        self.n = n
        self.start()

    def sumSquared(self):
        total = sum(i * i for i in range(1, self.n + 1))
        print(f"Sum of squares up to {self.n}: {total}")
    
    def run(self):
        self.sumSquared()