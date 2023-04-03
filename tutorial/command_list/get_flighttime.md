# get_flighttime コマンド

```get_flighttime()```

　ドローンの飛行時間を取得します。以下のサンプルコードでは、ドローンからの飛行時間を計測し、飛行時間が1分を超えたら自動着陸します。

```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる

ft = 0 # 飛行時間を格納する変数の初期値

while ft < 60: # 変数 ft が60以下の場合、以下を実行する
    ft = drone.get_flighttime() # ドローンの飛行時間が入る。

drone.land()
```

- **飛行時間は、総飛行時間となります。**<br>
　このコマンドで取得される飛行時間は、1本のバッテリーで飛行した総飛行時間となります。例えば、30秒飛行したのちに一度着陸して、再度離陸した後に当コマンドで飛行時間を取得すると、30からスタートします。

- **飛行時間は、秒単位で刻まれます。**<br>
　ミリ単位での飛行時間は取得できません。当コマンドで取得できる値は int 型です。

## 関連コマンド
- [get_battery コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_battery.md)
- [get_tof コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_tof.md)
- [get_imu コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_imu.md)
- [get_height コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_height.md)
- [get_speed コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_speed.md)
