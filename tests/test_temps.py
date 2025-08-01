from lumix.temps.convert import c_to_f, f_to_c

def test_c_to_f():
    assert c_to_f(0) == 32
    assert c_to_f(100) == 212
    assert round(c_to_f(-40), 2) == -40

def test_f_to_c():
    assert f_to_c(32) == 0
    assert f_to_c(212) == 100
    assert round(f_to_c(-40), 2) == -40
