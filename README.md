

# lumix

[![CI](https://github.com/davideFerigato/lumix/actions/workflows/ci.yml/badge.svg)](https://github.com/davideFerigato/lumix/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/docker-supported-blue)](https://github.com/USERNAME/lumix#docker)
[![PyPI](https://img.shields.io/pypi/v/lumix.svg)](https://pypi.org/project/lumix)

**`lumix` è una CLI modulare, localizzata e pronta a espandersi, per la conversione tra unità.**

Supporta:

⚖️ Conversioni fisiche
- **weight**: Converte tra chilogrammi, libbre, once, grammi.  
  Esempio: `lumix en weight from kg to lb 75` → converte 75 kg in libbre.  
- **length**: Converte tra metri, piedi, pollici, miglia, chilometri.  
  Esempio: `lumix en length from m to ft 1.80` → converte 1.80 m in piedi.  
- **volume**: Converte tra litri, millilitri, metri cubi, galloni.  
  Esempio: `lumix en volume from l to gal 2` → 2 litri in galloni.  
- **area**: Converte tra metri quadrati, piedi quadrati, acri, ettari.  
  Esempio: `lumix en area from m² to ft² 50` → 50 m² in ft².  
- **speed**: Converte tra km/h, mph (miglia orarie), m/s.  
  Esempio: `lumix en speed from km/h to mph 130` → velocità in miglia orarie.  
- **time**: Converte tra secondi, minuti, ore, giorni, settimane.  
  Esempio: `lumix en time from days to hours 3` → 3 giorni in ore.  
- **energy**: Converte tra joule, calorie, kilowattora, BTU.  
  Esempio: `lumix en energy from J to kcal 500`  
- **pressure**: Converte tra pascal, bar, atm, mmHg, psi.  
  Esempio: `lumix en pressure from bar to psi 2`  
- **power**: Converte tra watt, cavalli, kilowatt.  
  Esempio: `lumix en power from W to hp 1000`

⸻

💻 **Utility Digitali**
- **data**: Converte unità digitali tra byte, KB, MB, GB, TB, bit, nibble.  
  Esempio: `lumix en data from MB to GB 1500`  
- **bitrate**: Converte bitrate tra Kbps, Mbps, Gbps, Bps.  
  Esempio: `lumix en bitrate from Mbps to Kbps 100`  
- **hash**: Calcola hash (MD5, SHA1, SHA256) da una stringa.  
  Esempio: `lumix en hash sha256 "hello world"`  
- **color**: Converte tra formati colore RGB, HEX, HSL, CMYK.  
  Esempio: `lumix en color from rgb to hex 255,255,255`  
- **iptools**: Strumenti IP: calcola range da CIDR, subnet, classi.  
  Esempio: `lumix en iptools cidr-to-range 192.168.1.0/24`  
- **timezones**: Converte date/orari tra fusi orari.  
  Esempio: `lumix en timezones from Europe/Rome to Asia/Tokyo "2025-08-02 14:00"`

⸻

📅 **Data e Tempo**
- **date**: Converte tra formati data (US, IT, ISO, UNIX).  
  Esempio: `lumix en date from us to iso 08/02/2025`  
- **calendar**: Calcola differenze tra date, giorno della settimana, ecc.  
  Esempio: `lumix en calendar diff 2025-01-01 2025-12-31`  
- **age**: Calcola l’età da una data di nascita.  
  Esempio: `lumix en age from "1990-05-23"`

⸻

🔐 **Sicurezza e Crittografia**
- **passwords**: Genera password sicure con lunghezza e criteri.  
  Esempio: `lumix en passwords generate length 16 symbols true`

⸻

🌐 **Geo, Lingue, Codici**
- **country**: Converte codice ISO paese ↔ nome ↔ bandiera.  
  Esempio: `lumix en country from code to name IT`  
- **language**: Converte nome lingua ↔ codice ISO.  
  Esempio: `lumix en language from name to iso "italian"`  
- **unitsymbols**: Trova simboli unità ↔ nome ↔ tipo.  
  Esempio: `lumix en unitsymbols from W to "unit name"`

⸻

🧠 **Bonus Creativi**
- **roman**: Converte numeri arabi ↔ numeri romani.  
  Esempio: `lumix en roman from 2025 → MMXXV`  
- **morse**: Converte testo ↔ codice Morse.  
  Esempio: `lumix en morse to-text "... --- ..."`  
- **timezonebot**: Bot da terminale che risponde con l’orario in una città.  
  Esempio: `lumix en timezonebot what-time Tokyo`  
- **spoken**: Converte numeri in parole.  
  Esempio: `lumix en spoken from 123456 → “centoventitré mila…”`  
- **phonetic**: Codifica testo in alfabeto fonetico NATO.  
  Esempio: `lumix en phonetic for CIAO → “Charlie India Alpha Oscar”`

---

## Installazione

### Da PyPI

```bash
pip install lumix
```

### Da sorgenti

```bash
git clone https://github.com/USERNAME/lumix.git
cd lumix
python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install -e .
```

---

## Uso CLI

```bash
lumix --help
```

### Esempi

```bash
lumix --type temp --from C --to F 100
lumix --type base --from dec --to hex 42
lumix --type currency --from EUR --to USD 50
```

### Localizzazione automatica

```bash
LANG=es lumix --tipo temp --de C --a F 30
LANG=fr lumix --from C --to F 25
```

---

## GUI

```bash
python -m lumix.gui.app
```

---

## Autocompletamento

```bash
pip install argcomplete
eval "$(register-python-argcomplete lumix)"
```

Aggiungi al tuo `~/.bashrc` o `~/.zshrc` per renderlo permanente:

```bash
autoload -U compinit && compinit
eval "$(register-python-argcomplete lumix)"
```

---

## Docker

```bash
docker build -t lumix .
docker run --rm lumix --type temp --from C --to K 25
```

---

## Testing

```bash
pytest
```

---

## Contribuire

1. Fork & clone  
2. Crea branch `feature/x`  
3. Aggiungi test e traduzioni  
4. Apri una Pull Request

---

## Licenza

MIT © DMF