# 卒論デモ用リポジトリ

FlaskとOpenCVのサーバ

## コマンド

```bash
$ pipenv install xxxxxx # ライブラリをインストールするとき
$ pipenv run python server.py
```

```
localhost:8080
```

ディレクトリ構成

```txt
Root
┃
┣━ data        /  開発環境でrequest時に使うディレクトリ
┣━ tmp         /  送られてきた元のimgを一旦保存するディレクトリ
┣━ transformed /  加工したimgを保存するディレクトリ
┣━ python.py   /  このファイルをメインファイルとして実行する
┣━ transformation.py        / 透視変換を行うファイル
┣━ .python-version /  Pythonのバージョン 3.7.4
┣━ Pipfile     /  packageを管理するファイル
┗━ Pipfile.lock /  packageを管理するファイル
```

角度的に今対応できているのは、`data/1.jpg`