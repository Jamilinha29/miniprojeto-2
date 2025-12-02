from src.buffer import BoundedBuffer
from src.produtor import producer


def test_producer_basic():
    buf = BoundedBuffer(capacity=10)
    producer(buf, 1, 5)

    assert buf.total_produced == 5
    assert buf.size() == 5

    # verificar ordem e conteúdo dos itens produzidos
    items = [buf.consume() for _ in range(5)]
    expected = [(1, i) for i in range(5)]
    assert items == expected
