import pika

# Verbindung zur RabbitMQ-Instanz herstellen
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Queue deklarieren, in die die Nachricht gesendet werden soll
queue_name = 'meine_queue'
channel.queue_declare(queue=queue_name)

# Die Nachricht, die Sie senden möchten
message_body = 'Hallo, RabbitMQ!'

# Nachricht in die Queue senden
channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=message_body)

print(f" [x] Nachricht gesendet: '{message_body}'")

# Verbindung schließen
connection.close()
