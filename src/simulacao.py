import threading
import logging
from src.buffer import BoundedBuffer
from src.produtor import producer
from src.consumidor import consumer

logger = logging.getLogger(__name__)


def executar_simulacao(capacidade_buffer, n_produtores, n_consumidores, total_timesteps):
    logger.info(
        "Iniciando simulacao: capacidade=%s, produtores=%s, consumidores=%s, timesteps=%s",
        capacidade_buffer,
        n_produtores,
        n_consumidores,
        total_timesteps,
    )
    buffer = BoundedBuffer(capacidade_buffer)
    threads = []

    # Criar produtores
    for p in range(n_produtores):
        t = threading.Thread(target=producer, args=(buffer, p, total_timesteps))
        threads.append(t)
        t.start()

    # Criar consumidores:
    total = n_produtores * total_timesteps
    por_consumidor = total // n_consumidores
    extras = total % n_consumidores

    for c in range(n_consumidores):
        consumir = por_consumidor + (1 if c < extras else 0)
        t = threading.Thread(target=consumer, args=(buffer, c, consumir))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()

    logger.info("Todas as threads finalizaram. Total produzido=%s, total consumido=%s", buffer.total_produced, buffer.total_consumed)

    relatorio = {
        "Capacidade do buffer": capacidade_buffer,
        "Produtores": n_produtores,
        "Consumidores": n_consumidores,
        "Timesteps por produtor": total_timesteps,
        "Total produzido": buffer.total_produced,
        "Total consumido": buffer.total_consumed,
        "Itens restantes no buffer": buffer.size(),
        "Tempo médio espera produtores": buffer.wait_prod / max(1, buffer.total_produced),
        "Tempo médio espera consumidores": buffer.wait_cons / max(1, buffer.total_consumed),
        "history_time": buffer.history_time,
        "history_size": buffer.history_size
    }
    logger.info("Relatorio gerado: %s", {k: v for k, v in relatorio.items() if not isinstance(v, list)})
    return relatorio
