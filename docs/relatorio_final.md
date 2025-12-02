# Relatório Final — Miniprojeto 2

## Resumo do Projeto
Este repositório implementa uma simulação distribuída simples com produtores, consumidores e um buffer limitado. O objetivo é estudar o comportamento de sistemas concorrentes e gerar relatórios/ gráficos com os resultados.

## Estrutura do repositório
- `src/` : código fonte do projeto
  - `buffer.py` : implementação do buffer limitado (`BoundedBuffer`) usado pelos produtores/consumidores.
  - `produtor.py` : lógica do produtor (função `producer`).
  - `consumidor.py` : lógica do consumidor (função `consumer`).
  - `simulacao.py` : orquestra a execução da simulação (`executar_simulacao`).
  - `main.py` : script principal para executar a simulação e salvar resultados (CSV e gráficos).
  - `configuracoes.py` : constantes de configuração padrão (CAPACIDADE, PRODUTORES, CONSUMIDORES, TIMESTEPS).
  - `utils.py` : utilitários (por exemplo, `gerar_grafico`) usados para gerar imagens e processar resultados.

- `tests/` : testes unitários (pytest).
- `docs/` : documentação (este relatório está em `docs/relatorio_final.md`).
- `requirements.txt` : dependências do projeto.
- `.github/workflows/ci.yml` : workflow do GitHub Actions para rodar testes.

## Como executar localmente
1. Criar e ativar um ambiente virtual (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -U pip
pip install -r requirements.txt
```

2. Rodar a simulação (exemplo):

```powershell
python -m src.main
```

O script `main.py` gera arquivos CSV em `resultados/data` e gráficos em `resultados/data/graficos`.

## Como rodar os testes
Com o ambiente ativado e dependências instaladas:

```powershell
pytest -q
```

No CI (GitHub Actions) o workflow executa `pip install -r requirements.txt` e em seguida `pytest -q`.

## Observações sobre o CI
- O arquivo de workflow foi padronizado para usar `python 3.11` e o job exporta `PYTHONPATH=${{ github.workspace }}` para permitir importações como `from src...` durante os testes.
- Caso o runner apresente erros em instalação de dependências, verifique as primeiras linhas do step `Install dependencies` no log do Actions.

## Resumo das alterações feitas durante a revisão
- Corrigido `src/main.py` (remoção de linhas corrompidas duplicadas no final do arquivo).
- Ajustado `.github/workflows/ci.yml` para:
  - Usar `python-version: '3.11'` (remover matrix para evitar versão inválida `3.1`).
  - Definir `PYTHONPATH` para `${{ github.workspace }}` (resolve `ModuleNotFoundError: No module named 'src'`).

## Pontos de atenção / sugestões
- Organização do pacote: atualmente os módulos são importados via `src.*`. Alternativa mais robusta é transformar `src` em pacote instalável (ex.: adicionar `pyproject.toml`/`setup.cfg` e instalar `pip install -e .`) — isso torna imports independentes do `PYTHONPATH` e mais portátil.
- Repositórios com artefatos (p.ex. `resultados/data`) devem geralmente adicionar regras `.gitignore` para evitar commits acidentais de arquivos gerados pelo run.
- Considerar travar versões das dependências em `requirements.txt` para garantir reprodutibilidade no CI.

## Testes realizados localmente
- Executei a suíte de testes local (9 passed, 0 failed) antes das alterações no workflow.
- Depois de ajustar `PYTHONPATH` no CI, os erros de coleta (`ModuleNotFoundError`) devem ser resolvidos; caso surjam novos erros na etapa `Install dependencies` ou nos próprios testes, analisar o log específico.

## Como proceder se algo falhar no CI
- Cole o trecho inicial do step que falha (primeiras ~40 linhas) e eu reviso.
- Para reexecutar um run com as correções aplicadas, faça commit/push; também é possível re-executar o job manualmente pelo GitHub Actions.

## Contatos e autoria
- Autor do repositório: (conforme commit history)

---
Relatório gerado automaticamente pelo assistente de revisão de código.
