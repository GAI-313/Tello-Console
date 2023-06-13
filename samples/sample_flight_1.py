from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

drone.takeoff() # takeoff メソッドを呼び出しドローンを離陸させます。

drone.wait(15) # wait メソッドで5秒間ドローンを待機させます。

drone.land() # ドローンは自動着陸します。
