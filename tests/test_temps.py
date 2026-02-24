from lumix.temps.convert import convert

def test_c_to_f():
    assert convert(0, 'C', 'F') == "32.00"
    assert convert(100, 'C', 'F') == "212.00"
    assert convert(-40, 'C', 'F') == "-40.00"

def test_f_to_c():
    assert convert(32, 'F', 'C') == "0.00"
    assert convert(212, 'F', 'C') == "100.00"
    assert convert(-40, 'F', 'C') == "-40.00"