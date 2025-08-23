# Docker Compose.
-----------------
services:
  # Redis service
  redis:
    image: redis:7-alpine
    container_name: nora-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

  # FastAPI application
  app:
    build: .
    container_name: nora-app
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app/app
    depends_on:
      redis:
        condition: service_healthy
    env_file:
      - .env
      - .env.docker
    restart: unless-stopped

  # Celery Worker
  celery:
    build: .
    container_name: nora-celery
    command: celery -A app.task.c_app worker --loglevel=info
    volumes:
      - ./app:/app/app
    depends_on:
      redis:
        condition: service_healthy
    env_file:
      - .env
      - .env.docker
    restart: unless-stopped

  # Flower for monitoring Celery
  flower:
    build: .
    container_name: nora-flower
    command: celery -A app.task.c_app flower --port=5555
    ports:
      - "5555:5555"
    volumes:
      - ./app:/app/app
    depends_on:
      redis:
        condition: service_healthy
    env_file:
      - .env
      - .env.docker
    restart: unless-stopped

volumes:
  redis_data:
