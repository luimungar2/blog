# Django-Hitcount-RabbitMQ web service
Simple Blog App using django-hitcount and RabbitMQ

## 1. Get Started (locally)

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


After that, run the RabbitMQ server. Log as an admin and check out the queues tab.


On the next step, run the "receive.py" script as following:

```
python3 receive.py
```

Then, open the browser and switch between this 2 url: http://127.0.0.1:8000/primer-post and http://127.0.0.1:8000/segundo-post. 

## 2. Checking the main functionality

![Prueba1](https://user-images.githubusercontent.com/61665330/185766892-b0d96636-8a7c-499f-9d53-77fd9c804bab.JPG)

![Prueba2](https://user-images.githubusercontent.com/61665330/185766917-4cc1ae52-8d47-4ca5-82de-e5f987ba55d8.JPG)


You can log in as an admin and check all the info it provides..
![Prueba5](https://user-images.githubusercontent.com/61665330/185766942-99dfd353-8006-4a41-92e5-0e1e4c66e528.JPG)

You can either check the hitcount per page:
![prueba4](https://user-images.githubusercontent.com/61665330/185766943-5037b91c-4af8-4036-8d27-4f34b86ccd61.JPG)

or even see which user has posted some content, with its IP address.  

![Prueba3](https://user-images.githubusercontent.com/61665330/185767096-a469b9a9-90f9-40ea-9926-bcf9bd11a68a.JPG)


Whenever you swap between the primer-post and segundo-post url, you should get the following output on the django running terminal: 
![Prueba9](https://user-images.githubusercontent.com/61665330/185767203-6b0e00fe-90d5-4681-b955-ca0449b29c9c.JPG)

On the other hand, you should get a similar output on the receiver running terminal:
![Prueba6](https://user-images.githubusercontent.com/61665330/185767253-ed656c6c-e9bf-4cef-90a1-6fdb53223b4c.JPG)

This way, whenever an event occurs, it is registered by the RabbitMQ system, queueing the message and saving that log in the log folder.

## Managing interfaces

Finally, you can monitor changes in the web interface of the RabbitMQ running server as shown below:
![Prueba7](https://user-images.githubusercontent.com/61665330/185767344-3dfab140-cdd3-4256-8a08-fad2984ec703.JPG)


![Prueba8](https://user-images.githubusercontent.com/61665330/185767346-c07c3c21-9ad0-4f6b-9e49-87c754a956a5.JPG)


