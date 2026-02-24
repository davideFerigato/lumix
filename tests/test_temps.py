from lumix.temps.convert import convert

def test_c_to_f():
    assert convert(0, 'C', 'F') == 32
    assert convert(100, 'C', 'F') == 212
    assert round(convert(-40, 'C', 'F'), 2) == -40

def test_f_to_c():
    assert convert(32, 'F', 'C') == 0
    assert convert(212, 'F', 'C') == 100
    assert round(convert(-40, 'F', 'C'), 2) == -40