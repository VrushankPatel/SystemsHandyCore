from kafka.producer import KafkaProducer

bootstrap_servers_list = [
    'localhost:9092',
    'localhost:9093',
    'localhost:9094'
]


class Config:
    bootstrap_servers = ','.join(bootstrap_servers_list)
