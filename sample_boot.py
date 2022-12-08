# -*- coding: utf-8 -*-
"""
sample_boot.py
これはサンプルコードです。
このサンプルコードでは、Tello-Console tello.py を任意のプログラムにインポートする方法と、
tello.py の中にある console クラスがインスタンス化された時の振る舞いを見ることができます。
"""
from modules.tello import console # ここで modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # ここで console クラスを任意の変数に格納して console のインスタンスを生成する
"""
console クラスがインスタンス化されると、tello.py はTello との接続を確認し、正常に接続できることを診断します。
続いてバッテリーの残量、ファームウェアバージョンを調べ、ドローンが最新の状態であることを確認します。
最後に各スレッドを起動させてプログラムが実行可能であるかどうかを最終診断します。
"""