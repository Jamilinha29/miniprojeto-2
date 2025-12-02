import threading
from collections import deque
import time
import logging


class BoundedBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.space = threading.Semaphore(capacity)
        self.items = threading.Semaphore(0)
        self.mutex = threading.Lock()

        # Métricas
        self.total_produced = 0
        self.total_consumed = 0
        self.wait_prod = 0.0
        self.wait_cons = 0.0

        # Histórico para o gráfico
        self.history_size = []
        self.history_time = []
        self.start_time = time.time()
        self.logger = logging.getLogger(__name__)

    def produce(self, item):
        t0 = time.time()

        self.space.acquire()
        self.wait_prod += time.time() - t0

        with self.mutex:
            self.queue.append(item)
            self.total_produced += 1

            # log em nível debug para acompanhar produção (não muito verboso)
            if self.logger.isEnabledFor(10):
                self.logger.debug("Produced item: %s; size=%s", item, len(self.queue))

            # registrar histórico para o gráfico
            t = time.time() - self.start_time
            self.history_size.append(len(self.queue))
            self.history_time.append(t)

        self.items.release()

    def consume(self):
        t0 = time.time()

        self.items.acquire()
        self.wait_cons += time.time() - t0

        with self.mutex:
            item = self.queue.popleft()
            self.total_consumed += 1

            # registrar histórico para o gráfico
            t = time.time() - self.start_time
            self.history_size.append(len(self.queue))
            self.history_time.append(t)

            if self.logger.isEnabledFor(10):
                self.logger.debug("Consumed item: %s; size=%s", item, len(self.queue))

        self.space.release()
        return item

    def size(self):
        with self.mutex:
            return len(self.queue)
