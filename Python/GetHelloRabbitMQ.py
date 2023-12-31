import pika

# Verbindung zur RabbitMQ-Instanz herstellen
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Queue deklarieren, aus der Sie die Nachrichten abrufen möchten
queue_name = 'meine_queue'
channel.queue_declare(queue=queue_name)

# Funktion zum Verarbeiten von empfangenen Nachrichten
def callback(ch, method, properties, body):
    print(f" [x] Nachricht erhalten: {body}")

# Die Queue überwachen und Nachrichten empfangen
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Warten auf Nachrichten. Drücken Sie STRG+C zum Beenden.')
channel.start_consuming()
