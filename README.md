# Text noise generator 
Данный проект — это код на Python по генерации псевдослучайного текста, вдохновлённый Вавилонской библиотекой.
### Превью :
<img width="1280" height="720" alt="tng" src="https://github.com/user-attachments/assets/dc3b865b-4b8e-4b7d-9137-737c82dbf4d4" />

### Настройка генерации:
- --help (-h) - Помощь
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

### Пример настройки:
```
tng -a ru
```
<img width="1280" height="720" alt="tng -a ru" src="https://github.com/user-attachments/assets/f4d67e5e-67cc-4edf-a62c-c66ca97bcb14" />

```
tng --text-color light_magenta
```
<img width="1280" height="720" alt="tng --text-color light_blue" src="https://github.com/user-attachments/assets/8003abc4-50a9-4f90-9502-178892850ef3" />

```
tng -t 0.025
```
<img width="1280" height="720" alt="tng -t 0 025" src="https://github.com/user-attachments/assets/b0e05b7b-ffa9-48db-94d1-efa688cc55aa" />



### Установка Python скрипта на Unix(Linux, BSD, MacOS) системы (глобально):
- Необходим git

Выполните:
```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; chmod +x text-noise-generator.py; sudo cp text-noise-generator.py /bin/tng
```
или же через pip:
```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; sudo pip install .
```
если выдаёт ошибку "error: externally-managed-environment", то используйте(на свой страх и риск):
```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; sudo pip install . --break-system-packages
```
Если захотите установить локально, то измените в команде установки путь с /bin/tng на ~/.local/bin

### Установка с компиляцией на Unix(Linux, BSD, MacOS) системы через Nuitka (глобально):
#### Установка зависимостей:
- Arch:
```
sudo pacman -S git python nuitka python-ordered-set python-zstandard base-devel
```
- Debian/Ubuntu/Mint:
```
sudo apt update && sudo apt install -y git python3 nuitka python3-ordered-set python3-zstandard build-essential
```
- FreeBSD/OpenBSD/NetBSD:
```
sudo pkg install git python311 py311-nuitka
```
- MacOs:
```
xcode-select --install
brew install git python termcolor nuitka ordered-set zstandard
```
#### Компиляция и утановка
```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; nuitka text-noise-generator.py; sudo cp text-noise-generator.bin /bin/tng
```

Если захотите установить локально, то измените в команде установки путь с /bin/tng на ~/.local/bin

### Установка Python скрипта на Windows:
- Необходим git
- Запуск консоли от имени администратора

Только через pip:
```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; pip install .
```
если выдаёт ошибку "error: externally-managed-environment", то используйте(на свой страх и риск):
```
git clone https://github.com/Philin-Lemo/text-noise-generator.git; cd text-noise-generator; pip install . --break-system-packages
```
или же без git :
- Скачайте исходный код вручную
- Если потребуется распакуйте
- Переместите папку в C:/
- Запустите консоль от имени администратора
- Пропишите:
```
cd text-noise-generator; pip install .
```
если выдаёт ошибку "error: externally-managed-environment", то используйте(на свой страх и риск):
```
cd text-noise-generator; pip install . --break-system-packages
```
