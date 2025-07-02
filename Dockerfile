
FROM python:3.11-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ["gunicorn", "deporte_ecosistema.wsgi:application", "--bind", "0.0.0.0:8000"]
