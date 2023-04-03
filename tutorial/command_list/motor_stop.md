# motor_stop コマンド

```motor_stop()```
<br>

　**[motor_start コマンド]()** などによって始動されたモーターを停止するコマンドです。以下のサンプルコードで、モーター起動してから10秒後にモーターを停止させることができます。

```python
from modules.tello import console

drone = console()

drone.motor_start() # モータースタート
drone.wait(10) # 10 秒待機
drone.motor_stop() # モーター停止
```

- このコマンドを使用すると、**飛行中でもモーターを停止させます。** 注意して使用してください。
- **[emergency コマンド]()** と同じように使用しないでください。このコマンドはモーターを停止することを意図しているものであり、緊急用ではありません。

## motor_stop コマンドの関連コマンド
- [land コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/land.md)
- [takeoff コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/takeoff.md)
- [emergency コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/emergency.md)
- [stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/stop.md)
- [motor_start コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/motor_start.md)
