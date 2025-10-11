#!/bin/sh

# Try to connect to the DB until it responds
python - <<END
import socket, time, os
host = os.getenv("MYSQL_HOST", "db")
port = int(os.getenv("MYSQL_PORT", 3306))
while True:
    try:
        socket.create_connection((host, port))
        print("Database ready!")
        break
    except OSError:
        print("Waiting for database...")
        time.sleep(1)
END

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# (Optional) Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# (Optional) Create superuser if not exists
echo "Creating superuser (if not already created)..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@mail.com', 'admin')
EOF

# Start server
echo "Starting server..."
gunicorn messaging_app.wsgi:application --bind 0.0.0.0:8000
