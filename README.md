# MiniProjeto 2 — Sistema Distribuído

Breve projeto de simulação de produtores e consumidores (buffer limitado).

**Requisitos**

- Python 3.8+ (recomendado 3.11)
- Dependências (se houver):

```powershell
pip install -r requirements.txt
```

**Como executar**

1. Abra o PowerShell e entre na raiz do projeto. Exemplo:

```powershell
Set-Location 'C:\My\faculdade\Victor\Sistema Distribuido\miniprojeto 2'
# ou
cd 'C:\My\faculdade\Victor\Sistema Distribuido\miniprojeto 2'
```

2. Execute o pacote `src` usando o módulo principal:

```powershell
python -m src.main
```

> Observação: execute sempre com `python -m src.main` a partir da raiz do projeto. Não execute `src\main.py` diretamente, pois isso causa o erro "ModuleNotFoundError: No module named 'src'". O comando `python -m` garante que o pacote `src` esteja no caminho de importação.

**Alternativa (não recomendada)**

Se precisar rodar o script diretamente, defina temporariamente `PYTHONPATH` para a raiz do projeto:

```powershell
$env:PYTHONPATH = 'C:\My\faculdade\Victor\Sistema Distribuido\miniprojeto 2'
python src\main.py
```

**Testes**

Rodar os testes com:

```powershell
python -m pytest -q
```

---

Se quiser, posso: 1) ajustar os imports para usar imports relativos dentro de `src/` (para permitir executar `python -m src.main` sem problemas) ou 2) aplicar mudanças para permitir executar `src\main.py` diretamente. Qual prefere?
