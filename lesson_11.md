1) Создать директорию `files_race`, в ней создать пустой файл `cache`
2) Запустить скрипт как systemd-демон (домашняя директория - созданная в п1 `files_race`)
```python
#!/usr/bin/env python3
import fcntl
import time
from pathlib import Path

PATH = Path("./cache")

PATH.parent.mkdir(parents=True, exist_ok=True)
PATH.touch(exist_ok=True)

with PATH.open("r+") as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    print(f"Locked: {PATH}")
    try:
        while True:
            time.sleep(1)
    finally:
        fcntl.flock(f, fcntl.LOCK_UN)
```
3) В директории `files_race` создать файл `writer.py` с содержимым
```python
#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import fcntl
import sys

PATH = Path("./cache")

PATH.parent.mkdir(parents=True, exist_ok=True)
PATH.touch(exist_ok=True)

with PATH.open("a+") as f:
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit("file is locked by another process")

    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.flush()
    fcntl.flock(f, fcntl.LOCK_UN)
```
4) Запустить скрипт `writer.py` командой
```bash
python3 writer.py
```
5) Найти файл, который требуется скрипту `writer.py` (не заглядывая в исходный код) и найти какой процесс его блокирует; "убить" этот процесс и запустить скрипт `writer.py` еще раз
6) В директории `files_race` создать файл `bin.py` с сожержимым
```python
from pathlib import Path

def create_file(path, size_bytes):
    chunk = b"0" * (1024 * 1024)  # 1 MB блок
    with open(path, "wb") as f:
        remaining = size_bytes
        while remaining > 0:
            n = min(remaining, len(chunk))
            f.write(chunk[:n])
            remaining -= n

sizes = [
    1024,              # 1 KB
    10 * 1024,         # 10 KB
    1 * 1024 * 1024,   # 1 MB
    100 * 1024 * 1024, # 100 MB
    3 * 1024 * 1024 * 1024,  # 3 GB
]

out = Path("output")
out.mkdir(exist_ok=True)

for i, size in enumerate(sizes, 1):
    create_file(out / f"file_{i}_{size}.bin", size)
```
7) Запустить скрипт `bin.py`
```bash
python3 bin.py
```
8) Найти в директории `files_race` (и вложенных в нее директориях) самый большой файл (для этого самостоятельно изучить утилиту `du`)
