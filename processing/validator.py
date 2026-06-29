import logging

logger = logging.getLogger(__name__)


class MessageValidator:
    def validate(self, message: dict) -> bool:
        if message is None:
            logger.warning("Message is empty")
            return False
        if not all(key in message for key in ["s", "p", "q", "T"]):
            logger.warning("Message has missing params")
            return False
        if float(message["p"]) <= 0 or float(message["q"]) <= 0:
            logger.warning("Values are negative")
            return False
        return True
