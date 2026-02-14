from lumix.calendar.convert import date_diff

def test_date_diff():
    assert date_diff("2025-01-01", "2025-12-31") == 364
    assert date_diff("2024-01-01", "2024-12-31") == 365

