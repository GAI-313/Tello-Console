# get_imu コマンド

```get_imu()```

　ドローンの3次元傾斜を取得します。

```python
pitch, roll, yaw = drone.get_imu()
```
このコマンドは 3 つのデータを返します。

- pitch : 前後の傾き
- roll : 左右の傾き
- yaw : 旋回角度

## 関連コマンド
- [get_battery コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_battery.md)
- [get_tof コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_tof.md)
- [get_flighttime コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_flighttime.md)
- [get_flighttime コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_height.md)
- [get_speed コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_flighttime.md)
