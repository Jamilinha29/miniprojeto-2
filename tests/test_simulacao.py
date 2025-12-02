import pytest
from src.simulacao import executar_simulacao


@pytest.mark.parametrize(
    "capacidade,n_produtores,n_consumidores,timesteps",
    [
        (3, 2, 2, 4),
        (5, 3, 2, 3),
    ],
)
def test_executar_simulacao_small(capacidade, n_produtores, n_consumidores, timesteps):
    resultado = executar_simulacao(capacidade, n_produtores, n_consumidores, timesteps)

    total_esperado = n_produtores * timesteps
    assert resultado["Total produzido"] == total_esperado
    assert resultado["Total consumido"] == total_esperado
    assert resultado["Itens restantes no buffer"] == 0
    assert isinstance(resultado["history_time"], list)
    assert isinstance(resultado["history_size"], list)

