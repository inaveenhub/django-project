!/bin/bash

PORT=${PORT:-8000}

echo "Django migrate"
python manage.py migrate --noinput
echo "Run Gunicorn"
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 config.wsgi:application -k uvicorn.workers.UvicornWorker
