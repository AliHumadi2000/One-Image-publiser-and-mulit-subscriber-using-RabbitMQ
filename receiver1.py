from pika.exchange_type import ExchangeType
import pika

# create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
# create channe from the connection
channel = connection.channel()

# declare exchange
channel.exchange_declare(exchange='imageOneToMany',
                         exchange_type=ExchangeType.fanout)

# declare queue , we won't give name cause each subscriber will have its name
queue = channel.queue_declare(queue='')
# bind the queue
channel.queue_bind(exchange='imageOneToMany', queue=queue.method.queue)


def callback(ch, method, properties, body):
    # Playload = body.decode("utf-8")
    # Playload = ast.literal_eval(Playload)
    with open("G:\Protocols\OneToMany_Image\ receive01.jpg", "wb") as fi:
        fi.write(body)
        print(type(body))
        print("Image 01 Recieved...")


channel.basic_consume(
    queue=queue.method.queue, on_message_callback=callback, auto_ack=True
)
print("Waitng for message clik CTRL+C to exit")
channel.start_consuming()
