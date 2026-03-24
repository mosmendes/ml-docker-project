# Usa uma imagem oficial do Python disponível no Docker Hub como base
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as bibliotecas necessárias para o projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia os demais arquivos do projeto para o container
COPY . .

# Define o comando padrão para executar o script principal
CMD ["python", "main.py"]