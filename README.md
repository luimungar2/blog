# Django-Hitcount-Tutorial
Simple Blog App using django-hitcount and RabbitMQ

## Get Started (locally)

Install dependencies by following commad:

```
pip3 install requirements.txt
```
and run the project

```
python3 manage.py makemigrations posts
python3 manage.py migrate
python3 manage.py runserver
```
After that, run the RabbitMQ server.

On the next step, run the "receive.py" script and then, try to visit the following url: http://127.0.0.1:8000/primer-post . You should get a similar output like the ones in the screenshots folder.
