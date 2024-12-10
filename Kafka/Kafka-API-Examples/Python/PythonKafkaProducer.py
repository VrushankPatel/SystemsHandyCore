# Import the KafkaProducer module
from kafka.producer import KafkaProducer
from Config import Config
from KafkaCreateTopic import create_topic_if_doesnt_exist

# Create a KafkaProducer object with the bootstrap server address
producer = KafkaProducer(bootstrap_servers=Config.bootstrap_servers)

# Define a topic name
topic = 'first-topic'

create_topic_if_doesnt_exist(topic=topic, partitions=24, replication_factor=3)

# Define a message to send
message = b'Hello, this is a message from the producer'

# Send the message to the topic
producer.send(topic, message)

# Flush the producer to ensure the message is delivered
producer.flush()

# Close the producer
producer.close()
