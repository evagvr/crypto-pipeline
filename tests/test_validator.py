from processing.validator import MessageValidator


def test_valid_message_returns_true():
    validator = MessageValidator()
    message = {"s": "BTCUSTD", "p": "100", "q": "0.5", "T": 1234567890}

    result = validator.validate(message)

    assert result


def test_none_message_returns_false():
    validator = MessageValidator()
    message = {}

    result = validator.validate(message)

    assert not result


def test_missing_fields_returns_false():
    validator = MessageValidator()
    message = {"s": "BTCUSTD", "p": "100", "q": "0.5"}

    result = validator.validate(message)

    assert not result


def test_negative_price_returns_false():
    validator = MessageValidator()
    message = {"s": "BTCUSTD", "p": "-100", "q": "0.5", "T": 1234567890}

    result = validator.validate(message)

    assert not result
