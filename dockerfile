FROM python:3.12

WORKDIR /src

RUN apt-get update && \
    apt install -y python3-dev

RUN pip install --upgrade pip
RUN pip install poetry
ADD pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

CMD uvicorn anatomic.app:app --reload --host 0.0.0.0 --port 10000