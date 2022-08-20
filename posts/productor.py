# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 11:25:49 2022

@author: Luis Muniz Garcia
"""

import pika

RABBIT_URL = 'amqp://guest:guest@localhost:5672/%2F'
parameters = pika.URLParameters(RABBIT_URL)
connection = pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='eventos')
channel.exchange_declare(exchange ="events", exchange_type='fanout')

def publica(method,body):
    propiedades = pika.BasicProperties(method)
    channel.basic_publish(exchange='events',
                      routing_key='pruebaNexiona',
                      body=body,properties=propiedades)
    print(" [x] Enviado: %r" % body)
    #connection.close()