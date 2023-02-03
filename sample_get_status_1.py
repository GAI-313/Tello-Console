""" sample_get_data_1.py
　このサンプルコードは、ドローンから任意のステータスを取得する方法を記述します。
以前はドローンに対して指示を送り、ドローンを操作する方法を学びました。
console のメソッドには、get_ から始まるドローンの情報を取得する目ドッドが用意されています。

例えば get_battery メソッド。このメソッドはドローンの現在のバッテリー残量を取得します。
取得したデータは、新たに任意の変数として格納することで参照することができます。
"""

from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートするる

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

tof = drone.get_tof() # get_tof で、ドローンの ToF センサーからの飛行光度を取得

battery = drone.get_battery() # get_battery で、ドローンのバッテリー残量を取得

flight_time = drone.get_flighttime() # get_flighttime で、ドローンの飛行時間を取得（飛行中のみ秒数が刻まれます。）

imu = drone.get_imu() # get_imu で、ドローンの現在の姿勢角度 x, y, z 軸を取得

speed = drone.get_speed() # get_speed で、ドローンの設定された飛行速度を取得。（飛行中の飛行速度ではなくパラメータとして設定された飛行速度を取得します。）

# 結果を表示
print('ToF からの飛行高度：',tof)
print('ドローンのバッテリー残量：',battery)
print('ドローンの飛行時間：', flight_time)
print('ドローンの姿勢角（x, y, z）：', imu)
print('ドローンの設定された飛行速度：', speed)