<<<<<<< HEAD
import matplotlib.pyplot as plt
import os
import json


def gerar_grafico(relatorio, save_path: str = None):
   

    tempo = relatorio.get("history_time", [])
    tamanho = relatorio.get("history_size", [])

    plt.figure(figsize=(10, 5))
    plt.plot(tempo, tamanho)
    plt.title("Variação do Tamanho do Buffer ao Longo do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Itens no Buffer")
    plt.grid(True)

    if save_path:
        directory = os.path.dirname(save_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight")
        plt.close()
        return save_path
    else:
        plt.show()
        plt.close()
        return None
