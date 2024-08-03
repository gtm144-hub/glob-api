FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app/ .
COPY db/init.sql /docker-entrypoint-initdb.d/10-init.sql

##Temporary environment variables, in GCP should manage this
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_SERVER=localhost
ENV POSGRES_PORT=5432
ENV POSTGRES_DB=test-employers

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
