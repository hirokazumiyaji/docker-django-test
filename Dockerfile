FROM python:2.7
ADD app /app
WORKDIR /app
RUN pip install django redis mysqlclient
CMD python manage.py test
