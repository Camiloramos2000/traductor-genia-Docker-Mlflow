# mlflow_server/Dockerfile
FROM python:3.11-slim

WORKDIR /mlflow

RUN pip install mlflow[extras]

EXPOSE 5000

CMD mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root /mlflow/artifacts \
    --host 0.0.0.0 \
    --port 5000
