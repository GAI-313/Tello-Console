# land コマンド

```land()```
<br>

　ドローンを着陸させるコマンドです。以下のサンプルコードで、ドローンを着陸させることができます。着陸後、**[takeoff コマンド]()** 、**[throwfly コマンド]()** 、**[motor_start コマンド]()** を使用してドローンを離陸させることができます。

- このコマンドを使用すると、その場でドローンは高度を下げ着陸します。
- **[rc コマンド]()** によるドローン操作が渡されている状況下でこのコマンドを実行すると、ドローンは **操作出力を保持しながら着陸を行います。**<br>　
例えば、rc コマンドによって Elevator 出力 100 をドローンに送信すると、ドローンは **出力 100%  で前に進みながら着陸を行います。**
- land コマンドは、**[stop コマンド]()** でキャンセルできます。

```python
from modules.tello import console

drone = console()

drone.land()
```

## 関連コマンド
- [takeoff コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/takeoff.md)
- [emergency コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/emergency.md)
- [stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/stop.md)
- [motor_stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/motor_stop.md)
- [motor_start コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/motor_start.md)

