web:python manage.py runserver
web: gunicorn mysite.wsgi:application --log-file -
heroku ps:scale web=1
