from lumix.common.validate import validate_number, validate_temp
from lumix.common.lang import get_translator
import os
import argparse

def c_to_f(c): return c * 9 / 5 + 32
def f_to_c(f): return (f - 32) * 5 / 9

def run(args):
    lang = os.environ.get("LANG", "en")[:2]
    localedir = os.path.join(os.path.dirname(__file__), "languages")
    _ = get_translator("messages", lang, localedir)

    val = validate_number(args.value)
    src = validate_temp(args.src)
    dst = validate_temp(args.dst)

    if src == "C" and dst == "F":
        result = c_to_f(val)
        unit = "°F"
    elif src == "F" and dst == "C":
        result = f_to_c(val)
        unit = "°C"
    elif src == "C" and dst == "K":
        result = val + 273.15
        unit = "K"
    elif src == "K" and dst == "C":
        result = val - 273.15
        unit = "°C"
    elif src == "F" and dst == "K":
        result = f_to_c(val) + 273.15
        unit = "K"
    elif src == "K" and dst == "F":
        result = c_to_f(val - 273.15)
        unit = "°F"
    else:
        raise ValueError(_("Conversion not supported"))

    print(_("{val} {src} → {res:.2f} {unit}").format(
        val=val, src=src, res=result, unit=unit
    ))