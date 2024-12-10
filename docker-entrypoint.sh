!#/bin/sh

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Make database migrations and apply it"
python manage.py makemigrations
python manage.py migrate

echo "Starting server"
gunicorn -w 3 smart_home.wsgi -b unix:/app/nginx/wsgi.socket