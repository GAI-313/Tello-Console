""" sample_flight_1.py
　このサンプルコードはドローンを離陸、着陸させる方法を記述しています。
変数 drone は console を格納することで、console に命令を送る特別な変数になります。
console クラスには、ドローンに対してさまざまな命令を送るメソッドが用意されており、
このメソッドを以降記述することで Tello ドローンに任意の指示を送ることができます。

ここでは、実際にドローンを離陸させ、15秒間待機させてから着陸させるタスクを実行します。
"""

from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

drone.takeoff() # takeoff メソッドを呼び出しドローンを離陸させます。

drone.wait(15) # wait メソッドで5秒間ドローンを待機させます。

drone.land() # ドローンは自動着陸します。
