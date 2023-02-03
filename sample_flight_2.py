""" sample_flight_2.py
　このサンプルコードはドローンを操作する方法を記述しています。
変数 drone は console を格納することで、console に命令を送る特別な変数になります。
console クラスには、ドローンに対してさまざまな命令を送るメソッドが用意されており、
このメソッドを以降記述することで Tello ドローンに任意の指示を送ることができます。

ここでは、実際にドローンを離陸させ、15秒間待機させてから着陸させるタスクを実行します。
"""

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

