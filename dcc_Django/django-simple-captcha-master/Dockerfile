# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install to a wheelhouse
COPY requirements.txt .
RUN pip wheel --wheel-dir=/wheels -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt ke image
COPY requirements.txt .

# Copy wheels and install
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --find-links=/wheels --no-index -r requirements.txt

# Copy project files
COPY . /app/

WORKDIR /app/testproject

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]