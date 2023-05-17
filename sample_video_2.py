""" sample_video_2.py
　このサンプルプログラムは、Tello ドローンに搭載されたカメラからデータを取得し、それをウィンドウに表示するプログラムです。
つまり ドローンからリアルタイム映像を取得するプログラムです。
画像処理の基礎として、以下のプログラムを使用することで、Tello からカメラ映像を取得できます。

　また、このプログラムでは新たに、キーボードで Tello を操作するコードを記述しています。
OpenCV の waitKey メソッドを活用することで、生成されたカメラビューウィンドウ上のキーボード入力を検知することができます。
"""

from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする
import cv2 # 画像を扱うので open cv をインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する
drone.stream(1)

while True:
    frame = drone.frame # クラス内にある frame 変数を持ってくる。この変数にドローンのカメラデータが入っている。

    if frame is None or frame.size == 0: # カメラデータが破損している。または何もない場合は continue する。これを書かないとエラーが出てしまいます。
        print("None...")
        continue

    key = cv2.waitKey(1) & 0xFF # これを書くことでカメラビューウィンドウ内で任意のキーボードを検知できる。これを書かないとウィンドウは生成されない。
    cv2.imshow('CAMERA', frame) # ここでカメラビューウィンドウを生成する。

    if key == 27: # もし ESC キーが押されたらループを抜けてウィンドウを消す。27 は ESC キーのことである。
        drone.land()
        break

    elif key == ord('t'): # t キーを押すと離陸
        drone.takeoff()
    elif key == ord('l'): # l キーを押すと着陸
        drone.land()
    elif key == ord('w'): # w キーを押すと前進
        drone.forward(20)
    elif key == ord('s'): # s キーを押すと後進
        drone.back(20)
    elif key == ord('a'): # a キーを押すと左移動
        drone.left(20)
    elif key == ord('d'): # d キーを押すと右移動
        drone.left(20)
    elif key == ord('q'): # q キーを押すと反時計回り
        drone.ccw(10)
    elif key == ord('e'): # e キーを押すと時計回り
        drone.cw(10)
    elif key == ord('r'): # r キーを押すと上昇
        drone.up(20)
    elif key == ord('f'): # r キーを押すと下降
        drone.down(20)

cv2.destroyAllWindows()
del drone

'''
このプログラムはドローンから前方のカメラデータを取得して、ウィンドウ状にリアルタイムで表示します。
このプログラムを基礎にすることでドローンのカメラから画像を取得し、画像解析を行うことができます。
'''
