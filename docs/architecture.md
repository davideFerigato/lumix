Ecco i tre documenti aggiornati per la cartella `docs/`. Puoi copiarli e incollarli direttamente nei rispettivi file.

---

## **`docs/architecture.md`** (Architettura del Progetto)

```markdown
# Architettura del Progetto `lumix`

## Panoramica

`lumix` è un'applicazione modulare e localizzata progettata per fornire una CLI (e opzionalmente una GUI) per conversioni tra unità di misura, formati, codici e altre utilità. La struttura del progetto è orientata alla scalabilità e all'aggiunta semplice di nuove funzionalità.

---

## Struttura dei Componenti

```
lumix/
├── cli.py                      # Entry point CLI (argcomplete + run_cli)
├── pyproject.toml               # Build moderno, dipendenze e entry-point
├── docs/                        # Documentazione tecnica e d'uso
├── examples/                    # Esempi di utilizzo per ogni modulo
├── scripts/                      # Script utilitari (es. update_rates.py)
├── tests/                        # Suite di test modulari
└── lumix/                        # Pacchetto principale
    ├── cli/                      # Dispatcher CLI dinamico
    │   ├── __init__.py
    │   └── main.py                # Routing lingua → modulo → parser
    ├── common/                    # Utilità condivise tra tutti i moduli
    │   ├── __init__.py
    │   ├── lang.py                 # Gestione traduzioni con gettext
    │   └── validate.py              # Funzioni di validazione comuni
    ├── temps/                      # Modulo temperature
    ├── bases/                       # Modulo basi numeriche
    ├── currency/                    # Modulo valute (con API e cache)
    ├── weight/                      # Modulo peso
    ├── length/                      # Modulo lunghezza
    ├── volume/                      # Modulo volume
    ├── area/                        # Modulo superficie
    ├── speed/                       # Modulo velocità
    ├── time/                        # Modulo tempo
    ├── energy/                      # Modulo energia
    ├── pressure/                    # Modulo pressione
    ├── power/                       # Modulo potenza
    ├── data/                        # Modulo dati digitali
    ├── bitrate/                     # Modulo bitrate
    ├── hash/                        # Modulo hash
    ├── color/                       # Modulo colori
    ├── iptools/                     # Strumenti IP
    ├── timezones/                   # Conversione tra fusi orari
    ├── date/                        # Formati data
    ├── calendar/                    # Differenza tra date
    ├── age/                         # Calcolo età
    ├── passwords/                   # Generazione password
    ├── country/                     # Codici paese
    ├── language/                    # Codici lingua
    ├── unitsymbols/                  # Simboli e nomi unità
    ├── roman/                       # Numeri romani
    ├── morse/                       # Codice Morse
    ├── timezonebot/                  # Ora in una città
    ├── spoken/                      # Numeri in parole
    └── phonetic/                    # Alfabeto fonetico NATO
```

---

## Principi Architetturali

- **Separazione delle responsabilità**: ogni funzionalità ha la sua cartella con:
  - `convert.py` – logica di conversione (funzioni pure).
  - `parser.py` – parsing degli argomenti CLI, localizzazione, chiamata a `convert`.
  - `utils.py` (opzionale) – funzioni di supporto specifiche.
  - `languages/` (opzionale) – file `.po` per traduzioni con gettext (se non si usa la mappa interna).
- **Scalabilità**: aggiungere un nuovo modulo significa creare una nuova cartella con la stessa struttura, e il dispatcher (`cli/main.py`) lo caricherà automaticamente se presente nella mappa `PARSER_MODULES`.
- **Localizzazione**: il dispatcher riceve la lingua come primo argomento e seleziona le parole chiave appropriate. Ogni modulo gestisce la propria sintassi localizzata tramite `LANG_CONFIG`.
- **Autodiscovery CLI**: il dispatcher carica dinamicamente il parser del modulo richiamando `subprocess` (o direttamente importandolo, a seconda della configurazione).
- **Test**: ogni modulo ha un corrispondente file `test_<modulo>.py` in `tests/` che verifica le funzioni di conversione e i casi limite.

---

## Flusso di Esecuzione CLI

1. L'utente lancia `lumix en temperature from C to F 36.5`.
2. `cli.py` attiva `argcomplete` e chiama `lumix.cli.main.run_cli()`.
3. `main.py`:
   - Legge `lang` (primo argomento) e `key` (secondo argomento).
   - Cerca nella mappa `PARSER_MODULES[lang][key]` il modulo corrispondente (es. `'temperature'` → `'temps.parser'`).
   - Costruisce il percorso dello script parser (`../temps/parser.py`) e lo invoca con `subprocess`, passando `lang` e il resto degli argomenti.
4. Il parser del modulo (es. `temps/parser.py`):
   - Interpreta i parametri in base alla lingua (es. `from C to F` o `da C a F`).
   - Converte il valore numerico gestendo separatore decimale (`.` o `,`).
   - Chiama la funzione `convert()` dal proprio `convert.py`.
   - Stampa il risultato formattato.
5. L'output viene mostrato all'utente.

---

## Gestione delle Traduzioni

- Le traduzioni per le parole chiave (`from/to`, `da/a`, ecc.) sono gestite tramite dizionari `LANG_CONFIG` all'interno di ogni `parser.py`.
- Per testi più lunghi (es. messaggi di errore) si usa lo stesso meccanismo.
- In futuro si potrà integrare `gettext` utilizzando le funzioni in `common/lang.py`.

---

## Testing

La suite di test si trova in `tests/`. Ogni modulo ha test unitari per le funzioni in `convert.py` (e talvolta per il parser). Per eseguirli:

```bash
pytest tests/
```

---
```
