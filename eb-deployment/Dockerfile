FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "app:app", "--workers", "4", "--worker-class", "gthread", "--timeout", "30", "--bind", "0.0.0.0:8000"]
