FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir requirements.txt 

COPY . .

CMD ["python", "evaluate.py"]
