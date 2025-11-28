import threading
from collections import deque
import time

class BufferLimitado:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.fila = deque()
        self.espaco = threading.Semaphore(capacidade)
        self.itens = threading.Semaphore(0)
        self.mutex = threading.Lock()
        self.total_produzido = 0
        self.total_consumido = 0
        self.tempo_espera_prod = 0.0
        self.tempo_espera_cons = 0.0

    def produzir(self, item):
        t0 = time.time()
        self.espaco.acquire()
        self.tempo_espera_prod += time.time() - t0
        with self.mutex:
            self.fila.append(item)
            self.total_produzido += 1
        self.itens.release()

    def consumir(self):
        t0 = time.time()
        self.itens.acquire()
        self.tempo_espera_cons += time.time() - t0
        with self.mutex:
            item = self.fila.popleft()
            self.total_consumido += 1
        self.espaco.release()
        return item

    def tamanho(self):
        with self.mutex:
            return len(self.fila)
