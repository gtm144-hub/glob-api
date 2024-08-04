FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .
COPY db/init.sql /docker-entrypoint-initdb.d/10-init.sql

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
