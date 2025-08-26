FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

# Set the working directory
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir --root-user-action=ignore

COPY . /app/

EXPOSE 8000

# RUN chmod +x /app/entrypoint.sh

# ENTRYPOINT ["sh", "/app/entrypoint.sh"]