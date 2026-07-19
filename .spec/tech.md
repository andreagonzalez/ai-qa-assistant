# Especificação Técnica

## Linguagem

Python 3.11+

---

# Frameworks

- LangGraph
- LangChain
- LangChain OpenAI
- python-dotenv
- Pydantic

---

# Arquitetura

Arquitetura baseada em agentes.

Fluxo orientado por estados.

Separação entre:

- Graph
- Nodes
- State
- Tools
- Prompts

---

# Organização dos Arquivos

app.py

Ponto de entrada da aplicação.

---

graph.py

Construção do LangGraph.

---

nodes.py

Implementação dos nós.

---

state.py

Definição do QAState.

---

tools.py

Ferramentas utilizadas pelo agente.

---

prompts.py

Todos os prompts utilizados.

---

config.py

Leitura das configurações.

---

# Ferramentas

## load_checklist()

Entrada:

docs/checklist_qa.md

Saída:

Texto contendo checklist QA.

---

## save_report()

Entrada:

Relatório Markdown.

Saída:

Arquivo salvo em reports/.

---

# Prompt Principal

O modelo deverá atuar como um Analista de Testes experiente.

Deverá:

- analisar requisitos;
- identificar riscos;
- produzir critérios de aceite;
- gerar casos de teste;
- responder em Markdown.

---

# Memória

Será utilizada memória de execução através do State do LangGraph.

Não será utilizada memória persistente.

---

# Segurança

- Utilizar .env
- Não versionar chaves
- Validar entradas
- Limitar tamanho da User Story
- Tratar exceções

---

# Requisitos Funcionais

RF01

Receber User Story.

RF02

Consultar checklist.

RF03

Interpretar requisito.

RF04

Gerar critérios.

RF05

Gerar casos de teste.

RF06

Gerar riscos.

RF07

Gerar relatório.

RF08

Salvar relatório.

---

# Requisitos Não Funcionais

RNF01

Código modular.

RNF02

Documentação completa.

RNF03

Tempo médio inferior a 30 segundos.

RNF04

Projeto versionado no GitHub.

RNF05

Prompts documentados.

---

# Melhorias Futuras

- Integração com Jira
- Integração com Azure DevOps
- Integração com GitHub Issues
- Exportação para PDF
- Geração automática de TestRail
- Histórico de análises
- Interface Web em Streamlit