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

```text
validate_input → load_checklist → analyze_story → generate_acceptance → generate_test_cases → identify_risks → build_report
