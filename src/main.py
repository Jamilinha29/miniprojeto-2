import time
import os
import csv
import json
import logging
from logging.handlers import TimedRotatingFileHandler
from src.simulacao import executar_simulacao
from src.utils import gerar_grafico
from src.configuracoes import CAPACIDADE, PRODUTORES, CONSUMIDORES, TIMESTEPS


def salvar_relatorio_csv(relatorio, folder="resultados/data"):
    os.makedirs(folder, exist_ok=True)
    timestamp = int(time.time())
    filename = os.path.join(folder, f"resultados_{timestamp}.csv")
    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["chave", "valor"])
        for k, v in relatorio.items():
            if isinstance(v, (list, dict)):
                writer.writerow([k, json.dumps(v, ensure_ascii=False)])
            else:
                writer.writerow([k, v])
    return filename


def setup_logging(log_folder="resultados/data/logs"):
    os.makedirs(log_folder, exist_ok=True)
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = TimedRotatingFileHandler(
            os.path.join(log_folder, "execucao.log"), when="midnight", backupCount=7, encoding="utf-8"
        )
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logging.getLogger(__name__)


if __name__ == "__main__":
    # configurar logging
    setup_logging()

    inicio = time.time()
    resultado = executar_simulacao(CAPACIDADE, PRODUTORES, CONSUMIDORES, TIMESTEPS)
    fim = time.time()

    print("\n=== RELATÓRIO FINAL ===")
    for k, v in resultado.items():
        if not isinstance(v, list):
            print(f"{k}: {v}")

    print(f"Tempo total: {fim - inicio:.2f} segundos")

    # Garantir pastas de resultados e salvar relatório
    os.makedirs("resultados/data/graficos", exist_ok=True)
    os.makedirs("resultados/data/logs", exist_ok=True)

    csv_path = salvar_relatorio_csv(resultado, folder="resultados/data")
    print(f"Relatório salvo em: {csv_path}")

    # Salvar gráfico principal e também criar cópias com nomes padronizados
    grafico_base = "resultados/data/graficos/buffer_lotacao.png"
    saved = gerar_grafico(resultado, save_path=grafico_base)
    if saved:
        print(f"Gráfico salvo em: {saved}")
        # criar cópias com nomes solicitados
        try:
            import shutil
            shutil.copy(grafico_base, "resultados/data/graficos/produtores_consumidores.png")
            shutil.copy(grafico_base, "resultados/data/graficos/eficiencia.png")
        except Exception:
            pass
