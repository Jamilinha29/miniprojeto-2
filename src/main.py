import time
from configuracoes import CAPACIDADE, PRODUTORES, CONSUMIDORES, TIMESTEPS
from simulacao import executar_simulacao

if __name__ == "__main__":
    inicio = time.time()
    resultado = executar_simulacao(CAPACIDADE, PRODUTORES, CONSUMIDORES, TIMESTEPS)
    fim = time.time()

    print()
    print("=== RELATORIO FINAL ===")
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")
    print(f"tempo_total: {fim - inicio:.2f} segundos")
