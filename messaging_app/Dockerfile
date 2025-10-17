FROM python:3.10
WORKDIR /usr/local/messaging_app

# Install MySQL client dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    sqlite3 \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Make entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose port
EXPOSE 8000

# Create user so the container doesn't run on root
RUN useradd messageuser
RUN chown -R messageuser:messageuser /usr/local/messaging_app
USER messageuser

# Set entrypoint (this runs when container starts)
ENTRYPOINT ["./entrypoint.sh"]

# docker run -d -p 8000:8000 --name messaging_app_container messaging_app_image
