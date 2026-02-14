from lumix.morse.convert import text_to_morse, morse_to_text

def test_text_to_morse():
    assert text_to_morse("SOS") == "... --- ..."
    assert text_to_morse("CIAO") == "-.-. .. .- ---"

def test_morse_to_text():
    assert morse_to_text("... --- ...") == "SOS"
    assert morse_to_text("-.-. .. .- ---") == "CIAO"

