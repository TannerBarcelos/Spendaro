ARG PY_VERSION=3.11-slim

FROM python:${PY_VERSION}

WORKDIR /usr/api

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./ ./

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
