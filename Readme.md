# Projeto Docker com Machine Learning



## Objetivo



Este projeto foi desenvolvido para atender à atividade proposta da disciplina, utilizando uma imagem base disponível no Docker Hub e personalizando-a para uma necessidade específica.



A necessidade específica atendida foi a criação de um ambiente conteinerizado para executar um script simples de Machine Learning com Python e Scikit-Learn, permitindo rodar o projeto de forma padronizada e portátil.



## Imagem base utilizada



A imagem base utilizada foi:



`python:3.12-slim`



Essa imagem foi escolhida por ser oficial, leve e adequada para projetos em Python.



## Personalização realizada



A personalização da imagem base foi feita por meio de um arquivo `Dockerfile`, com as seguintes configurações:



\- definição do diretório de trabalho `/app`;

\- cópia do arquivo de dependências;

\- instalação da biblioteca `scikit-learn`;

\- cópia dos arquivos do projeto para dentro do container;

\- definição do comando de execução do script principal.



## Estrutura do projeto



&#x20;   ml-docker-project/

&#x20;   ├── Dockerfile

&#x20;   ├── .dockerignore

&#x20;   ├── requirements.txt

&#x20;   ├── main.py

&#x20;   └── README.md


## Descrição da aplicação

A aplicação consiste em um script simples de Machine Learning desenvolvido em Python com a biblioteca Scikit-Learn. O script utiliza o dataset Iris, realiza a separação entre treino e teste, treina um modelo DecisionTreeClassifier e exibe no terminal a acurácia e algumas previsões do modelo.


## Arquivo Dockerfile


O Dockerfile desenvolvido contém comentários para facilitar o entendimento da personalização realizada.



## Como construir a imagem



No terminal, dentro da pasta do projeto:



&#x20;   docker build -t ml-docker-project:1.0 .



## Como executar o container



&#x20;   docker run --name ml-container ml-docker-project:1.0



## Resultado esperado



Ao executar o container, o script realiza o treinamento de um modelo simples com o dataset Iris e exibe no terminal:



\- mensagem de sucesso;

\- acurácia do modelo;

\- algumas previsões realizadas.



Exemplo de saída:



&#x20;   Projeto de Machine Learning executado com sucesso no Docker.

&#x20;   Acurácia do modelo: 1.00

&#x20;   Primeiras previsões: \[1 0 2 1 1]


## Publicação da imagem


Após a construção da imagem localmente, a imagem foi publicada no Docker Hub na área da usuária.


## Requisitos



\- Docker Desktop instalado e em execução.


## Links

GitHub:
https://github.com/mosmendes/ml-docker-project

Docker Hub:
https://hub.docker.com/r/mosmendes/ml-docker-project



## Autora



Mônica Mendes

