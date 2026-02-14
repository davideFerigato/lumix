from datetime import datetime

FORMAT_MAP = {
    'us': '%m/%d/%Y',
    'iso': '%Y-%m-%d',
    'eu': '%d/%m/%Y',
    'jp': '%Y年%m月%d日',
}

def convert_date(date_str: str, from_format: str, to_format: str) -> str:
    """
    Converte una data da un formato all'altro.

    Args:
        date_str: stringa della data
        from_format: codice formato sorgente ('us', 'iso', 'eu', 'jp')
        to_format: codice formato destinazione

    Returns:
        stringa della data nel formato destinazione
    """
    if from_format not in FORMAT_MAP or to_format not in FORMAT_MAP:
        raise ValueError(f"Formato non supportato: {from_format} o {to_format}")

    dt = datetime.strptime(date_str, FORMAT_MAP[from_format])
    return dt.strftime(FORMAT_MAP[to_format])