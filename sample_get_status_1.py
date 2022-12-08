# -*- coding: utf-8 -*-

from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートするる

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

tof = drone.get_tof() # get_tof で、ドローンの ToF センサーからの飛行光度を取得

battery = drone.get_battery() # get_battery で、ドローンのバッテリー残量を取得

flight_time = drone.get_flighttime() # get_flighttime で、ドローンの飛行時間を取得（飛行中のみ秒数が刻まれます。）

imu = drone.get_imu() # get_imu で、ドローンの現在の姿勢角度 x, y, z 軸を取得

speed = drone.get_speed() # get_speed で、ドローンの設定された飛行速度を取得。（飛行中の飛行速度ではなくパラメータとして設定された飛行速度を取得します。）

# 結果を表示
print('ToF からの飛行高度：%s'%(tof))
print('ドローンのバッテリー残量：%s'%(battery))
print('ドローンの飛行時間：%s'%(flight_time))
print('ドローンの姿勢角（x, y, z）：%s'%(imu))
print('ドローンの設定された飛行速度：%s'%(speed))