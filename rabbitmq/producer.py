#!/usr/bin/python

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()
channel.queue_declare(queue='hello')

count = 10
i = 1
while i <= count:
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
    i += 1

print "Send \"Hello \"World"

conn.close()