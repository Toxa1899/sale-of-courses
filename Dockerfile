# Используйте официальный Python образ
FROM python:3.9

# Установите рабочий каталог
WORKDIR /app

# Установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте все файлы проекта
COPY . .

# Экспонируйте порт
EXPOSE 8000

# Команда по умолчанию для запуска сервера Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
