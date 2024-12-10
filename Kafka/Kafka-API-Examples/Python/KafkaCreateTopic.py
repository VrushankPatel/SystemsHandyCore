# Import the KafkaAdminClient and NewTopic modules
from kafka.admin import KafkaAdminClient, NewTopic
from Config import Config

# Create a KafkaAdminClient object with the bootstrap server address
admin_client = KafkaAdminClient(bootstrap_servers=Config.bootstrap_servers)


def create_kafka_topic(topic, partitions, replication_factor):
    new_topic = NewTopic(name=topic, num_partitions=partitions, replication_factor=replication_factor)

    # Create the topic using the admin client
    admin_client.create_topics([new_topic])

    # Print a confirmation message
    print(f'Topic {topic} created successfully')


def does_topic_exist(topic):
    topics_list = admin_client.list_topics()
    return topic in topics_list


def create_topic_if_doesnt_exist(topic, partitions, replication_factor):
    if does_topic_exist(topic):
        print(f'Topic {topic} already exists')
    else:
        create_kafka_topic(topic=topic, partitions=partitions, replication_factor=replication_factor)


# Let's check if first-topic exists, if doesn't then create one
if __name__ == '__main__':
    topic = "first-topic"
    create_topic_if_doesnt_exist(topic=topic, partitions=24, replication_factor=3)

    admin_client.close()
