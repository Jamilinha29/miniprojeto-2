import os
import datetime

def criar_pasta(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def salvar_em_arquivo(caminho, conteudo):
    with open(caminho, "a", encoding="utf-8") as f:
        f.write(conteudo + "\n")
