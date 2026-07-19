# AI QA Assistant

Agente inteligente desenvolvido com LangGraph que auxilia analistas de testes durante o processo de análise de requisitos.

## Visão Geral

O AI QA Assistant recebe uma User Story escrita em linguagem natural e produz automaticamente um relatório estruturado contendo:

- Resumo da User Story
- Critérios de Aceite
- Casos de Teste
- Cenários Positivos
- Cenários Negativos
- Riscos encontrados
- Recomendações para QA

## Objetivo

Reducir o esforço manual necessário para transformar requisitos em um plano inicial de testes.

## Problema

Durante o refinamento de requisitos, analistas de testes precisam interpretar User Stories e elaborar manualmente critérios de aceite e casos de teste. Esse processo consome tempo, depende da experiência do analista, pode gerar inconsistências e nem sempre cobre riscos importantes.

## Solução

O AI QA Assistant automatiza essa primeira análise utilizando Inteligência Artificial.

## Arquitetura

O sistema é baseado em um agente implementado com LangGraph, onde cada etapa do processamento é representada por um nó do grafo.

### Fluxo de Execução

```
validate_input → load_checklist → analyze_story → generate_acceptance → generate_test_cases → identify_risks → build_report
```

### Estado Compartilhado

O estado QAState armazena todas as informações produzidas durante a execução:
- user_story
- checklist
- analysis
- acceptance_criteria
- test_cases
- risks
- recommendations
- report

## Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd ai-qa-assistant
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # no macOS/Linux
```

3. Instale as dependências:
```bash
pip install -e .
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite .env e adicione sua OPENAI_API_KEY
```

## Uso

### Via linha de comando

```bash
# Passando a User Story diretamente
ai-qa-assistant "Como cliente, quero recuperar minha senha para conseguir acessar novamente minha conta."

# Passando arquivo de texto com uma única User Story
ai-qa-assistant --file user-story.txt

# Passando arquivo de texto com várias User Stories
# Separe cada história por uma linha em branco ou use '---' como delimitador
ai-qa-assistant --file examples/multiple-user-stories.txt
```

### Como biblioteca

```python
from ai_qa_assistant.app import run_analysis

user_story = "Como cliente, quero recuperar minha senha para conseguir acessar novamente minha conta."
result = run_analysis(user_story)

print(result.report)
```

## Estrutura do Projeto

```
ai-qa-assistant/
├── src/
│   ├── ai_qa_assistant/
│   │   ├── __init__.py
│   │   ├── app.py           # Ponto de entrada
│   │   ├── config.py        # Configuração
│   │   ├── graph.py         # Definição do LangGraph
│   │   ├── state.py         # Estado compartilhado
│   │   ├── tools.py         # Ferramentas
│   │   ├── prompts.py       # Prompts para IA
│   │   └── nodes/
│   │       ├── __init__.py
│   │       ├── validate_input.py
│   │       ├── load_checklist.py
│   │       ├── analyze_story.py
│   │       ├── generate_acceptance.py
│   │       ├── generate_test_cases.py
│   │       ├── identify_risks.py
│   │       └── build_report.py
│   ├── docs/
│   │   └── checklist_qa.md  # Checklist de QA
│   ├── reports/             # Relatórios gerados
│   └── examples/            # Exemplos de input
├── pyproject.toml
├── .env.example
└── README.md
```

## Dependências

- LangGraph
- LangChain
- LangChain OpenAI
- python-dotenv
- Pydantic

## Requisitos

- Python 3.11+

## Limitações

O agente não substitui a revisão humana. As respostas são sugestões produzidas por IA e devem ser validadas pela equipe de QA.

## Próximos Passos

- Integração com Jira
- Integração com Azure DevOps
- Integração com GitHub Issues
- Exportação para PDF
- Interface Web em Streamlit