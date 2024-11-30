# Устанавка базового образ
FROM python:3.9-slim

# Устанавка рабочего директория внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /app

# Копирование зависимостей
# Для того чтобы не пересобирать их каждый раз при сборке образа
COPY requirements.txt .


RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
# Установка зависимостей
RUN pip install -U pip
RUN pip install playwright
RUN pip install pytest-playwright

RUN pip install -r requirements.txt
# RUN apk add --no-cache coreutils
RUN playwright install

# Копирование остальных файлов проекта
COPY . .


# Запуск 
# CMD ["pytest"]
