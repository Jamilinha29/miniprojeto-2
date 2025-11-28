def produtor(buffer, pid, passos):
    for passo in range(passos):
        buffer.produzir((pid, passo))
