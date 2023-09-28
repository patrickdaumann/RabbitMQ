import pika


def SendRabbitMQMessage(Message: object, Queue: str, host: str = 'localhost') -> bool:

    # Verbindung zur RabbitMQ-Instanz herstellen
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    # Queue deklarieren, in die die Nachricht gesendet werden soll
    queue_name = Queue
    channel.queue_declare(queue=queue_name)

    # Die Nachricht, die Sie senden möchten
    message_body = Message

    # Nachricht in die Queue senden
    channel.basic_publish(exchange='',
                        routing_key=queue_name,
                        body=message_body)

    # Verbindung schließen
    connection.close()

    return True


