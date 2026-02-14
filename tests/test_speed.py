from lumix.speed.convert import convert

def test_convert():
    assert round(convert(130, "km/h", "mph"), 2) == 80.78
    assert convert(10, "m/s", "km/h") == 36

