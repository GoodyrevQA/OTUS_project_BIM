# Используйте официальный Python образ в качестве базового
FROM python:3.11-slim

# Установите переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установите системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Установите зависимости для Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxrandr2 \
    libgtk-3-0 \
    libgbm1 \
    && rm -rf /var/lib/apt/lists/*

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файл зависимостей
COPY requirements.txt .

# Обновите pip и установите зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Установите браузеры Playwright
RUN playwright install 

# Скопируйте остальной код приложения
COPY . .

# # Установите команду по умолчанию для запуска тестов
# CMD ["pytest"]