FROM python:3.11-slim

# Defina as variáveis de ambiente para a aplicação.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho no container.
WORKDIR /app

# Copia o arquivo de dependências e as instala.
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copia todo o código do projeto para o container.
COPY . /app/

# Expõe a porta 8000.
EXPOSE 8000

# Comando para rodar o servidor Gunicorn.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "smart_mail_classifier.wsgi:application"]