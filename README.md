

# lumix

[![CI](https://github.com/USERNAME/lumix/actions/workflows/ci.yml/badge.svg)](https://github.com/USERNAME/lumix/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/docker-supported-blue)](https://github.com/USERNAME/lumix#docker)
[![PyPI](https://img.shields.io/pypi/v/lumix.svg)](https://pypi.org/project/lumix)

**`lumix` è una CLI modulare, localizzata e pronta a espandersi, per la conversione tra unità.**

Supporta:

- Temperature (°C, °F, °K)
- Basi numeriche (dec ↔ bin ↔ hex ↔ oct)
- Valute (con cache e API)
- Localizzazione automatica (en, it, es, fr, ja)
- Autocompletamento per Bash/Zsh
- GUI opzionale via Tkinter

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