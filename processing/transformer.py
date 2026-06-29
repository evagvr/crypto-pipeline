from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class MessageTransformer:
    def transform(self, message: dict) -> dict:
        new_message = dict()
        new_message["symbol"] = message["s"]
        new_message["price"] = float(message["p"])
        new_message["quantity"] = float(message["q"])
        new_message["timestamp"] = datetime.fromtimestamp(message["T"] / 1000)
        logger.info("Transformed message")
        return new_message
