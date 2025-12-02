# Relatório Final — MinSistema de Controle para Linha de Produção Industrialprojeto

## Resumo
Projeto de simulação concorrente que modela produtores, consumidores e buffers limitados para estudar comportamento de sistemas distribuídos e gerar métricas e gráficos. O código foi adaptado para o tema "Sistema de Controle para Linha de Produção Industrial" (estações/máquinas, esteiras e buffers intermediários).

## Objetivo
Modelar e simular uma linha de produção simplificada para analisar gargalos, tempos de espera, throughput e o impacto de falhas nas estações. Gerar relatórios (CSV), gráficos e logs para avaliação de resiliência e eficiência.

## Metodologia
- Simulação baseada em threads; sincronização por semáforos e locks.
- Cada estação é modelada como thread que consome, processa e produz itens.
- Coleta de métricas em tempo de execução: ocupação do buffer, total produzido/consumido, tempos de espera e histórico temporal.

## Estrutura do repositório (visão rápida)
- `src/` — código-fonte
  - `buffer.py` — `BoundedBuffer` (controle de concorrência + métricas).
  - `produtor.py` — função `producer` (gera/insere itens no buffer).
  - `consumidor.py` — função `consumer` (consome/processa itens).
  - `simulacao.py` — orquestra threads, agrega métricas e retorna `relatorio`.
  - `utils.py` — geração de gráficos (`gerar_grafico`) e utilitários.
  - `configuracoes.py` — parâmetros padrão (CAPACIDADE, PRODUTORES, CONSUMIDORES, TIMESTEPS).
  - `main.py` — ponto de entrada (executa simulação, grava CSV e gera gráficos).
- `tests/` — testes unitários (usar `pytest`).
- `.github/workflows/ci.yml` — configuração do CI.
- `resultados/data/` — saída: CSVs, gráficos e logs.

## Parâmetros principais
- `CAPACIDADE` — capacidade do buffer.
- `PRODUTORES` — número de pontos de entrada.
- `CONSUMIDORES` — número de estações.
- `TIMESTEPS` — número de passos da simulação.

Reduza `TIMESTEPS` para execuções rápidas durante desenvolvimento (ex.: 100).

## Como reproduzir (PowerShell)
1. Criar e ativar ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Instalar dependências:

```powershell
pip install -r requirements.txt
```

3. Executar simulação (modo padrão):

```powershell
python -m src.main
```

4. Rodar testes:

```powershell
pytest -q
```

Observação: este projeto usa layout `src/`. Se ocorrer `ModuleNotFoundError: No module named 'src'`, execute `python -m src.main` ou defina `PYTHONPATH`.

## Formatos de saída
- CSV: `resultados/data/resultados_<timestamp>.csv` — pares `chave, valor` (listas/dicts em JSON quando necessário).
- Gráficos: `resultados/data/graficos/*.png` — histórico de lotação e throughput.
- Logs: `resultados/data/logs/execucao.log` (rotacionamento configurado em `main.py`).

## Arquitetura e responsabilidades
- `BoundedBuffer` (`src/buffer.py`): controla concorrência entre produtores e consumidores usando semáforos `space`/`items` e `mutex`. Mantém métricas: `total_produced`, `total_consumed`, `wait_prod`, `wait_cons`, `history_time`, `history_size`.
- `produtor.py` / `consumidor.py`: loops simples que chamam `produce()` / `consume()` por N timesteps.
- `simulacao.py`: cria threads, distribui carga e agrega métricas em um dicionário `relatorio` retornado ao `main`.
- `utils.py`: funções de plotagem e exportação.

## Métricas coletadas
- Total produzido / consumido.
- Tempo médio de espera para produção/consumo.
- Histórico temporal do tamanho do buffer (para análise de gargalos).

## CI (GitHub Actions)
- Arquivo: `.github/workflows/ci.yml`.
- Configuração recomendada já aplicada: `runs-on: ubuntu-latest`, `python-version: '3.11'` e `env: PYTHONPATH: ${{ github.workspace }}` para permitir imports `from src ...` durante a coleta de testes.

## Problemas comuns e soluções rápidas
- `Version '3.1' was not found` no Actions: usar `3.11` (corrigir typo no workflow).
- `ModuleNotFoundError: No module named 'src'`: executar com `python -m src.main` ou definir `PYTHONPATH`/instalar pacote localmente.
- Estouro de buffer: reduzir taxa de entrada, aumentar `CAPACIDADE` ou implementar políticas de redirecionamento.

## Implementado (estado atual)
- `BoundedBuffer` com semáforos e métricas (`src/buffer.py`).
- Funções `producer` e `consumer` (`src/produtor.py`, `src/consumidor.py`).
- Orquestração da simulação e agregação de métricas (`src/simulacao.py`).
- Ponto de entrada `src/main.py` que executa a simulação, grava um CSV consolidado e gera um gráfico por execução.
- Testes unitários presentes em `tests/` (execução local: 9 passed, 0 failed).
- Ajuste no CI para `python 3.11` e `PYTHONPATH` definido.

## Funcionalidades propostas / extensões (não implementadas)
- Flags CLI: `--tabelas`, `--graficos`, `--resumo` para controlar saídas de forma granular (proposta para `main.py`).
- Módulos adicionais de organização: `supervisor.py`, `relatorios.py`, `logs.py` para separar responsabilidades.
- Injeção programada de falhas (`scheduled_failures`) e políticas avançadas de realocação de carga.
- Exportação de CSVs separados por estação (tabelas por estação).

