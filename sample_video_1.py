# -*- coding: utf-8 -*-

from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする
import cv2 # 画像を扱うので open cv をインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

while True:
    frame = drone.frame # クラス内にある frame 変数を持ってくる。この変数にドローンのカメラデータが入っている。

    if frame is None or frame.size == 0: # カメラデータが破損している。または何もない場合は continue する。これを書かないとエラーが出てしまいます。
        continue

    key = cv2.waitKey(1) & 0xFF # これを書くことでカメラビューウィンドウ内で任意のキーボードを検知できる。これを書かないとウィンドウは生成されない。
    cv2.imshow('CAMERA', frame) # ここでカメラビューウィンドウを生成する。

    if key == 27: # もし ESC キーが押されたらループを抜けてウィンドウを消す。27 は ESC キーのことである。
        break

cv2.destroyAllWindows()

'''
このプログラムはドローンから前方のカメラデータを取得して、ウィンドウ状にリアルタイムで表示します。
このプログラムを基礎にすることでドローンのカメラから画像を取得し、画像解析を行うことができます。
'''