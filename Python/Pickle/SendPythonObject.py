import pickle
from RabbitMQFunctions import *
from Person import Person


p1 = Person("Peter Müller", 45, "Berlin")
messagedata = pickle.dumps(p1)

SendRabbitMQMessage(messagedata, "Pickle")
