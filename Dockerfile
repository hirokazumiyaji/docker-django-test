FROM python:2.7
ADD app /app
WORKDIR /app
RUN pip install django redis
CMD cd /app && python manage.py test
