# AI QA Assistant

## Visão Geral

O AI QA Assistant é um agente inteligente desenvolvido com LangGraph que auxilia analistas de testes durante o processo de análise de requisitos.

O agente recebe uma User Story escrita em linguagem natural e produz automaticamente um relatório estruturado contendo:

- Resumo da User Story
- Critérios de Aceite
- Casos de Teste
- Cenários Positivos
- Cenários Negativos
- Riscos encontrados
- Recomendações para QA

O objetivo é reduzir o esforço manual necessário para transformar requisitos em um plano inicial de testes.

---

# Problema

Durante o refinamento de requisitos, analistas de testes precisam interpretar User Stories e elaborar manualmente critérios de aceite e casos de teste.

Esse processo:

- consome tempo;
- depende da experiência do analista;
- pode gerar inconsistências;
- nem sempre cobre riscos importantes.

O AI QA Assistant automatiza essa primeira análise utilizando Inteligência Artificial.

---

# Objetivos

O sistema deverá:

- interpretar User Stories;
- identificar funcionalidades;
- identificar regras de negócio;
- sugerir critérios de aceite;
- gerar casos de teste;
- identificar riscos;
- gerar um relatório em Markdown.

---

# Público-alvo

- QA Engineers
- Analistas de Testes
- Desenvolvedores
- Product Owners
- Scrum Masters

---

# Entrada

Texto simples.

Exemplo:

Como cliente,
quero recuperar minha senha
para conseguir acessar novamente minha conta.

Também poderá aceitar arquivos:

- txt
- md

---

# Saída

Relatório estruturado contendo:

## Resumo

Resumo da funcionalidade.

## Funcionalidades

Lista das funcionalidades identificadas.

## Critérios de Aceite

...

## Casos de Teste

CT001

CT002

...

## Riscos

...

## Recomendações

...

---

# Benefícios

- Padronização
- Economia de tempo
- Maior cobertura inicial de testes
- Apoio ao planejamento de QA

---

# Limitações

O agente não substitui a revisão humana.

As respostas são sugestões produzidas por IA e devem ser validadas pela equipe de QA.

---

# Critérios de Sucesso

O projeto será considerado concluído quando:

- interpretar corretamente uma User Story;
- gerar relatório estruturado;
- utilizar LangGraph;
- utilizar pelo menos uma ferramenta;
- utilizar memória;
- possuir documentação completa.