# Verwende das offizielle RabbitMQ-Basisimage von Docker Hub
FROM rabbitmq

# Freigegebene Ports
EXPOSE 5672 15672

# Aktiviere das Management-Plugin
RUN rabbitmq-plugins enable rabbitmq_management

# Standard-Befehl zum Starten von RabbitMQ
CMD ["rabbitmq-server"]
