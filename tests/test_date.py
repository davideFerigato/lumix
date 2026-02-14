from lumix.date.convert import convert_date

def test_convert_date():
    assert convert_date("08/02/2025", "us", "iso") == "2025-02-08"
    assert convert_date("2025-02-08", "iso", "eu") == "08/02/2025"

