python3 src/manage.py makemigrations
python3 src/manage.py migrate
python3 src/manage.py collectstatic --no-input
gunicorn -b 0.0.0.0:8765 src/main.wsgi --reload