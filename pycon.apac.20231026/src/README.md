## Binary

```bash
$ python3 bincat_01.py file_01
0010001100100000010000110110111101101110011000110111010101110010011100100110010101101110011000110111100100100...
```

```bash
$ python3 bincat_02.py file_01
00100011 00100000 01000011 01101111 01101110 01100011 01110101 01110010 01110010 01100101 01101110 01100011 01111001 ...
```

```bash
$ python3 bincat_03.py file_01
0010_0011 0010_0000 0100_0011 0110_1111 0110_1110 0110_0011 0111_0101 0111_0010 0111_0010 0110_0101 0110_1110 0110_0011 ...
```

```bash
$ python3 base_2_16.py
0000, 0
0001, 1
0010, 2
0011, 3
0100, 4
0101, 5
0110, 6
0111, 7
1000, 8
1001, 9
1010, A
1011, B
1100, C
1101, D
1110, E
1111, F
```

```bash
$ python3 bincat_04.py file_01
23 20 43 6F 6E 63 75 72 72 65 6E 63 79 20 61 6E 64 20 61 73 79 6E 63 20 2F 20 61 77 61 69 74 0A 0A 44 65 74 61 69 6C 73 ...
```

## Text

### ASCII


```bash
$ python3 bincat_05.py file_01
# Concurrency and async / await

Details about the `async def` syntax for *path operation functions* and some background about asynchronous code, concurrency, and parallelism.

## In a hurry?

<abbr title="too long; didn't read"><strong>TL;DR:</strong></abbr>

If you are using third party libraries that tell you to call them with `await`, like:

\`\`\`Python
results = await some_library()
\`\`\`

Then, declare your *path operation functions* with `async def` like:

\`\`\`Python hl_lines="2"
@app.get('/')
async def read_results():
    results = await some_library()
    return results
\`\`\`

!!! note
    You can only use `await` inside of functions created with `async def`.

---

If you are using a third party library that communicates with something (a database, an API, the file system, etc.) and doesn't have support for using `await`, (this is currently the case for most database libraries), then declare your *path operation functions* as normally, with just `def`, like:

\`\`\`Python hl_lines="2"
@
```

### UTF-8

```bash
$ python3 cat.py file_02
# 並行処理と async / await

*path operation 関数*のための `async def` に関する詳細と非同期 (asynchronous) コード、並行処理 (Concurrency)、そして、並列処理 (Parallelism) の背景について。

## 急いでいますか？

<abbr title="too long; didn't read (長すぎて読めない人のための要約という意味のスラング)"><strong>TL;DR:</strong></abbr>

次のような、`await` を使用して呼び出すべきサードパーティライブラリを使用している場合:

\`\`\`Python
results = await some_library()
\`\`\`

以下の様に `async def` を使用して*path operation 関数*を宣言します。

\`\`\`Python hl_lines="2"
@app.get('/')
async def read_results():
    results = await some_library()
    return results
\`\`\`

!!! note "備考"
    `async def` を使用して作成された関数の内部でしか `await` は使用できません。

---

データベース、API、ファイルシステムなどと通信し、`await`
```

```bash
$ python3 cat.py file_03
# 🛠️ &amp; 🔁 / ⌛

ℹ 🔃 `async def` ❕ *➡ 🛠️ 🔢* &amp; 🖥 🔃 🔁 📟, 🛠️, &amp; 🔁.

## 🏃 ❓

<abbr title="too long; didn't read"><strong>🆑;👩‍⚕️:</strong></abbr>

🚥 👆 ⚙️ 🥉 🥳 🗃 👈 💬 👆 🤙 👫 ⏮️ `await`, 💖:

\`\`\`Python
results = await some_library()
\`\`\`

⤴️, 📣 👆 *➡ 🛠️ 🔢* ⏮️ `async def` 💖:

```Python hl_lines="2"
@app.get('/')
async def read_results():
    results = await some_library()
    return results
\`\`\`

!!! note
    👆 💪 🕴 ⚙️ `await` 🔘 🔢 ✍ ⏮️ `async def`.

---

🚥 👆 ⚙️ 🥉 🥳 🗃 👈 🔗 ⏮️ 🕳 (💽, 🛠️, 📁 ⚙️, ♒️.) &amp; 🚫 ✔️ 🐕‍🦺 ⚙️ `await`, (👉 ⏳ 💼 🌅 💽 🗃), ⤴️ 📣 👆 *➡ 🛠️ 🔢* 🛎, ⏮️ `def`, 💖:

\`\`\`Python hl_lines="2"
@app.get('/')
def results():
    results = some_library()
    return results
\`\`\`

---

🚥 👆 🈸 (😫) 🚫 ✔️ 🔗 ⏮️ 
```


## SQLite

```bash
$ sqlite3 test.db
sqlite> CREATE TABLE fruits (
   ...>   id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>   name VARCHAR(256),
   ...>   country VARCHAR(2),
   ...>   num INTEGER
   ...> );
sqlite> INSERT INTO fruits(name, country, num) VALUES ("Orange", "JP", 7), ("Apple", "JP", 3), ("Grape", "US", 5);
sqlite> 
sqlite> ^D
```

```bash
$ echo '.schema' | sqlite3 test.db
CREATE TABLE fruits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(256),
  country VARCHAR(2),
  num INTEGER
);
CREATE TABLE sqlite_sequence(name,seq);
```

