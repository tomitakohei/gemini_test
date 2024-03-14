FROM python:3.10

RUN pip install "google-cloud-aiplatform>=1.38"
ADD run.py .
