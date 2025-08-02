# lumix 🚀

&#x20;&#x20;

**lumix** è una potente **CLI modulare** e **localizzata**, progettata per gestire conversioni tra unità e strumenti di utilità.

## 📋 Somario

- [✨ Caratteristiche](#-caratteristiche)
- [⚙️ Installazione](#️-installazione)
- [🚀 Uso CLI](#-uso-cli)
- [🔍 Esempi dettagliati](#-esempi-dettagliati)
- [⏱️ Autocompletamento](#️-autocompletamento)
- [🏗️ Docker](#️-docker)
- [🧪 Testing](#-testing)
- [🤝 Contribuire](#-contribuire)
- [📝 Licenza](#-licenza)

---

## ✨ Caratteristiche

- 🌐 **Localizzazione**: supporta **it**, **en**, **es**, **fr**, **jp**.
- ⚙️ **CLI modulare**: aggiungi facilmente nuovi parser, senza cambiare il core.
- 🛠️ **Conversioni fisiche**, **utility digitali**, **date/tempo**, **sicurezza**, **geo**, **bonus creativi**.
- 🖥️ **GUI opzionale** via Tkinter.

---

## ⚙️ Installazione

### Da PyPI

```bash
pip install lumix
```

### Da sorgenti

```bash
git clone https://github.com/davideFerigato/lumix.git
cd lumix
python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install -e .
```

---

## 🚀 Uso CLI

```bash
lumix --help
```

---

## 🔍 Esempi dettagliati

### ⚖️ Conversioni fisiche

- **weight**: `lumix en weight from kg to lb 75` → 75 kg in libbre.
- **length**: `lumix en length from m to ft 1.80` → 1.80 m in piedi.
- **volume**: `lumix en volume from l to gal 2` → 2 L in galloni.
- **area**: `lumix en area from m² to ft² 50` → 50 m² in ft².
- **speed**: `lumix en speed from km/h to mph 130` → km/h → mph.
- **time**: `lumix en time from days to hours 3` → 3 giorni in ore.
- **energy**: `lumix en energy from J to kcal 500`
- **pressure**: `lumix en pressure from bar to psi 2`
- **power**: `lumix en power from W to hp 1000`

### 💻 Utility Digitali

- **data**: `lumix en data from MB to GB 1500`
- **bitrate**: `lumix en bitrate from Mbps to Kbps 100`
- **hash**: `lumix en hash sha256 "hello world"`
- **color**: `lumix en color from rgb to hex 255,255,255`
- **iptools**: `lumix en iptools cidr-to-range 192.168.1.0/24`
- **timezones**: `lumix en timezones from Europe/Rome to Asia/Tokyo "2025-08-02 14:00"`

### 📅 Data e Tempo

- **date**: `lumix en date from us to iso 08/02/2025`
- **calendar**: `lumix en calendar diff 2025-01-01 2025-12-31`
- **age**: `lumix en age from "1990-05-23"`

### 🔐 Sicurezza e Crittografia

- **passwords**: `lumix en passwords generate length 16 symbols true`

### 🌐 Geo, Lingue, Codici

- **country**: `lumix en country from code to name IT`
- **language**: `lumix en language from name to iso "italian"`
- **unitsymbols**: `lumix en unitsymbols from W to "unit name"`

### 🧠 Bonus Creativi

- **roman**: `lumix en roman from 2025 → MMXXV`
- **morse**: `lumix en morse to-text "... --- ..."`
- **timezonebot**: `lumix en timezonebot what-time Tokyo`
- **spoken**: `lumix en spoken from 123456 → "centoventitré mila…"`
- **phonetic**: `lumix en phonetic for CIAO → "Charlie India Alpha Oscar"`

---

## ⏱️ Autocompletamento

```bash
pip install argcomplete
eval "$(register-python-argcomplete lumix)"
# Aggiungi in ~/.bashrc o ~/.zshrc per renderlo permanente
```

---

## 🏗️ Docker

```bash
docker build -t lumix .
docker run --rm lumix --type temp --from C --to K 25
```

---

## 🧪 Testing

```bash
pytest
```

---

## 🤝 Contribuire

1. Fork & clone
2. Crea branch `feature/x`
3. Aggiungi test e traduzioni
4. Apri una Pull Request

---

## 📝 Licenza

MIT © DMF

