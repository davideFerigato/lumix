

# Architettura del Progetto `lumix`

## Panoramica

`lumix` è un'applicazione modulare e localizzata progettata per fornire una CLI (e opzionalmente una GUI) per la conversione tra unità (temperatura, basi numeriche, valute, ecc.). La struttura del progetto è orientata alla scalabilità e all'aggiunta semplice di nuove funzionalità.

---

## Struttura dei Componenti

```
lumix/
├── cli.py                  # Entry point CLI
├── pyproject.toml          # Build moderno e entry-point
├── docs/                   # Documentazione tecnica e d'uso
├── examples/               # Esempi di utilizzo
├── scripts/                # Script utilitari
├── tests/                  # Suite di test modulari
└── lumix/                  # Pacchetto principale
    ├── cli/                # Dispatcher CLI dinamico
    ├── common/             # Utilità condivise e scheletro moduli
    ├── temps/              # Modulo temperatura (convert/parser/utils/lang)
    ├── bases/              # Modulo basi numeriche (convert/parser/utils/lang)
    ├── currency/           # Modulo valute (convert/parser/utils/lang/api/cache)
    └── gui/                # Interfaccia grafica Tkinter
```

---

## Principi Architetturali

- **Separazione delle responsabilità**: ogni funzionalità ha la sua cartella con parser, logica, traduzioni e utility.
- **Scalabilità**: è possibile aggiungere nuove funzionalità copiando la struttura base fornita da `common/`.
- **Localizzazione**: ogni modulo ha le proprie traduzioni (`languages/`).
- **Autodiscovery CLI**: il dispatcher carica dinamicamente solo i moduli che definiscono un parser.

---

## Esecuzione

- CLI: `lumix --type temp --from C --to F 100`
- GUI: `python -m lumix.gui.app`

---

## Testing

I test sono definiti nella cartella `tests/` e organizzati per funzionalità (`test_temps.py`, `test_bases.py`, ecc.).