# Arquitetura do Projeto

## Visão Geral

O sistema será baseado em um agente implementado com LangGraph.

Cada etapa do processamento será representada por um nó do grafo.

O estado compartilhado armazenará todas as informações produzidas durante a execução.

---

# Fluxo

START

↓

validate_input

↓

load_checklist

↓

analyze_story

↓

generate_acceptance

↓

generate_test_cases

↓

identify_risks

↓

build_report

↓

END

---

# Estado Compartilhado

QAState

Campos:

- user_story
- checklist
- analysis
- acceptance_criteria
- test_cases
- risks
- recommendations
- report

---

# Nós

## validate_input

Responsável por validar a entrada.

---

## load_checklist

Lê o arquivo:

docs/checklist_qa.md

Atualiza:

checklist

---

## analyze_story

Interpreta a User Story utilizando LLM.

Atualiza:

analysis

---

## generate_acceptance

Produz critérios de aceite.

Atualiza:

acceptance_criteria

---

## generate_test_cases

Produz:

- cenários positivos
- cenários negativos
- exceções

Atualiza:

test_cases

---

## identify_risks

Identifica riscos técnicos.

Atualiza:

risks

---

## build_report

Consolida todas as informações.

Atualiza:

report

---

# Ferramentas

Tool 1

load_checklist()

Leitura de arquivo Markdown.

Tool 2

save_report()

Salva relatório em Markdown.

---

# Estrutura de Pastas

ai-qa-assistant/

app.py

graph.py

nodes.py

state.py

tools.py

prompts.py

config.py

docs/

examples/

reports/

README.md

---

# Memória

A memória será implementada através do QAState.

Cada nó atualizará apenas sua parte do estado.

Todo o processamento será baseado nesse estado compartilhado.