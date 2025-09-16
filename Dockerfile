FROM python:3.11-slim

# Defina as variáveis de ambiente para a aplicação.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Defina o diretório de trabalho no container.
WORKDIR /app

# Copie o poetry para o container.
RUN pip install poetry

# Copie os arquivos de dependências e instale-as.
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root

# Copie o código do projeto para o container.
COPY . /app/

# Exponha a porta 8000 para que a aplicação possa ser acessada.
EXPOSE 8000

# Comando para rodar o servidor Gunicorn.
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "smart_mail_classifier.wsgi:application"]