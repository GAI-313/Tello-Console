# -*- coding: utf-8 -*- 

from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

drone.takeoff() # takeoff メソッドを呼び出しドローンを離陸させます。

drone.wait(15) # wait メソッドで5秒間ドローンを待機させます。

drone.land() # ドローンは自動着陸します。

"""
tello console 内にはドローンをオペレートするためのメソッドが用意されており、これをコマンドとして使用することでドローンを操作することができます。
taeoff, land コマンドは引数を持ちませんが、 wait コマンドなどの一部のコマンドには括弧内に引数を代入する必要があります。
試しに wait() コマンドの引数を変えてみてください。ドローンのホバリング時間が変化します。
"""