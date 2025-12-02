import time
import pytest
from src.buffer import BoundedBuffer


@pytest.fixture(params=[1, 2, 5])
def buffer(request):
    """Fixture que cria um `BoundedBuffer` com capacidades diferentes.

    Isso permite reutilizar o mesmo teste para múltiplas capacidades.
    """
    return BoundedBuffer(capacity=request.param)


def test_produce_consume_basic(buffer):
    # produzir até a capacidade e verificar comportamento FIFO
    cap = buffer.capacity
    for i in range(cap):
        buffer.produce(f"item{i}")

    assert buffer.size() == cap
    assert buffer.total_produced == cap

    for i in range(cap):
        assert buffer.consume() == f"item{i}"

    assert buffer.total_consumed == cap
    assert buffer.size() == 0


def test_history_and_metrics():
    buf = BoundedBuffer(capacity=3)
    buf.produce(1)
    time.sleep(0.001)
    buf.produce(2)
    time.sleep(0.001)
    buf.consume()

    # history lists should have entries
    assert len(buf.history_time) >= 3
    assert len(buf.history_size) >= 3
    # metrics should reflect operations
    assert buf.total_produced == 2
    assert buf.total_consumed == 1

