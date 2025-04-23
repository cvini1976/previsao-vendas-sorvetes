# Previsão de Vendas de Sorvete com Machine Learning - Gelato Mágico

## Visão Geral do Projeto

Este projeto tem como objetivo desenvolver um modelo de Machine Learning para prever as vendas de sorvete da Gelato Mágico com base na temperatura ambiente. A previsão de vendas permitirá ao proprietário otimizar a produção, reduzir desperdícios e maximizar lucros.

## Cenário

A Gelato Mágico, uma sorveteria localizada em uma cidade litorânea, observa uma forte correlação entre a temperatura diária e a quantidade de sorvetes vendidos. A falta de um planejamento preciso leva a problemas como superprodução ou falta de estoque.

## Objetivo

Construir um modelo de regressão preditiva capaz de prever as vendas de sorvete utilizando a temperatura como principal variável preditora. O projeto também envolve o uso do Azure para treinamento, MLflow para gerenciamento de modelos e a criação de um pipeline para garantir a reprodutibilidade.

## Etapas do Projeto (Planejamento)

1.  **Coleta e Preparação dos Dados:**
    * Criação de um dataset simulado (ou coleta de dados reais, se disponível) contendo datas, temperaturas e vendas de sorvete.
    * Análise exploratória dos dados para entender a relação entre temperatura e vendas.
    * Pré-processamento dos dados (tratamento de valores ausentes, normalização/padronização, se necessário).

2.  **Treinamento do Modelo no Azure:**
    * Utilização do Azure Machine Learning para treinar um modelo de regressão (por exemplo, Regressão Linear, Random Forest Regressor, etc.).
    * Seleção e ajuste de hiperparâmetros do modelo.
  
      **Criação do Experimento no Azure ML Studio**
      Tela inicial do Azure Machine Learning Studio, destacando a criação de um novo experimento.
      ![image](https://github.com/user-attachments/assets/b64ee829-5245-49f3-9c76-3c38497a8d12)
  
      **Configuração do Dataset no Azure ML Studio**
      Dataset carregado no Azure ML Studio, com as colunas 'Data', 'Vendas' e 'Temperatura' visíveis.
      ![image](https://github.com/user-attachments/assets/2d0c825e-d01f-426f-8d9c-d57d55d6fe55)
  
      **Configuração da computação no Azure ML Studio**
      Configurando a computação necessarian no Azure ML Studio 'Instacia de computação e Cluster de computação'.
      ![image](https://github.com/user-attachments/assets/dd927918-b481-460a-868f-48fd8ab90dec)

      ![image](https://github.com/user-attachments/assets/e1f17e4a-e5c5-4198-bc66-4ee97525e1c3)

      **Configuração da computação no Azure ML Automatizado**
      Configurando ML Automatizado para treinar e localizar melhor o modelo.
      ![image](https://github.com/user-attachments/assets/3e1dd3f8-aef6-43cf-ba86-b5983d9bd3b2)

      **Configurando Designer**
      usa componentes pré-construídos existentes e tipos de conjunto de dados anteriores (tabular, arquivo) e é mais adequada para processamento de dados e tarefas tradicionais de          aprendizado de máquina, como regressão e classificação.
      ![image](https://github.com/user-attachments/assets/b855e066-fbbf-447b-91bb-e85c42e1395e)

      ![image](https://github.com/user-attachments/assets/68715812-34ec-485b-968a-0968859a79c0)

      **Execução do JObs do modelo**
      Execução do JObs do modelo com os dados treinados.
      ![image](https://github.com/user-attachments/assets/bebd8115-c2e9-417c-b45d-792153c39ff9)

      ![image](https://github.com/user-attachments/assets/c199e7ad-7da7-42c5-8d0e-689846677f4b)

Durante a construção deste projeto, alguns insights importantes podem surgir:

* **A Importância da Correlação:** A forte correlação entre temperatura e vendas de sorvete torna a temperatura uma variável preditora relevante.
* **O Poder do Machine Learning para Otimização:** Modelos preditivos podem ajudar empresas a tomar decisões mais informadas e otimizar seus processos.
* **A Utilidade do Azure e MLflow:** O Azure oferece um ambiente robusto para treinamento e implantação de modelos, enquanto o MLflow facilita o gerenciamento do ciclo de vida do modelo.
* **A Relevância de Pipelines:** Pipelines automatizados garantem a reprodutibilidade e facilitam a atualização e o retreinamento de modelos.
* **Considerações sobre Dados Reais:** Trabalhar com dados reais pode trazer desafios como dados faltantes, outliers e a necessidade de engenharia de features mais complexa.

## Prints do Processo (A Serem Adicionados)

Aqui você adicionará prints de tela que demonstrem as etapas do seu projeto, como:

* Criação do repositório no GitHub.
* Estrutura de pastas e arquivos no seu repositório local.
* (Futuramente) Prints do Azure Machine Learning (criação de experimento, treinamento do modelo, registro do modelo).
* (Futuramente) Prints do MLflow (rastreamento de runs, registro do modelo).
* (Futuramente) Prints da criação do pipeline (se aplicável).

## Insights e Aprendizados

Durante a construção deste projeto, alguns insights importantes podem surgir:

* **A Importância da Correlação:** A forte correlação entre temperatura e vendas de sorvete torna a temperatura uma variável preditora relevante.
* **O Poder do Machine Learning para Otimização:** Modelos preditivos podem ajudar empresas a tomar decisões mais informadas e otimizar seus processos.
* **A Utilidade do Azure e MLflow:** O Azure oferece um ambiente robusto para treinamento e implantação de modelos, enquanto o MLflow facilita o gerenciamento do ciclo de vida do modelo.
* **A Relevância de Pipelines:** Pipelines automatizados garantem a reprodutibilidade e facilitam a atualização e o retreinamento de modelos.
* **Considerações sobre Dados Reais:** Trabalhar com dados reais pode trazer desafios como dados faltantes, outliers e a necessidade de engenharia de features mais complexa.

## Próximos Passos e Possibilidades

* **Coleta de Dados Reais:** Integrar dados de vendas reais da Gelato Mágico para treinar um modelo mais preciso.
* **Incorporação de Outras Variáveis:** Adicionar outras variáveis que possam influenciar as vendas, como dia da semana, feriados, promoções, etc.
* **Análise Sazonal:** Investigar padrões sazonais nas vendas ao longo do ano.
* **Previsão de Demanda por Sabor:** Se os dados permitirem, tentar prever a demanda por diferentes sabores de sorvete.
* **Implementação em Nuvem:** Implementar o modelo treinado em um serviço de nuvem para fornecer previsões em tempo real para a sorveteria.
* **Criação de uma Interface de Usuário:** Desenvolver uma interface simples para que o proprietário da Gelato Mágico possa inserir a temperatura e obter a previsão de vendas.
