"""
Prompts template strings for the AI QA Assistant.

This module defines all prompts used by the LangGraph nodes to interact
with the LLM. Each prompt is designed for a specific step in the QA analysis
pipeline and includes clear instructions and output format specifications.

All prompts use Python f-string syntax for parameter substitution.
"""

# ============================================================================
# SYSTEM PROMPTS
# ============================================================================

SYSTEM_PROMPT = """
Você é um Analista de Testes experiente e atencioso, especializado em análise
de requisitos e planejamento de testes.

Sua tarefa é analisar User Stories e produzir documentação técnica de alta
qualidade seguindo boas práticas de QA.

Regras de comportamento:
- Analise com atenção todos os detalhes dos requisitos
- Identifique todos os aspectos que precisam ser testados
- Considere cenários positivos, negativos e exceções
- Identifique riscos técnicos e de negócio
- Seja específico e detalhado nos critérios de aceite
- Utilize Markdown para formatação
- Considere o checklist QA fornecido como referência
- Seu público-alvo inclui QA Engineers, Desenvolvedores e Product Owners
"""

VALIDATE_INPUT_SYSTEM_PROMPT = """
Você é um validador de requisitos. Sua tarefa é verificar se a entrada
corresponde a uma User Story válida.
"""

# ============================================================================
# NODE-SPECIFIC PROMPTS
# ============================================================================

# ----------------------------------------------------------------------------
# validate_input
# ----------------------------------------------------------------------------

VALIDATE_INPUT_PROMPT = """
Valide se a entrada fornecida é uma User Story válida.

Regras de validação:
- A User Story deve estar em linguagem natural
- Deve conter as três partes fundamentais: "Como", "Quero", "Para"
- O formato típico é: "Como [ator], quero [funcionalidade], para [benefício]"
- Tamanho máximo permitido: 5000 caracteres
- Não deve conter código ou sintaxe técnica complexa

User Story a ser validada:
{user_story}

Formato de resposta:
- Responda apenas "VALID" se a User Story for válida
- Responda "INVALID: <motivo>" se a User Story for inválida

Exemplos de resposta:
VALID
INVALID: User Story não contém a parte "para" (benefício)
"""

# ----------------------------------------------------------------------------
# load_checklist
# ----------------------------------------------------------------------------

LOAD_CHECKLIST_PROMPT = """
Carregue o checklist de QA para referência durante a análise.

Checklist:
{checklist_content}

Use este checklist como guia para identificar aspectos que devem ser
considerados na análise da User Story.
"""

# ----------------------------------------------------------------------------
# analyze_story
# ----------------------------------------------------------------------------

ANALYZE_STORY_PROMPT = """
Analise a User Story fornecida e extraia as informações essenciais para
o planejamento de testes.

User Story:
{user_story}

Checklist:
{checklist}

Extraia as seguintes informações:

## Análise da User Story

### Funcionalidade Principal
Descreva a funcionalidade principal que está sendo solicitada.

### Ator (Quem utiliza)
Identifique o papel ou角色 que utiliza esta funcionalidade.

### Benefício (Por que é importante)
Explique o valor ou benefício que esta funcionalidade traz.

### Pré-condições
Descreva as condições que devem estar satisfeitas antes da funcionalidade
ser executada.

### Pós-condições
Descreva o estado final após a execução da funcionalidade.

### Regras de Negócio
Identifique todas as regras de negócio implícitas ou explícitas.

### Dados envolvidos
Liste os dados ou entidades envolvidos na funcionalidade.

Formato de resposta:
Utilize Markdown para formatação. Seja específico e detalhado.
"""

# ----------------------------------------------------------------------------
# generate_acceptance
# ----------------------------------------------------------------------------

GENERATE_ACCEPTANCE_PROMPT = """
Gere critérios de aceite para a User Story com base na análise realizada.

User Story Original:
{user_story}

Análise:
{analysis}

Checklist QA:
{checklist}

Critérios de Aceite devem:
- Ser específicos e testáveis
- Cobrir cenários de sucesso (happy path)
- Cobrir cenários de falha (error path)
- Ser verificáveis sem ambiguidade
- Incluir condições de saída (exit criteria)

Formato de resposta (Markdown):

## Critérios de Aceite

- **AC01 - [Descrição breve]**: Descrição detalhada do critério
- **AC02 - [Descrição breve]**: Descrição detalhada do critério
- **AC03 - [Descrição breve]**: Descrição detalhada do critério

Formato para cada critério:
- Número do critério (AC01, AC02, etc.)
- Título descritivo curto
- Descrição completa e verificável
- Considere: sucesso, falha e exceções
"""

# ----------------------------------------------------------------------------
# generate_test_cases
# ----------------------------------------------------------------------------

GENERATE_TEST_CASES_PROMPT = """
Gere casos de teste completos para a User Story.

User Story:
{user_story}

Critérios de Aceite:
{acceptance_criteria}

Tipos de casos de teste a serem gerados:

## Casos de Teste

### Cenários Positivos (Happy Path)
Casos que verificam o comportamento esperado quando tudo ocorre conforme o planejado.

Formato:
#### CT001 - [Descrição breve]
**Precondição**: ...
**Passos**:
1. ...
2. ...
3. ...
**Entrada**: ...
**Resultado Esperado**: ...

### Cenários Negativos (Error Path)
Casos que verificam o comportamento quando entradas inválidas ou erros ocorrem.

Formato:
#### CT002 - [Descrição breve]
**Precondição**: ...
**Passos**:
1. ...
**Entrada**: ...
**Resultado Esperado**: ...

### Cenários de Exceção
Casos que verificam comportamentos excepcionais ou edge cases.

Formato:
#### CT003 - [Descrição breve]
**Precondição**: ...
**Passos**:
1. ...
**Entrada**: ...
**Resultado Esperado**: ...

Regras:
- Comece a numeração em CT001
- Seja específico nos passos e resultados esperados
- Considere validações de entrada
- Inclua casos de performance quando aplicável
"""

