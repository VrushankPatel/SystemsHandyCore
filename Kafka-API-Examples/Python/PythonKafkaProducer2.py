# Import the KafkaProducer module
from kafka.producer import KafkaProducer
from Config import Config
from KafkaCreateTopic import create_topic_if_doesnt_exist
from RandomStrings import generate_random_str

# Create a KafkaProducer object with the bootstrap server address
producer = KafkaProducer(bootstrap_servers=Config.bootstrap_servers)

# Define a topic name
topic = 'first-topic'

create_topic_if_doesnt_exist(topic=topic, partitions=24, replication_factor=3)

for i in range(25000):
    random_str = generate_random_str(4056)
    message = bytes(f"The KEY [ {i} ] : {random_str}", 'utf-8')
    print(f"producing message ", i, f" -> {random_str}")
    producer.send(topic, message)
    producer.flush()

# Close the producer
producer.close()
