import os
from src.utils import gerar_grafico


def test_gerar_grafico_save(tmp_path):
    # criar relatório de exemplo com histórico simples
    rel = {
        "history_time": [0.0, 0.1, 0.2],
        "history_size": [0, 1, 0],
    }

    out_file = tmp_path / "grafico_test.png"
    saved = gerar_grafico(rel, save_path=str(out_file))

    assert saved == str(out_file)
    assert out_file.exists()
    # arquivo deve ter tamanho maior que zero
    assert out_file.stat().st_size > 0
