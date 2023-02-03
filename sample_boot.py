""" sample_boot.py

　このプログラムは、tello.py に記述されている console クラスを呼び、
その console クラスを任意の変数に格納して、console クラスを活性化（インスタンス化）させる方法をサンプルとして記述します。

console クラスとは、Tello を Python で操作できるようにするプログラムのことを指します。
console クラスは、誰かから命令されないと何もしてくれません。
そのために、console クラスを import で呼び込み、任意の変数に格納させて console に命令を送るよう準備させるのです。
console は、任意の変数に格納（インスタンス化）された時、ドローンへの接続プログラムを実行し、
以降のドローンに対するプログラムを受け付けます。
"""
from modules.tello import console # ここで modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # ここで console クラスを任意の変数に格納して console のインスタンスを生成する