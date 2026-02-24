import pytest
from unittest.mock import patch
from lumix.currency.convert import convert_currency

@patch("lumix.currency.api.fetch_exchange_rate")
def test_convert_currency(mock_fetch):
    # Simula il tasso di cambio: per EUR → USD, la funzione restituisce amount * rate
    # Quindi per 100 EUR, se il tasso è 1.18, restituisce 118.0
    mock_fetch.return_value = 118.0  # 100 EUR * 1.18 USD/EUR

    converted = convert_currency(100, "EUR", "USD")
    assert converted == 118.0

    # Test con valute uguali
    assert convert_currency(50, "EUR", "EUR") == 50.0