# ----------------------------------------------------------------------------
# identify_risks
# ----------------------------------------------------------------------------

IDENTIFY_RISKS_PROMPT = """
Identifique riscos técnicos e de negócio associados à User Story.

User Story:
{user_story}

Análise:
{analysis}

Critérios de Aceite:
{acceptance_criteria}

Tipos de riscos a considerar:

### Risco Técnico
- Complexidade técnica inerente
- Integrações com outros sistemas
- Dependencies externas
- Performance e escalabilidade
- Segurança
- Testabilidade do código

### Risco de Negócio
- Impacto no usuário
- Cumprimento de regulamentações
- Reputação da empresa
- Custo de falha

Formato de resposta (Markdown):

## Riscos Identificados

### Risco Técnico
**ID**: RSK-TEC-001
**Descrição**: ...
**Probabilidade**: [Alta/Média/Baixa]
**Impacto**: [Alto/Médio/Baixo]
**Prioridade**: [Alta/Média/Baixa]
**Mitigação**: ...

### Risco de Negócio
**ID**: RSK-NEG-001
**Descrição**: ...
**Probabilidade**: [Alta/Média/Baixa]
**Impacto**: [Alto/Médio/Baixo]
**Prioridade**: [Alta/Média/Baixa]
**Mitigação**: ...

Regras:
- Identifique pelo menos 3 riscos (2 técnicos, 1 de negócio)
- Use a matriz probabilidade x impacto para priorização
- Forneça estratégias de mitigação específicas
"""

# ----------------------------------------------------------------------------
# generate_recommendations
# ----------------------------------------------------------------------------

GENERATE_RECOMMENDATIONS_PROMPT = """
Gere recomendações para o time de QA com base na análise da User Story.

User Story:
{user_story}

Análise:
{analysis}

Riscos Identificados:
{risks}

Áreas para recomendação:

## Recomendações para QA

### Preparação do Ambiente
- Infraestrutura necessária
- Configurações especiais
- Dados de teste requeridos

### Dados de Teste
- Quais dados são necessários
- Como preparar os dados
- Considerações sobre dados sensíveis

### Tipos de Teste Recomendados
- Testes funcionais
- Testes de integração
- Testes de regressão
- Testes de performance (se aplicável)
- Testes de segurança (se aplicável)

### Checklist de Validação
- Verificações antes de deploy
- Verificações pós-deploy
- Monitoramento recomendado

### Observações Adicionais
- Pontos de atenção especiais
- Interações com outras funcionalidades
- Documentação necessária

Regras:
- Seja prático e acionável
- Priorize o que traz mais valor para a qualidade
- Considere o orçamento de tempo disponível
"""

# ----------------------------------------------------------------------------
# build_report
# ----------------------------------------------------------------------------

BUILD_REPORT_PROMPT = """
Consolide todas as informações em um relatório estruturado e completo.

User Story Original:
{user_story}

Análise:
{analysis}

Critérios de Aceite:
{acceptance_criteria}

Casos de Teste:
{test_cases}

Riscos Identificados:
{risks}

Recomendações:
{recommendations}

Formato do relatório final (Markdown):

# Relatório de Análise de User Story

## 1. Resumo

Resumo conciso da funcionalidade analisada, incluindo:
- O que será desenvolvido
- Quem utilizará
- Qual o valor para o negócio

## 2. Funcionalidades Identificadas

Lista das principais funcionalidades extraídas da User Story:
- Funcionalidade 1
- Funcionalidade 2
- Funcionalidade 3

## 3. Critérios de Aceite

### AC01 - [Descrição]
Descrição detalhada...

### AC02 - [Descrição]
Descrição detalhada...

(continuar para todos os critérios)

## 4. Casos de Teste

### Cenários Positivos

#### CT001 - [Descrição]
**Precondição**: ...
**Passos**: ...
**Resultado Esperado**: ...

(continuar para todos os casos positivos)

### Cenários Negativos

#### CT00X - [Descrição]
**Precondição**: ...
**Passos**: ...
**Resultado Esperado**: ...

(continuar para todos os casos negativos)

### Exceções

#### CT00X - [Descrição]
**Precondição**: ...
**Passos**: ...
**Resultado Esperado**: ...

(continuar para todos os casos de exceção)

## 5. Riscos Identificados

### RSK-TEC-001 - [Descrição]
- **Probabilidade**: ...
- **Impacto**: ...
- **Prioridade**: ...
- **Mitigação**: ...

(continuar para todos os riscos)

## 6. Recomendações para QA

### Preparação do Ambiente
- ...

### Dados de Teste
- ...

### Tipos de Teste Recomendados
- ...

### Checklist de Validação
- ...

## 7. Anexos

### Checklist Utilizado
[Incluir o checklist QA como referência]

### Notas Adicionais
[Qualquer informação complementar]

Regras:
- Mantenha consistência com a formatação Markdown
- Use numeração sequencial para casos de teste
- Referencie critérios de aceite nos casos de teste
- Seja claro e objetivo
"""