Se desejar, posso (a) remover menções a funcionalidades não implementadas do relatório, ou (b) implementar a CLI básica e a exportação por estação — diga qual prefere.

## Recomendações práticas
1. Transformar `src/` em pacote instalável (`pyproject.toml`) e usar `pip install -e .` em desenvolvimento.
2. Adicionar `resultados/` a `.gitignore` para evitar commits de artefatos.
3. Incluir `pre-commit` com `black`, `isort` e `ruff` para manter qualidade.
4. Documentar CLI de `main.py` e adicionar testes de integração leves no CI.

## Desenvolvimento e qualidade
Instalação das ferramentas de formatação (exemplo PowerShell):

```powershell
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
# Formatar/organizar código
black .
isort .
ruff --fix .
```

## Como contribuir
1. Fork → clone → branch `feature/<nome>`.
2. Rodar testes e pre-commit localmente.
3. Abrir PR com descrição e evidências (logs/prints).

----

- Nota: o código atual implementa as funcionalidades básicas descritas no relatório: `BoundedBuffer` (`src/buffer.py`), funções `producer`/`consumer`, `executar_simulacao` (`src/simulacao.py`) e o ponto de entrada `src/main.py` que grava um CSV único e gera um gráfico.

- Funcionalidades mencionadas no relatório que são propostas/EXTENSÕES (não implementadas atualmente):
  - Flags CLI como `--tabelas`, `--graficos` e `--resumo` — atualmente `src/main.py` não faz parsing de argumentos.
  - Módulos dedicados como `supervisor.py`, `relatorios.py` ou `logs.py` não existem no repositório atual; são sugestões para organizar melhor execução passo-a-passo e geração tabular por estação.
  - Injeção programada de falhas (`scheduled_failures`) e políticas avançadas de realocação — não implementadas; podem ser adicionadas em `simulacao.py` como mecanismo de eventos por timestep.
  - Exportação de CSVs separados por estação/tabela — atualmente `main.py` grava apenas um CSV com pares `chave, valor`.

- Se preferir que o relatório reflita apenas o estado atual do código, posso remover/ajustar menções a essas funcionalidades ou, alternativamente, implementar rapidamente o suporte a CLI e/ou exportação tabular.

## Formato dos arquivos gerados

- CSV: `resultados/data/resultados_<timestamp>.csv` — pares `chave, valor`. Listas/dicts em JSON.
- Gráficos: `resultados/data/graficos/*.png` — principal: `buffer_lotacao.png`.
- Logs: `resultados/data/logs/execucao.log` (rotacionado diariamente).

## Arquitetura e responsabilidades dos módulos

- `BoundedBuffer` (`src/buffer.py`):
  - Controlo de concorrência com semáforos `space` e `items` e `mutex`.
  - Métricas: `total_produced`, `total_consumed`, `wait_prod`, `wait_cons`.
  - Histórico de ocupação: `history_time`, `history_size`.

- `producer` / `consumer`:
  - Funções simples que chamam `buffer.produce()` / `buffer.consume()` por N timesteps.

- `simulacao.py`:
  - Cria e inicia threads; divide a carga total entre consumidores; aguarda `join` e gera relatório agregando métricas.

- `utils.py`:
  - `gerar_grafico(relatorio, save_path)` — plota `history_time` x `history_size` e salva PNG.

## Métricas coletadas

- Total produzido / consumido.
- Tempo médio de espera para produção/consumo (`wait_prod / total_produced`, `wait_cons / total_consumed`).
- Histórico temporal do tamanho do buffer para análise de lotação.

## CI (GitHub Actions)

- Arquivo: `.github/workflows/ci.yml`.
- Configuração atual:
  - `runs-on: ubuntu-latest`
  - `python-version: '3.11'`
  - `env: PYTHONPATH: ${{ github.workspace }}` para permitir imports `from src ...` durante a coleta de testes.
  - Passos: checkout, setup-python, pip install -r requirements.txt, pip install pytest, pytest -q.

## Problemas comuns e como resolver

- Erro: `Version '3.1' was not found` — verificar matrix do workflow e usar `3.11`.
- Erro: `ModuleNotFoundError: No module named 'src'` — executar com `python -m src.main` ou definir `PYTHONPATH`.
- Instalação de dependências falha ou demora — travar versões e usar cache do pip.

## Boas práticas e recomendações

1. Transformar `src/` em pacote instalável (`pyproject.toml`) e usar `pip install -e .` em dev.
2. Adicionar `resultados/` a `.gitignore` para evitar commits de artefatos.
3. Reduzir `TIMESTEPS` padrão para facilitar desenvolvimento e testes rápidos.
4. Incluir testes de integração leves no CI para garantir regressões mínimas.
5. Documentar CLI de `main.py` (flags para parametrizar execução).

## Desenvolvimento e qualidade de código

- Use `pre-commit` com `black`, `isort` e `ruff`.

```powershell
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
```

Comandos de formatação:

```powershell
black .
isort .
ruff --fix .
```

## Como contribuir

1. Fork → clone → branch `feature/x`.
2. Rodar testes e pré-commit localmente.
3. Abrir PR com descrição e evidências (logs/prints).

---

**Grupo:** Byte 5
**Membros:** Jamili Gabriela, Emílio Gaspar, Wesley Albuquerque
**Data:** 2025-12-02


