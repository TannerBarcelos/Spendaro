ARG PY_VERSION="3.11-slim"

# Development image
FROM python:${PY_VERSION} AS dev
RUN apt-get update
WORKDIR /usr/api
COPY ./requirements ./requirements
RUN pip install --no-cache-dir --upgrade -r ./requirements/requirements-dev.txt
COPY ./ ./
CMD ["python", "server.py"]

# Production image
FROM python:${PY_VERSION} AS prod
RUN apt-get update \
    && apt-get install -y libpq-dev gcc
WORKDIR /usr/api
COPY ./requirements ./requirements
RUN pip install --no-cache-dir --upgrade -r ./requirements/requirements-prod.txt
COPY ./ ./
CMD ["python", "server.py"]