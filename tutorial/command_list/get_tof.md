# get_tof コマンド

```get_tof()```

　ドローンの絶対高度を取得します。以下のサンプルコードでは、ドローンからの絶対高度を計測し、地表から 150cm を超えるまで上昇し続けるプログラムになります。

```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる

tof = 100 # 飛行高度を格納する変数の初期値

while tof < 1500: # 変数 ft が1500以下の場合、以下を実行する
    tof = drone.get_tof() # ドローンの飛行高度がミリ単位で入る。
    drone.up(20) # 20cm づつ上昇

drone.land()
```

- **ToF センサーからの絶対高度を取得します。**<br>
　このコマンドで取得される飛行高度は、ドローン本体下部に搭載された ToF センサーからの地表から機体までの距離となります。**離陸地点からの飛行高度ではありません。**

- **飛行高度の単位は mm です。**<br>
　このコマンドで取得される絶対高度の値は **mm** です。例えば、1500 が返されたら 地表から 1.5m の場所を飛行していることを指します。<br>

　ToF センサーは、100mm 以下を検知することはできないため、最小値は 100 となります。
## 関連コマンド
- [get_battery コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_battery.md)
- [get_speed コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_speed.md)
- [get_flighttime コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_flighttime.md)
- [get_get_height コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_height.md)
- [get_imu コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_imu.md)
