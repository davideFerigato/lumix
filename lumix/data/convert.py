"""
Funzioni di conversione per dati digitali (base 10).
Fattori: 1 KB = 1000 B, 1 MB = 1000 KB, ecc.
"""

_TO_BYTES = {
    "b": 1.0,
    "byte": 1.0,
    "kb": 1000.0,
    "kbyte": 1000.0,
    "mb": 1000.0 * 1000.0,
    "mbyte": 1000.0 * 1000.0,
    "gb": 1000.0 * 1000.0 * 1000.0,
    "gbyte": 1000.0 * 1000.0 * 1000.0,
    "tb": 1000.0 * 1000.0 * 1000.0 * 1000.0,
    "tbyte": 1000.0 * 1000.0 * 1000.0 * 1000.0,
}

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converte un valore da un'unità di dati a un'altra.

    Args:
        value: Valore numerico da convertire.
        from_unit: Unità di partenza (es. 'mb', 'gb').
        to_unit: Unità di arrivo.

    Returns:
        float: Valore convertito.
    """
    from_norm = from_unit.lower().replace(' ', '')
    to_norm = to_unit.lower().replace(' ', '')

    if from_norm not in _TO_BYTES or to_norm not in _TO_BYTES:
        raise ValueError(f"Unità non supportata: {from_unit} o {to_unit}")

    # Converti in byte
    value_in_bytes = value * _TO_BYTES[from_norm]
    # Converti da byte a unità destinazione
    result = value_in_bytes / _TO_BYTES[to_norm]
    return result