# Офіційний образ Python
FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask слухає порт 5000
EXPOSE 5000

# Запускаємо додаток
CMD ["python", "app.py"]
