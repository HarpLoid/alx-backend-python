FROM python:3.10
WORKDIR /usr/local/messaging_app

# Install MySQL client dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Make entrypoint script executable
RUN chmod +x entrypoint.sh

# Set entrypoint (this runs when container starts)
ENTRYPOINT ["./entrypoint.sh"]

# Create user so the container doesn't run on root
RUN useradd messageuser
USER messageuser

# Expose port
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#chore: add Dockerfile for messaging_app containerization
ENTRYPOINT ["docker", "build", "-t", "messaging_app_image", "."]

docker run -d -p 8000:8000 --name messaging_app_container messaging_app_image
