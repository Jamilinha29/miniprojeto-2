# MiniProjeto 2 — Sistema Distribuído

Simulação de produtores e consumidores com buffer limitado. O projeto implementa uma pequena simulação concorrente, gera relatórios em CSV e gráficos, e possui testes automatizados.

**Visão rápida**
- Linguagem: Python
- Recomendado: Python 3.11

**Conteúdo principal**
- `src/` — código fonte
- `tests/` — testes (pytest)
- `docs/` — documentação (inclui `relatorio_final.md`)
- `resultados/` — saídas geradas (CSV, gráficos)

## Requisitos

- Python 3.8+ (recomendado 3.11)
- Instalar dependências:

```powershell
pip install -r requirements.txt
```

## Estrutura do código

- `src/buffer.py` — `BoundedBuffer`
- `src/produtor.py` — função `producer`
- `src/consumidor.py` — função `consumer`
- `src/simulacao.py` — `executar_simulacao`
- `src/utils.py` — funções utilitárias (ex.: `gerar_grafico`)
- `src/configuracoes.py` — configurações padrão
- `src/main.py` — script principal (entrada do programa)

## Como executar

Recomendo rodar a partir da raiz do projeto usando o módulo `src`:

```powershell
cd 'C:\My\faculdade\Victor\Sistema Distribuido\miniprojeto 2'
python -m src.main
```

Por que usar `python -m src.main`?
- Executar com `-m` garante que o diretório do projeto esteja no `PYTHONPATH` e evita `ModuleNotFoundError: No module named 'src'`.

### Alternativa (não recomendada)

Se quiser executar diretamente o arquivo (por exemplo para depuração rápida), defina o `PYTHONPATH` temporariamente:

```powershell
$env:PYTHONPATH = 'C:\My\faculdade\Victor\Sistema Distribuido\miniprojeto 2'
python src\main.py
```

## Testes

Executar a suíte de testes:

```powershell
python -m pytest -q
```

## Integração Contínua (CI)

- O workflow está em `.github/workflows/ci.yml` e usa `python 3.11`.
- O job define `PYTHONPATH` para `${{ github.workspace }}` para permitir imports `from src ...` durante a execução dos testes.

## Recomendações

- Tornar `src` um pacote instalável (`pip install -e .`) ou adicionar `pyproject.toml`/`setup.cfg` para melhorar portabilidade.
- Adicionar `resultados/` ao `.gitignore` para não versionar artefatos gerados.
- Travar versões das dependências no `requirements.txt` para garantir reprodutibilidade no CI.

## Execução em Docker (opcional)

Para reproduzir o ambiente do runner (ex.: Python 3.11):

```powershell
docker run --rm -v "${PWD}:/work" -w /work python:3.11 bash -lc "pip install -r requirements.txt && pytest -q"
```

## Contribuição

- Abra uma issue para descrever a mudança desejada.
- Crie branches com o prefixo `feature/` ou `fix/` e envie pull requests.

---

Se quiser, eu aplico mudanças adicionais: transformar `src` em pacote instalável, adicionar `.gitignore` para `resultados/`, ou commitar este README atualizado. Diga qual deseja que eu faça.
