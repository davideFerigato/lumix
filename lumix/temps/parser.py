import argparse
import os
from lumix.common.lang import get_translator

def get_parser(lang="en"):
    print("[DEBUG] Parsed lang =", lang)

    import sys
    from argcomplete.completers import ChoicesCompleter

    # Determina la lingua guardando sys.argv se possibile
    for i, arg in enumerate(sys.argv):
        if arg in ["--it", "--es", "--fr", "--jp", "--en"]:
            lang = arg[2:]
            break

    # Set up i18n
    localedir = os.path.join(os.path.dirname(__file__), "languages")
    _ = get_translator("messages", lang, localedir)

    # Localized option names based on selected language
    localized_flags = {
        "en": {"type": "--temp", "from": "--from", "to": "--to"},
        "it": {"type": "--temperatura", "from": "--da", "to": "--a"},
        "es": {"type": "--temperatura", "from": "--de", "to": "--a"},
        "fr": {"type": "--température", "from": "--de", "to": "--à"},
        "jp": {"type": "--温度", "from": "--から", "to": "--へ"},
    }

    # Fallback to English if unsupported
    flags = localized_flags.get(lang, localized_flags["en"])

    parser = argparse.ArgumentParser(description=_("Temperature converter"))
    # Use constant value for the 'type' argument to avoid requiring a value
    parser.add_argument(flags["type"], dest="type", action="store_const", const="temps", help=_("Conversion type"))
    arg_from = parser.add_argument(flags["from"], dest="src", required=True, help=_("Source unit"))
    arg_from.completer = ChoicesCompleter(["C", "F", "K"])
    arg_to = parser.add_argument(flags["to"], dest="dst", required=True, help=_("Target unit"))
    arg_to.completer = ChoicesCompleter(["C", "F", "K"])
    parser.add_argument("value", type=float, help=_("Value to convert"))

    # Autocomplete registration
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    # Debug outputs
    print("[DEBUG] All parser actions:")
    for action in parser._actions:
        print("  ", action.option_strings)

    return parser