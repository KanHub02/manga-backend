python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input
gunicorn -b 0.0.0.0:8666 core.wsgi --reload