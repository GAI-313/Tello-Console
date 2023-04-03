# get_battery コマンド

```get_battery()```

　ドローンのバッテリー残量を取得します。以下のサンプルコードでは、ドローンのバッテリー残量が 20% 以下になったら着陸するプログラムになります。

```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる

bt = drone.battery() # 飛行時間を格納する変数の初期値

while bt > 20: # 変数 bt が20以上の場合、以下を実行する
    bt = drone.get_battery() # ドローンの飛行時間が入る。

drone.land()
```

- **バッテリー残量は常に 5秒間隔でバックグラウンドで更新されています。**<br>
　このコマンドを使うことで、リアルタイムでのバッテリー残量を取得することができますが、Tello-Console では、**5秒おきにバッテリー残量のチェックが入ります。** consoke クラスから battery_level 変数を取得することで、5秒おきに更新されているバッテリー残量を取得できます。余計なプロセスをさきたい場合は、この方法をお勧めします。

## 関連コマンド

- [get_flighttime コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_flighttime.md)
- [get_tof コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_tof.md)
- [get_imu コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_imu.md)
- [get_height コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_height.md)
- [get_speed コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_speed.md)
