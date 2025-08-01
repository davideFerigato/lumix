

import pytest
from unittest.mock import patch
from lumix.currency.convert import convert_currency

@patch("lumix.currency.api.fetch_exchange_rates")
def test_convert_currency(mock_fetch):
    # Simula i tassi di cambio
    mock_fetch.return_value = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.0
    }

    # EUR → USD
    converted, rate = convert_currency("EUR", "USD", 100)
    assert round(converted, 2) == round(100 / 0.85, 2)
    assert round(rate, 4) == round(1 / 0.85, 4)

    # USD → JPY
    converted, rate = convert_currency("USD", "JPY", 2)
    assert converted == 2 * 110.0
    assert rate == 110.0