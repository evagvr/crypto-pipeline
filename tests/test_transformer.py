from processing.transformer import MessageTransformer


def test_symbol_transformed_correctly():
    transformer = MessageTransformer()
    message = {"s": "BTCUSTD", "p": "100", "q": "0.5", "T": 1234567890}

    result = transformer.transform(message)

    assert message["s"] == result["symbol"]


def test_price_converted_to_float():
    transformer = MessageTransformer()
    message = {"s": "BTCUSTD", "p": "100", "q": "0.5", "T": 1234567890}

    result = transformer.transform(message)

    assert float(message["p"]) == result["price"]


def test_timestamp_not_none():
    transformer = MessageTransformer()
    message = {"s": "BTCUSTD", "p": "100", "q": "0.5", "T": 1234567890}

    result = transformer.transform(message)

    assert result["timestamp"] is not None
