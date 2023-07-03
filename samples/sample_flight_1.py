from tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする
# 74 128 105 
drone = console(tello_ip="192.168.201.76") # console クラスを任意の変数に格納して console のインスタンスを生成する

drone.takeoff() # takeoff メソッドを呼び出しドローンを離陸させます。

drone.wait(5) # wait メソッドで5秒間ドローンを待機させます。
drone.up(60)
drone.flip("r")

drone.land() # ドローンは自動着陸します。
