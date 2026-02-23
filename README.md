# Lumix 🔄

[![PyPI version](https://img.shields.io/pypi/v/lumix)](https://pypi.org/project/lumix/)
[![Python versions](https://img.shields.io/pypi/pyversions/lumix)](https://pypi.org/project/lumix/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/davideFerigato/lumix/actions/workflows/tests.yml/badge.svg)](https://github.com/davideFerigato/lumix/actions/workflows/tests.yml)

**Lumix** is a **modular**, **multilingual** command-line converter for physical units, digital data, time, security tools, and creative utilities.  
Designed to be **easily extensible**, it features **shell autocompletion** and an **optional GUI** – all in one sleek package.

🌐 **Supported languages:** English, Italian, French, Spanish, Japanese.  
⚙️ **Modular core:** add your own converters in minutes.  
🖥️ **Optional GUI** (Tkinter) for those who prefer point‑and‑click.

---

## ✨ Features

- **🌍 Multilingual by design** – Use Lumix in your native language (en, it, fr, es, jp).
- **🧩 Modular architecture** – Each converter is independent; adding a new one is as simple as creating a new folder.
- **🚀 Rich set of converters** – From physical units to digital data, from time zones to creative tools (see [examples](#-detailed-examples)).
- **⌨️ Shell autocompletion** – Works with bash and zsh via `argcomplete`.
- **🐳 Docker‑ready** – Run Lumix anywhere without installing dependencies.
- **🧪 Fully tested** – High test coverage with `pytest`.
- **🖥️ Optional GUI** – A simple Tkinter interface (in development).

---

## 📦 Installation

### From PyPI (recommended)

```bash
pip install lumix
From source

bash
git clone https://github.com/davideFerigato/lumix.git
cd lumix
python -m venv venv && source venv/bin/activate   # or `venv\Scripts\activate` on Windows
pip install --upgrade pip
pip install -e .
🚀 Basic Usage

bash
lumix --help
Lumix follows a simple pattern:

bash
lumix <language> <converter> from <source> to <target> <value>
For example:

bash
lumix en temperature from C to F 36.5
lumix it temperatura da C a F 36,5      # Italian uses comma as decimal separator
🔍 Detailed Examples

🔥 Temperature

bash
lumix en temperature from C to F 36.5
# Output: 36.5 °C → 97.70 °F
💱 Currency

bash
lumix en currency from EUR to USD 50
# Output: 50.00 EUR → 54.23 USD
🔢 Number Bases

bash
lumix en base from dec to hex 255
# Output: 255 (dec) → ff (hex)
⚖️ Weight

bash
lumix en weight from kg to lb 75
# Output: 75.00 kg → 165.35 lb
📏 Length

bash
lumix en length from m to ft 1.80
# Output: 1.80 m → 5.91 ft
🧴 Volume

bash
lumix en volume from l to gal 2
# Output: 2.00 l → 0.53 gal
🟦 Area

bash
lumix en area from m2 to ft2 50
# Output: 50.00 m² → 538.20 ft²
🏎️ Speed

bash
lumix en speed from km/h to mph 130
# Output: 130.00 km/h → 80.78 mph
⏱️ Time

bash
lumix en time from days to hours 3
# Output: 3.00 days → 72.00 hours
⚡ Energy

bash
lumix en energy from J to kcal 500
# Output: 500.00 J → 0.12 kcal
🌡️ Pressure

bash
lumix en pressure from bar to psi 2
# Output: 2.00 bar → 29.01 psi
🔌 Power

bash
lumix en power from W to hp 1000
# Output: 1000.00 W → 1.34 hp
💾 Digital Data

bash
lumix en data from MB to GB 1500
# Output: 1500.00 MB → 1.46 GB
📡 Bitrate

bash
lumix en bitrate from Mbps to Kbps 100
# Output: 100.00 Mbps → 100000.00 Kbps
🔐 Hash

bash
lumix en hash sha256 "hello world"
# Output: "hello world" → b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
🎨 Color

bash
lumix en color from rgb to hex 255,255,255
# Output: RGB(255,255,255) → #ffffff
🌐 IP Tools

bash
lumix en iptools cidr-to-range 192.168.1.0/24
# Output: First IP: 192.168.1.0 / Last IP: 192.168.1.255
🕒 Time Zones

bash
lumix en timezones from Europe/Rome to Asia/Tokyo "2025-08-02 14:00"
# Output: 2025-08-02 14:00 Europe/Rome → 2025-08-02 21:00 Asia/Tokyo
📅 Date & Calendar

bash
lumix en date from us to iso 08/02/2025
# Output: 08/02/2025 (us) → 2025-02-08 (iso)

lumix en calendar diff 2025-01-01 2025-12-31
# Output: Difference: 364 days
🧑 Age Calculator

bash
lumix en age from 1990-05-23
# Output: 35 years old (depending on current date)
🔑 Password Generator

bash
lumix en passwords generate length 16 symbols true
# Output: Generated password: K#9mP$2xL@5qR!vW
🌍 Country Codes

bash
lumix en country from code to name IT
# Output: Italy
🗣️ Language Codes

bash
lumix en language from name to code "italian"
# Output: it
📏 Unit Symbols

bash
lumix en unitsymbols from W to "unit name"
# Output: watt
Ⅿ Roman Numerals

bash
lumix en roman from 2025
# Output: 2025 → MMXXV
...‑‑‑ Morse Code

bash
lumix en morse to-text "... --- ..."
# Output: SOS
🤖 Timezone Bot

bash
lumix en timezonebot what-time Tokyo
# Output: Current time in Tokyo: 2025-08-02 22:15:00 JST
🔢 Numbers to Words

bash
lumix en spoken from 123456
# Output: one hundred twenty-three thousand four hundred fifty-six
🔤 Phonetic Alphabet

bash
lumix en phonetic for CIAO
# Output: Charlie India Alpha Oscar
⏩ Shell Autocompletion

Lumix integrates with argcomplete to provide smart tab completion.

bash
pip install argcomplete
eval "$(register-python-argcomplete lumix)"
# Add the eval line to your ~/.bashrc or ~/.zshrc to make it permanent
Note: Autocompletion is still under active improvement.
🐳 Docker

Run Lumix in a container without any local installation:

bash
docker build -t lumix .
docker run --rm lumix en temperature from C to F 36.5
🧪 Testing

We use pytest for unit tests. To run the full suite:

bash
pytest tests/
Each module has its own test file (test_<module>.py) to ensure reliability.

🤝 Contributing

Contributions are welcome! Whether you want to add a new converter, improve documentation, or fix a bug, please feel free to open an issue or submit a pull request.

Fork the repository.
Create a feature branch (git checkout -b feature/amazing-converter).
Commit your changes (git commit -m 'Add amazing converter').
Push to the branch (git push origin feature/amazing-converter).
Open a Pull Request.
Please make sure to update tests as appropriate.

📄 License

Distributed under the MIT License. See LICENSE for more information.

🙏 Acknowledgements

Frankfurter API for real‑time exchange rates.
argcomplete for shell completion magic.
All contributors and users who make this project better.
Happy converting! 🚀
