---

## **`docs/usage.md`** (Guida all'Uso)

```markdown
# Guida all'Uso di `lumix`

## Installazione

### Da PyPI

```bash
pip install lumix
```

### Da sorgenti

```bash
git clone https://github.com/tuo-utente/lumix.git
cd lumix
python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install -e .
```

---

## Uso Generale

```bash
lumix <lingua> <tipo> [parametri]
```

- `<lingua>`: `en`, `it`, `fr`, `es`, `jp`
- `<tipo>`: il nome del modulo nella lingua scelta (vedi tabella sotto)
- I parametri variano per modulo, ma seguono solitamente lo schema:
  `from <unità_src> to <unità_dst> <valore>` (o equivalenti localizzati)

**Esempio**: `lumix en temperature from C to F 36.5`

---

## Elenco Completo dei Tipi per Lingua

| Italiano (it)   | Inglese (en)   | Francese (fr)  | Spagnolo (es)  | Giapponese (jp) | Modulo       |
|-----------------|----------------|----------------|----------------|-----------------|--------------|
| temperatura     | temperature    | température    | temperatura    | 温度            | temps        |
| valuta          | currency       | devise         | moneda         | 通貨            | currency     |
| base            | base           | base           | base           | 基数            | bases        |
| peso            | weight         | poids          | peso           | 重さ            | weight       |
| lunghezza       | length         | longueur       | longitud       | 長さ            | length       |
| volume          | volume         | volume         | volumen        | 体積            | volume       |
| area            | area           | surface        | área           | 面積            | area         |
| velocità        | speed          | vitesse        | velocidad      | 速度            | speed        |
| tempo           | time           | temps          | tiempo         | 時間            | time         |
| energia         | energy         | énergie        | energía        | エネルギー      | energy       |
| pressione       | pressure       | pression       | presión        | 圧力            | pressure     |
| potenza         | power          | puissance      | potencia       | 電力            | power        |
| dati            | data           | données        | datos          | データ          | data         |
| bitrate         | bitrate        | débit          | bitrate        | ビットレート    | bitrate      |
| hash            | hash           | hash           | hash           | ハッシュ        | hash         |
| colore          | color          | couleur        | color          | 色              | color        |
| strumentiip     | iptools        | outilsip       | herramientasip | IPツール        | iptools      |
| fusi            | timezones      | fuseaux        | husos          | タイムゾーン    | timezones    |
| data            | date           | date           | fecha          | 日付            | date         |
| calendario      | calendar       | calendrier     | calendario     | カレンダー      | calendar     |
| età             | age            | âge            | edad           | 年齢            | age          |
| password        | passwords      | motsdepasse    | contraseñas    | パスワード      | passwords    |
| paese           | country        | pays           | país           | 国              | country      |
| lingua          | language       | langue         | idioma         | 言語            | language     |
| simboliunita    | unitsymbols    | symbolesunités | simbolosunidad | 単位記号        | unitsymbols  |
| romano          | roman          | romain         | romano         | ローマ数字      | roman        |
| morse           | morse          | morse          | morse          | モールス        | morse        |
| timezonebot     | timezonebot    | robotfuseau    | zonabot        | タイムゾーンボット | timezonebot  |
| parlato         | spoken         | parlé          | hablado        | 話し言葉        | spoken       |
| fonetico        | phonetic       | phonétique     | fonético       | 発音記号        | phonetic     |

---

## Esempi per Modulo

### Temperatura
```bash
lumix en temperature from C to F 36.5
lumix it temperatura da C a F 36,5
```

### Valuta
```bash
lumix en currency from EUR to USD 50
lumix it valuta da EUR a USD 50
```

### Basi numeriche
```bash
lumix en base from dec to hex 255
lumix it base da dec a hex 255
```

### Peso
```bash
lumix en weight from kg to lb 75
lumix it peso da kg a lb 75
```

### Lunghezza
```bash
lumix en length from m to ft 1.80
lumix it lunghezza da m a ft 1,80
```

### Volume
```bash
lumix en volume from l to gal 2
lumix it volume da l a gal 2
```

### Area
```bash
lumix en area from m2 to ft2 50
lumix it area da m2 a ft2 50
```

### Velocità
```bash
lumix en speed from km/h to mph 130
lumix it velocità da km/h a mph 130
```

### Tempo
```bash
lumix en time from days to hours 3
lumix it tempo da giorni a ore 3
```

### Energia
```bash
lumix en energy from J to kcal 500
lumix it energia da J a kcal 500
```

### Pressione
```bash
lumix en pressure from bar to psi 2
lumix it pressione da bar a psi 2
```

### Potenza
```bash
lumix en power from W to hp 1000
lumix it potenza da W a hp 1000
```

### Dati digitali
```bash
lumix en data from MB to GB 1500
lumix it dati da MB a GB 1500
```

### Bitrate
```bash
lumix en bitrate from Mbps to Kbps 100
lumix it bitrate da Mbps a Kbps 100
```

### Hash
```bash
lumix en hash sha256 "hello world"
lumix it hash sha256 "ciao mondo"
```

### Colori
```bash
lumix en color from rgb to hex 255,255,255
lumix it colore da rgb a hex 255,255,255
```

### Strumenti IP
```bash
lumix en iptools cidr-to-range 192.168.1.0/24
lumix en iptools ip-to-bin 192.168.1.1
lumix en iptools netmask 10.0.0.0/8
lumix en iptools subnet-info 192.168.1.0/24
```

### Fusi orari
```bash
lumix en timezones from Europe/Rome to Asia/Tokyo "2025-08-02 14:00"
lumix it fusi da Europe/Rome a Asia/Tokyo "02/08/2025 14:00"
```

### Formati data
```bash
lumix en date from us to iso 08/02/2025
lumix it data da us a iso 08/02/2025
```

### Differenza date
```bash
lumix en calendar diff 2025-01-01 2025-12-31
lumix it calendario diff 01/01/2025 31/12/2025
```

### Calcolo età
```bash
lumix en age from 1990-05-23
lumix it età da 23/05/1990
```

### Generazione password
```bash
lumix en passwords generate length 12
lumix en passwords generate length 16 symbols true
```

### Codici paese
```bash
lumix en country from code to name IT
lumix it paese da codice a nome IT
```

### Codici lingua
```bash
lumix en language from name to code "italian"
lumix it lingua da nome a codice "italiano"
```

### Simboli unità
```bash
lumix en unitsymbols from W to "unit name"
lumix en unitsymbols from kilogram to symbol
```

### Numeri romani
```bash
lumix en roman from 2025
lumix en roman to MMXXV
```

### Codice Morse
```bash
lumix en morse from-text "SOS"
lumix en morse to-text "... --- ..."
```

### Ora in una città (timezonebot)
```bash
lumix en timezonebot what-time Tokyo
lumix it timezonebot what-time Roma
```

### Numeri in parole
```bash
lumix en spoken from 123456
lumix it parlato da 123456
```

### Alfabeto fonetico
```bash
lumix en phonetic for CIAO
lumix en phonetic for HELLO
```

---

## Docker

```bash
docker build -t lumix .
docker run --rm lumix en temperature from C to F 36.5
```

---

## Autocompletamento (bash/zsh)

```bash
pip install argcomplete
eval "$(register-python-argcomplete lumix)"
# Aggiungi in ~/.bashrc o ~/.zshrc per renderlo permanente
```

---

## Note

- I comandi `--from`, `--to` e le unità sono case‑insensitive.
- Il separatore decimale dipende dalla lingua: `en` e `jp` usano il punto (`.`), le altre usano la virgola (`,`).
- Per valori con virgola, assicurarsi di racchiuderli tra virgolette se contengono spazi (es. date).
```
