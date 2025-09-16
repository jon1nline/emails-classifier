FROM python:3.12-slim

# Defina as variáveis de ambiente para a aplicação.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho no container.
WORKDIR /app

# Instala o Poetry.
RUN pip install poetry

# Copia os arquivos de dependências do Poetry e os instala.
# O Docker irá usar o cache para acelerar o processo se eles não mudarem.
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root

# Copia todo o código do projeto para o container.
COPY . /app/

# Expõe a porta 8000.
EXPOSE 8000

# Comando para rodar o servidor Gunicorn através do Poetry.
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "smart_mail_classifier.wsgi:application"]