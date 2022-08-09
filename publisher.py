import pika
from pika.exchange_type import ExchangeType

# create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# create channe from the connection
channel = connection.channel()

# declare the name of the queue
channel.exchange_declare(exchange='imageOneToMany',
                         exchange_type=ExchangeType.fanout)


class Image(object):
    __slots__ = ['filename']

    def __init__(self, filename):
        self.filename = filename

    @property
    def get(self):
        with open(self.filename, 'rb') as im:
            data = im.read()
        return data


# create object from the class
image = Image(filename="G:\Protocols\OneToMany_Image\mine.jpg")
data = image.get
channel.basic_publish(exchange='imageOneToMany', routing_key='', body=data)

connection.close()
