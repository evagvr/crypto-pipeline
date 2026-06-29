import logging
import json
from kafka import KafkaProducer

logger = logging.getLogger(__name__)


class KafkaProducerClient:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )
        self.topic = topic

    def send(self, message: str):
        try:
            self.producer.send(self.topic, message)
            logger.info("Message was sent")
        except Exception as e:
            logger.error(e)

    def close(self):
        self.producer.close()
        logger.info("Kafka producer was closed")
