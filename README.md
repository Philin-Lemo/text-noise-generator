# Text noise generator
This project is a Python code for generating pseudo-random text, inspired by the Library of Babel.

Preview:

<img width="854" height="480" alt="tng" src="https://github.com/user-attachments/assets/b909627f-07f8-4a0c-8412-3593fd33618f" />

### Generation settings:

- --help (-h) - Help
- --sleep-time (-t) - Time between printing characters (default: 0.05)
- --max-len (-max) - Maximum word length (default: 12)
- --min-len (-min) - Minimum word length (default: 3)
- --alphabet (-a) - Alphabet used (en/ru or a string of custom characters) (default: en)
- --text-color - Text color (default: white)
- --filling-void (-v) - Frequency of spaces (default: 12)
- --filling-points (-p) - Frequency of periods (default: 5)
- --filling-commas (-c) - Frequency of commas (default: 3)
- --filling-question (-q) - Frequency of question marks (default: 1)
- --filling-exclamation-marks - Frequency of exclamation marks (default: 1)

### Configuration example:

```
tng -a QWERTYUIOPASDFGHJKLZXCBNM
```
<img width="854" height="480" alt="tng -a QWERTYUIOPASDFGHJKLZXCBNM" src="https://github.com/user-attachments/assets/597461c8-2eb4-4b0c-9e6b-c29b17c4add4" />

```
tng --text-color light_blue
```
(The preview and settings examples were made in vhs, so the blue color is increased)
<img width="854" height="480" alt="tng --text-color light_blue" src="https://github.com/user-attachments/assets/98f955d3-0cf0-4a37-8362-c65ca4f0163e" />

```
tng -t 0.025
```
<img width="854" height="480" alt="tng -t 0 025" src="https://github.com/user-attachments/assets/353515dc-2c2e-466e-a4d7-f9a84c06ba17" />

### Installing the Python script on Unix (Linux, BSD, MacOS) systems (globally):

· Git is required

Run:

```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; chmod +x text-noise-generator.py; sudo cp text-noise-generator.py /bin/tng
```

or via pip:

```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; sudo pip install .
```

if you get the error "error: externally-managed-environment", then use (at your own risk):

```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; sudo pip install . --break-system-packages
```

If you want to install locally, change the path in the installation command from /bin/tng to ~/.local/bin

### Installing with compilation on Unix (Linux, BSD, MacOS) systems via Nuitka (globally):

#### Installing dependencies:

· Arch:

```
sudo pacman -S git python nuitka python-ordered-set python-zstandard base-devel
```

· Debian/Ubuntu/Mint:

```
sudo apt update && sudo apt install -y git python3 nuitka python3-ordered-set python3-zstandard build-essential
```

· FreeBSD/OpenBSD/NetBSD:

```
sudo pkg install git python311 py311-nuitka
```

· MacOs:

```
xcode-select --install
brew install git python termcolor nuitka ordered-set zstandard
```

#### Compilation and installation:

```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; nuitka text-noise-generator.py; sudo cp text-noise-generator.bin /bin/tng
```

If you want to install locally, change the path in the installation command from /bin/tng to ~/.local/bin

### Installing the Python script on Windows  (globally):

· Git is required
· Run the console as administrator

Only via pip:

```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; pip install .
```

if you get the error "error: externally-managed-environment", then use (at your own risk):

```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; pip install . --break-system-packages
```

or without git:

· Download the source code manually
· Unzip if necessary
· Move the folder to C:/
· Run the console as administrator
· Type:

```
cd text-noise-generator; pip install .
```

if you get the error "error: externally-managed-environment", then use (at your own risk):

```
cd text-noise-generator; pip install . --break-system-packages
```
