ARG PY_VERSION=3.11-slim

FROM python:${PY_VERSION} AS base

# Update dependencies and install dependencies to build psycopg2 binary
RUN apt-get update \
    && apt-get install -y libpq-dev gcc

WORKDIR /usr/api

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get install libpq-dev
COPY ./ ./

FROM base AS dev
WORKDIR /usr/api
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

FROM base AS prod
WORKDIR /usr/api
CMD ["uvicorn", "server:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]