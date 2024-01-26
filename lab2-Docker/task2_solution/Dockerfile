# Используем базовый образ PyTorch
FROM pytorch/pytorch:latest

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6

# Устанавливаем необходимые библиотеки Python
RUN pip install numpy opencv-python timm pillow torch torchvision matplotlib 

# Копируем все файлы из текущей директории в образ
COPY input /usr/local/Dev/input

# Устанавливаем рабочую директорию
WORKDIR /usr/local/Dev
