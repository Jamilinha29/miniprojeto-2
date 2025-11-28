import threading
from collections import deque
import time

class BoundedBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.space = threading.Semaphore(capacity)
        self.items = threading.Semaphore(0)
        self.mutex = threading.Lock()
        self.total_produced = 0
        self.total_consumed = 0
        self.wait_prod = 0.0
        self.wait_cons = 0.0

    def produce(self, item):
        t0 = time.time()
        self.space.acquire()
        self.wait_prod += time.time() - t0
        with self.mutex:
            self.queue.append(item)
            self.total_produced += 1
        self.items.release()

    def consume(self):
        t0 = time.time()
        self.items.acquire()
        self.wait_cons += time.time() - t0
        with self.mutex:
            item = self.queue.popleft()
            self.total_consumed += 1
        self.space.release()
        return item

    def size(self):
        with self.mutex:
            return len(self.queue)
