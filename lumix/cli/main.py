import importlib
import os
import sys
import argparse
import gettext
import argcomplete
from argcomplete.completers import ChoicesCompleter

# Mappa delle lingue disponibili
LANGUAGE_FLAGS = ["--it", "--en", "--es", "--fr", "--jp"]
LANGUAGE_CODES = {
    "--it": "it",
    "--en": "en",
    "--es": "es",
    "--fr": "fr",
    "--jp": "jp"
}

# Alias localizzati delle funzionalità
TYPE_ALIASES = {
    "temps": {
        "en": ["--temp"],
        "it": ["--temperatura", "--temp"],
        "es": ["--temperatura", "--temp"],
        "fr": ["--température", "--temp"],
        "jp": ["--温度", "--temp"]
    }
}


def run_cli():
    # Rilevamento lingua: si legge da sys.argv prima di tutto
    lang = "en"  # default
    for flag in LANGUAGE_FLAGS:
        if flag in sys.argv:
            lang = LANGUAGE_CODES[flag]
            break

    # Imposta gettext
    localedir = os.path.join(os.path.dirname(__file__), "lumix", "temps", "languages")
    gettext.bindtextdomain("messages", localedir)
    gettext.textdomain("messages")
    _ = gettext.gettext

    # Crea parser globale
    parser = argparse.ArgumentParser(description="Lumix CLI")

    # Aggiungi flags lingua (opzionali)
    for flag in LANGUAGE_FLAGS:
        parser.add_argument(flag, action="store_const", const=LANGUAGE_CODES[flag], dest="lang", help="Language")

    # Ottieni tutte le opzioni possibili di tipo in base alla lingua
    def all_type_options(language):
        result = []
        for aliases in TYPE_ALIASES.values():
            result.extend(aliases.get(language, []))
        return result

    # Aggiungi dinamicamente le opzioni delle funzionalità localizzate
    for module_name, alias_map in TYPE_ALIASES.items():
        for opt in alias_map.get(lang, []):
            parser.add_argument(
                opt,
                dest="type",
                action="store_const",
                const=module_name,
                help=_("Conversion type")
            )

    # Solo se l'utente NON ha specificato una lingua, mostra tutte le opzioni '--type' disponibili
    if not any(flag in sys.argv for flag in LANGUAGE_FLAGS):
        parser.add_argument(
            "--type",
        ).completer = ChoicesCompleter(all_type_options("en"))

    # Attiva autocompletamento
    argcomplete.autocomplete(parser)

    args, unknown = parser.parse_known_args()

    if not args.lang:
        args.lang = lang  # fallback da sys.argv

    print("[DEBUG] args:", args)
    print("[DEBUG] args.lang:", getattr(args, "lang", None))
    print("[DEBUG] args.type:", getattr(args, "type", None))
    print("[DEBUG] unknown:", unknown)

    if not getattr(args, "type", None):
        print("[ERROR] No conversion type selected.")
        print("[DEBUG] Available args:", vars(args))
        sys.exit(1)

    modname = args.type
    try:
        mod = importlib.import_module(f"lumix.{modname}.parser")
        parser2 = mod.get_parser(args.lang)
        try:
            sub_args = parser2.parse_args(unknown)
            for k, v in vars(sub_args).items():
                setattr(args, k, v)
        except SystemExit as e:
            print("[ERROR] Failed to parse sub-arguments:", unknown)
            raise e
        mod2 = importlib.import_module(f"lumix.{modname}.convert")
        mod2.run(args)
    except Exception as e:
        print("[ERROR] Exception while executing module:", e)
        sys.exit(1)