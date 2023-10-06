import pika
from random import randint
from time import sleep

# Verbindung zur RabbitMQ-Instanz herstellen
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# Queue deklarieren, in die die Nachricht gesendet werden soll
queue_name = 'PerformanceTest'
channel.queue_declare(queue=queue_name)



while True:
    # Die Nachricht, die Sie senden möchten
    message_body = str(randint(1, 10000000000))
    
    # Nachricht in die Queue senden
    channel.basic_publish(exchange='',
                        routing_key=queue_name,
                        body=message_body)
    print(f"Nachricht gesendet: '{message_body}'")

# Verbindung schließen
connection.close()
