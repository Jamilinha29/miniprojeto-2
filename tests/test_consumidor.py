import threading
import time
from src.buffer import BoundedBuffer
from src.consumidor import consumer
from src.produtor import producer


def test_consumer_basic():
    buf = BoundedBuffer(capacity=10)
    # preencher buffer com itens conhecidos
    for i in range(5):
        buf.produce(("p", i))

    consumer(buf, 0, 5)
    assert buf.total_consumed == 5
    assert buf.size() == 0


def test_consumer_blocks_until_items_available():
    buf = BoundedBuffer(capacity=5)

    # iniciar consumidor que irá tentar consumir 5 itens (vai bloquear)
    t = threading.Thread(target=consumer, args=(buf, 0, 5))
    t.start()

    # dar tempo para o consumidor tentar adquirir (bloquear em empty)
    time.sleep(0.01)

    # produzir os itens que o consumidor espera
    producer(buf, 1, 5)

    t.join(timeout=2)
    assert not t.is_alive()
    assert buf.total_consumed == 5
