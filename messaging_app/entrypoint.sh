#!/bin/sh

# echo "Waiting for database..."
# until nc -z -v -w30 "$MYSQL_HOST" "$MYSQL_PORT"; do
#   echo "Waiting for database connection..."
#   sleep 2
# done
# echo "Database ready!"

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser (if not already created)..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@mail.com', 'admin')
EOF

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
