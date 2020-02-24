## Install

```shell
$ cd src/
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip3 install -r requirements.lock
```

## Usage

```shell
(venv) $ python3 main.py -h
usage: main.py [-h] [--output OUTPUT]
               [--fields {title,speaker,level,category,url,content} [{title,speaker,level,category,url,content} ...]]

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        出力先ファイル名
  --fields {title,speaker,level,category,url,content} [{title,speaker,level,category,url,content} ...]
                        出力先ファイルに含めるフィールド(default: title speaker level category url)
```

## Examples

```shell
(venv) $ python3 main.py
(venv) $ head -n 4 shizuoka.csv
title,speaker,level,category,url
DataFlow + Pythonで大規模データ処理,masahito,レベル:All: エンジニア以外も対象,カテゴリ:データ基盤,https://shizuoka.pycon.jp/session/masahito/
Djangoで始めるWeb開発の世界 〜Web開発を知らない方に贈る、Django Girls Tutorialとその周辺のクイックツアー〜,nikkie,レベル:All: エンジニア以外も対象,カテゴリ:WEB系,https://shizuoka.pycon.jp/session/ftnext/
EeLとWebSlidesで一味違う画像処理のプレゼン,高橋かずひと,レベル:All: エンジニア以外も対象,カテゴリ:プレゼンテーション,https://shizuoka.pycon.jp/session/kzhttkhs/

(venv) $ python3 main.py --fields title speaker category
(venv) $ head -n 4 shizuoka.csv
title,speaker,category
DataFlow + Pythonで大規模データ処理,masahito,カテゴリ:データ基盤
Djangoで始めるWeb開発の世界 〜Web開発を知らない方に贈る、Django Girls Tutorialとその周辺のクイックツアー〜,nikkie,カテゴリ:WEB系
EeLとWebSlidesで一味違う画像処理のプレゼン,高橋かずひと,カテゴリ:プレゼンテーション
```
