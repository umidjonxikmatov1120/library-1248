web : gunicorn 'core.wsgi'
web: gunicorn core.wsgi --log-file -
#or works good with external database
web: python manage.py migrate && gunicorn core.wsgi