FROM python:3.9-alpine

RUN apk add \
    python3 \
    python3-dev \
    build-base \
    libffi-dev \
    curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python

ADD pyproject.toml .
ADD poetry.lock .

RUN ~/.local/bin/poetry config virtualenvs.create false && \
    ~/.local/bin/poetry install

WORKDIR /app

ADD . .

EXPOSE 8000

CMD uvicorn main:app
