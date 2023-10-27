ARG PY_VERSION="3.11-slim"
ARG REQUIREMENTS_FILE_DEV="./requirements/requirements-dev.txt"
ARG REQUIREMENTS_FILE_PROD="./requirements/requirements-prod.txt"

# Development image
FROM python:${PY_VERSION} AS dev
RUN apt-get update
WORKDIR /usr/api
COPY ${REQUIREMENTS_FILE_DEV} .
RUN pip install --no-cache-dir --upgrade -r ${REQUIREMENTS_FILE_DEV}
COPY ./ ./
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Production image
FROM python:${PY_VERSION} AS prod
RUN apt-get update \
    && apt-get install -y libpq-dev gcc
WORKDIR /usr/api
COPY ${REQUIREMENTS_FILE_PROD} .
RUN pip install --no-cache-dir --upgrade -r ${REQUIREMENTS_FILE_PROD}
COPY ./ ./
CMD ["uvicorn", "server:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]