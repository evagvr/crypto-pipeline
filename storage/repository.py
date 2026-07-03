from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from storage.models import Base, Trade
import logging

logger = logging.getLogger(__name__)


class TradeRepository:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def save_trade(self, trade_data: dict):
        try:
            session = self.session()
            new_trade = Trade(**trade_data)
            session.add(new_trade)
            session.commit()
            logger.info("Trade has been saved succesfully")
        except Exception as e:
            logger.error(e)
        finally:
            session.close()

    def get_trades(self):
        try:
            session = self.session()
            result = session.query(Trade).all()
            logger.info("Trades have been obtained")
            return result
        except Exception as e:
            logger.error(e)
        finally:
            session.close()
