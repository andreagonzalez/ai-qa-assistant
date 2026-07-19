"""
Prompts template strings for the AI QA Assistant.
"""

# Main system prompt for the QA analyst agent
SYSTEM_PROMPT = """
Você é um Analista de Testes experiente e atencioso.
Sua tarefa é analisar User Stories e produzir documentação técnica de qualidade.

Regras:
- Analise com atenção os requisitos
- Identifique todos os aspectos que precisam ser testados
- Considere cenários positivos, negativos e exceções
- Identifique riscos técnicos e de negócio
- Seja específico e detalhado nos critérios de aceite
- Utilize Markdown para formatação
"""

# Prompt para analisar a User Story
ANALYZE_STORY_PROMPT = """
Analise a seguinte User Story e extraia:

1. Funcionalidade principal
2. Ator (quem utiliza)
3. Benefício (por que é importante)
4. Pré-condições
5. Pós-condições

User Story:
{user_story}

Formato de resposta (Markdown):
## Análise da User Story

### Funcionalidade Principal
...

### Ator
...

### Benefício
...

### Pré-condições
...

### Pós-condições
...
"""

# Prompt para gerar critérios de aceite
GENERATE_ACCEPTANCE_PROMPT = """
Com base na análise da User Story e no checklist QA, gere critérios de aceite.

User Story:
{user_story}

Análise:
{analysis}

Checklist:
{checklist}

Formato de resposta (Markdown):
## Critérios de Aceite

- **AC01**: ...
- **AC02**: ...
- **AC03**: ...

Regras:
- Seja específico e testável
- Cada critério deve ser verificável
- Considere cenários de sucesso e falha
"""

# Prompt para gerar casos de teste
GENERATE_TEST_CASES_PROMPT = """
Gere casos de teste completos para a User Story.

User Story:
{user_story}

Critérios de Aceite:
{acceptance_criteria}

Formato de resposta (Markdown):
## Casos de Teste

### Cenários Positivos

#### CT001 - [Descrição]
**Precondição**: ...
**Passos**:
1. ...
2. ...
3. ...
**Resultado Esperado**: ...

### Cenários Negativos

#### CT002 - [Descrição]
**Precondição**: ...
**Passos**:
1. ...
**Resultado Esperado**: ...

### Exceções

#### CT003 - [Descrição]
**Precondição**: ...
**Passos**:
1. ...
**Resultado Esperado**: ...
"""

# Prompt para identificar riscos
IDENTIFY_RISKS_PROMPT = """
Identifique riscos técnicos e de negócio para a User Story.

User Story:
{user_story}

Análise:
{analysis}

Critérios de Aceite:
{acceptance_criteria}

Formato de resposta (Markdown):
## Riscos

### Risco Técnico
**ID**: RSK-001
**Descrição**: ...
**Probabilidade**: [Alta/Média/Baixa]
**Impacto**: [Alto/Médio/Baixo]
**Mitigação**: ...

### Risco de Negócio
**ID**: RSK-002
**Descrição**: ...
**Probabilidade**: [Alta/Média/Baixa]
**Impacto**: [Alto/Médio/Baixo]
**Mitigação**: ...
"""

# Prompt para gerar recomendações
GENERATE_RECOMMENDATIONS_PROMPT = """
Gere recomendações para o time de QA com base na análise da User Story.

User Story:
{user_story}

Análise:
{analysis}

Riscos:
{risks}

Formato de resposta (Markdown):
## Recomendações para QA

### Preparação do Ambiente
- ...

### Dados de Teste
- ...

### Tipos de Teste Recomendados
- ...

### Checklist de Regressão
- ...
"""

# Prompt para construir o relatório final
BUILD_REPORT_PROMPT = """
Consolide todas as informações em um relatório estruturado.

User Story Original:
{user_story}

Análise:
{analysis}

Critérios de Aceite:
{acceptance_criteria}

Casos de Teste:
{test_cases}

Riscos:
{risks}

Recomendações:
{recommendations}

Formato de resposta (Markdown):
# Relatório de Análise de User Story

## 1. Resumo
...

## 2. Funcionalidades Identificadas
...

## 3. Critérios de Aceite
...

## 4. Casos de Teste
...

## 5. Riscos Identificados
...

## 6. Recomendações para QA
...
"""

# Prompt para validação de entrada
VALIDATE_INPUT_PROMPT = """
Valide se a entrada é uma User Story válida.

Regras:
- A User Story deve estar em linguagem natural
- Deve conter as partes: Como, Quero, Para
- Tamanho máximo: 5000 caracteres

User Story:
{user_story}

Responda com "VALID" ou "INVALID" seguido da razão.
"""