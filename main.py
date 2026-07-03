import asyncio
import os
from ingestion.binance_websocket import BinanceWebsocketClient
from ingestion.kafka_producer import KafkaProducerClient
from processing.validator import MessageValidator
from processing.transformer import MessageTransformer
from storage.repository import TradeRepository

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")


def on_message(message):
    if not validator.validate(message):
        return
    new_message = transformer.transform(message)
    producer.send(new_message)
    repository.save_trade(new_message)


connection_string = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
repository = TradeRepository(connection_string=connection_string)
validator = MessageValidator()
transformer = MessageTransformer()
producer = KafkaProducerClient(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, topic="trades"
)

if __name__ == "__main__":
    client = BinanceWebsocketClient(
        symbols=["btcusdt", "ethusdt"], on_message=on_message
    )
    asyncio.run(client.connect())
