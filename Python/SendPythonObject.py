import pickle
import RabbitMQFunctions


my_object = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

messagedata = pickle.dumps(my_object)

RabbitMQFunctions.SendRabbitMQMessage(messagedata, "Pickle")