```bash
$ echo 'SELECT * FROM fruits;' | sqlite3 test.db
1|Orange|JP|7
2|Apple|JP|3
3|Grape|US|5
```

```bash
$ python3 -c 'print(open("test.db", "rb").read(100))'
b'SQLite format 3\x00\x10\x00\x01\x01\x0c@  \x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00._\x1d'
```

```bash
$ python3 sqlite_01.py test.db
FileHeader(magic_number=b'SQLite format 3\x00',
           page_size=4096,
           write_format=1,
           read_format=1,
           unused_reserved_space=12,
           maximum_embedded_payload_fraction=64,
           minimum_embedded_payload_fraction=32,
           leaf_payload_fraction=32,
           file_change_counter=2,
           in_header_database_size=3,
           first_freelist_trunk_page=0,
           freelist_pages=0,
           schema_cookie=1,
           schema_format_number=4,
           default_page_cache_size=0,
           largest_root_btree_page=0,
           database_text_encoding=1,
           user_version=0,
           is_incremental_vacuum_mode=0,
           application_id=0,
           version_valid_for_number=2,
           sqlite_version_number=3039005)
```

```bash
$ python3 -m venv venv --upgrade-deps
$ . venv/bin/activate
(venv) $ pip3 install sqlparse

(venv) $ python3 sqlite_02.py test.db .dbinfo
database page size: 4096
number of tables: 2

(venv) $ python3 sqlite_02.py test.db .schema
CREATE TABLE fruits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(256),
  country VARCHAR(2),
  num INTEGER);
CREATE TABLE sqlite_sequence(name,seq);

(venv) $ python3 sqlite_02.py test.db .print_rows fruits
| 1 | Orange | JP | 7 | 
| 2 | Apple | JP | 3 | 
| 3 | Grape | US | 5 | 
```


### Appendix


```bash
$ vim -b test.db
00000000: 53 51 4c 69 74 65 20 66 6f 72 6d 61 74 20 33 00  SQLite format 3.
00000010: 10 00 01 01 0c 40 20 20 00 00 00 02 00 00 00 03  .....@  ........
00000020: 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 04  ................
00000030: 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00  ................
00000040: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02  ................
00000060: 00 2e 5f 1d 0d 00 00 00 02 0f 0e 00 0f 60 0f 0e  .._..........`..
00000070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
...
00000ee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000ef0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000f00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 50 02  ..............P.
00000f10: 06 17 2b 2b 01 59 74 61 62 6c 65 73 71 6c 69 74  ..++.Ytablesqlit
00000f20: 65 5f 73 65 71 75 65 6e 63 65 73 71 6c 69 74 65  e_sequencesqlite
00000f30: 5f 73 65 71 75 65 6e 63 65 03 43 52 45 41 54 45  _sequence.CREATE
00000f40: 20 54 41 42 4c 45 20 73 71 6c 69 74 65 5f 73 65   TABLE sqlite_se
00000f50: 71 75 65 6e 63 65 28 6e 61 6d 65 2c 73 65 71 29  quence(name,seq)
00000f60: 81 11 01 07 17 19 19 01 81 7d 74 61 62 6c 65 66  .........}tablef
00000f70: 72 75 69 74 73 66 72 75 69 74 73 02 43 52 45 41  ruitsfruits.CREA
00000f80: 54 45 20 54 41 42 4c 45 20 66 72 75 69 74 73 20  TE TABLE fruits 
00000f90: 28 0a 20 20 69 64 20 49 4e 54 45 47 45 52 20 50  (.  id INTEGER P
00000fa0: 52 49 4d 41 52 59 20 4b 45 59 20 41 55 54 4f 49  RIMARY KEY AUTOI
00000fb0: 4e 43 52 45 4d 45 4e 54 2c 0a 20 20 6e 61 6d 65  NCREMENT,.  name
00000fc0: 20 56 41 52 43 48 41 52 28 32 35 36 29 2c 0a 20   VARCHAR(256),. 
00000fd0: 20 63 6f 75 6e 74 72 79 20 56 41 52 43 48 41 52   country VARCHAR
00000fe0: 28 32 29 2c 0a 20 20 6e 75 6d 20 49 4e 54 45 47  (2),.  num INTEG
00000ff0: 45 52 0a 29 00 00 00 00 00 00 00 00 00 00 00 00  ER.)............
00001000: 0d 00 00 00 03 0f c6 00 0f e4 0f d5 0f c6 00 00  ................
00001010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00001020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
...
00001fa0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00001fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00001fc0: 00 00 00 00 00 00 0d 03 05 00 17 11 01 47 72 61  .............Gra
00001fd0: 70 65 55 53 05 0d 02 05 00 17 11 01 41 70 70 6c  peUS........Appl
00001fe0: 65 4a 50 03 0e 01 05 00 19 11 01 4f 72 61 6e 67  eJP........Orang
00001ff0: 65 4a 50 07 00 00 00 00 00 00 00 00 00 00 00 00  eJP.............
00002000: 0d 00 00 00 01 0f e8 00 0f e8 00 00 00 00 00 00  ................
00002010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00002020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
...
00002fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00002fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00002fe0: 00 00 00 00 00 00 00 00 0a 01 03 19 01 66 72 75  .............fru
00002ff0: 69 74 73 03 00 00 00 00 00 00 00 00 00 00 00 00  its.............
```
