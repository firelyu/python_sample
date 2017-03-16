#!/usr/bin/python

import pika

def callback(ch, method, properties, body):
    print "[%s] receive >%r<" % (method, body)

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
channel.start_consuming()