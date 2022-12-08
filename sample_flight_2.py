# -*- coding: utf-8 -*-

from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

drone.takeoff()

drone.cw(90)        # 時計回りに旋回します。
drone.ccw(90)       # 反時計回りに旋回します。

drone.forward(50)   # 前進します。
drone.back(50)      # 後進します。

drone.right(50)     # 右移動します。
drone.left(50)      # 左移動します。

drone.up(50)        # 上昇します。
drone.down(50)      # 下降します。

drone.land()

"""
ここでは実際にドローンをプログラムで動かしてみます。このプログラムを実行するとドローンは3次元に移動します。
必ず開けた場所で実行してください。

引数やコマンドを書き換えてみましょう。するとドローンの飛行パターンや距離が変わります。
"""

