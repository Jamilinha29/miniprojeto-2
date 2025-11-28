import threading
import time
from buffer import BufferLimitado
from produtor import produtor
from consumidor import consumidor

def executar_simulacao(capacidade, n_produtores, n_consumidores, passos_por_produtor):
    buffer = BufferLimitado(capacidade)
    threads = []

    for p in range(n_produtores):
        t = threading.Thread(target=produtor, args=(buffer, p, passos_por_produtor))
        threads.append(t)
        t.start()

    total_itens = n_produtores * passos_por_produtor
    por_consumidor = total_itens // n_consumidores
    extras = total_itens % n_consumidores

    for c in range(n_consumidores):
        passos = por_consumidor + (1 if c < extras else 0)
        t = threading.Thread(target=consumidor, args=(buffer, c, passos))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    relatorio = {
        "capacidade_buffer": capacidade,
        "produtores": n_produtores,
        "consumidores": n_consumidores,
        "passos_por_produtor": passos_por_produtor,
        "total_produzido": buffer.total_produzido,
        "total_consumido": buffer.total_consumido,
        "restante_buffer": buffer.tamanho(),
        "tempo_medio_espera_produtores": buffer.tempo_espera_prod / max(1, buffer.total_produzido),
        "tempo_medio_espera_consumidores": buffer.tempo_espera_cons / max(1, buffer.total_consumido)
    }

    return relatorio
