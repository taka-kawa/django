# django

# メモ

1. 始め方

~~~
django-admin startproject first
~~~

firstというdjangoプロジェクトを作る



2. 起動

~~~
python manage.py runserver
~~~



3. djangoアプリケーションを作成するときのコマンド

~~~
python manage.py startapp myapp
~~~



4. setting.pyのINSTALLED_APPSに追加

~~~
diary.apps.DiaryConfig
~~~



# 各ファイルの役割

# first内

## manage.py

djangoを管理するファイル



## db.sqlite3

DBファイル



## __pycache__

一度コンパイルすることで少し早くなっている



## wsgi.py

サーバー運用するときに必要

## urls.py

urlに対応するためのファイル

このURLの時はこの処理だと定義する



## setting.py

djangoの設定ファイル

エラーとか



# myapp内

## admin.py

管理画面に関するファイル



## apps.py

djangoのアプリの設定



## models.py

dbの設定を行う



## tests.py

テストを書くファイル

## views.py

処理を書くファイル



# model作成

1. diary/models.pyいじってモデル作成
2. 終わったら下記で変更を伝える

~~~
python manage.py makemigrations diary
~~~

3. そして変更をdbに反映

~~~
python manage.py migrate
~~~



# 汎用ビュー

- htmlの名称に法則がある
  - モデル名_confirm_deleteみたいな
  - ​