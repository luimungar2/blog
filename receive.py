# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:16:49 2022

@author: Luis Muniz Garcia
"""
RABBIT_URL = 'amqp://guest:guest@localhost:5672/%2F'
import pika, sys, os, json, django, logging
#from posts.models import Post

parameters = pika.URLParameters(RABBIT_URL)
connection = pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='eventos')
channel.queue_bind(queue='eventos', exchange='events', routing_key='pruebaNexiona')

def callback(ch, method, properties, body):
    print(" [x] Evento Recibido: ",body.decode())
    print("Guardando log")
    logging.basicConfig(filename="logs/log.txt", level=logging.INFO,
                    format="%(asctime)s %(message)s", filemode="a")
    logging.info(body.decode())
    
    #post = Post.objects.get(id=id)
    #post.hit_count_generic = post.hit_count_generic +1
    #post.save()
    if "Not counted" in body.decode():
        print("Contador de visitas no incrementado")
    else:
        print("Contador de visita incrementado")
    
channel.basic_consume(queue='eventos', on_message_callback=callback, auto_ack=True)
print(' [*] Consumiendo mensajes. Pulsa CTRL+C para salir.')
channel.start_consuming()
print("[x] Mensaje consumido.")
#channel.close()

# if __name__ == '__main__':
#     try:
#         callback()
#     except KeyboardInterrupt:
#         print('Abortado.')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
