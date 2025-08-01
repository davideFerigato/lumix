# Guida all'Uso di `lumix`

## Installazione

### Da PyPI

```
pip install lumix
```

### Da sorgenti

```
git clone https://github.com/tuo-utente/lumix.git
cd lumix
python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install -e .
```

---

## Uso da Linea di Comando (CLI)

### Aiuto
```
lumix --help
```

### Temperatura

```
lumix --from C --to F 100
# Output: 100 °C = 212.00 °F
```

### Basi Numeriche

```
lumix --from dec --to bin 42
# Output: 101010
```

### Valute

```
lumix --from EUR --to USD 50
# Output: 50 EUR = 54.23 USD (rate 1.0846)
```

---

## Uso con Docker

```
docker build -t lumix .
docker run --rm lumix --from C --to F 100
```

---

## GUI (opzionale)

Se il tuo sistema ha Tkinter attivo:

```
python -m lumix.gui.app
```

---

## Localizzazione

Puoi cambiare lingua dell'interfaccia CLI tramite la variabile `LANG`.

Esempi:
```
LANG=it lumix --from C --to F 37
LANG=fr lumix --from EUR --to USD 20
```

---

## Autocompletamento Shell (bash/zsh)

```
pip install argcomplete
eval "$(register-python-argcomplete lumix)"
```

Per abilitazione permanente, aggiungi a `~/.zshrc` o `~/.bashrc`:

```
autoload -U compinit && compinit
eval "$(register-python-argcomplete lumix)"
```

---

## Note

- I comandi `--from`, `--to`, e le unità sono case-insensitive.
- Alcune lingue offrono alias localizzati: es. `--da`, `--a` in italiano.
