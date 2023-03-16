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

- [get_battery コマンド]()
- [get_tof コマンド]()
- [get_flighttime コマンド]()
- [get_height コマンド]()
- [get_speed コマンド]()
