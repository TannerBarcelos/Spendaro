ARG PY_VERSION=3.11-slim

FROM python:${PY_VERSION} AS base
WORKDIR /usr/api
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./ ./

FROM base AS dev
RUN pip install --no-cache-dir --upgrade -r requirements-dev.txt
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

FROM base AS prod
WORKDIR /usr/api
CMD ["python", "server.py"]