# motor_start コマンド

```motor_start()```
<br>

　このコマンドを実行すると、その場でドローンのモーターを起動させます。**[rc コマンド]()** と併用することで高度な飛行プログラムを構築できます。以下のサンプルコードは、motor_start コマンドでモーターを起動させ、rc コマンドで 20% 出力で 2秒間上昇するプログラムです。
```python
from modules.tello import console

drone = console()

drone.motor_start() # モーター始動
drone.rc(0,0,20,0) # スロットルに 20 出力
drone.wait(2) # 2秒待機
drone.stop() # rc コマンド出力を停止
```

- このコマンド単体ではドローンを離陸させることはできません。
- このコマンドは CSC コマンドをスクリプト化したものです。rc コマンドと併用することを前提としています。
- **[motor_stop コマンド]()** でモーターを止めることができます。

# 関連コマンド
- [motor_stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/motor_stop.md)
- [land コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/land.md)
- [takeoff コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/takeff.md)
- [rc コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/rc.md)
