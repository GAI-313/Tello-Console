# cw コマンド

```cw(dig)```
<br>

 このコマンドは、以下の引数を取得します。引数に入れる値は **int** で、範囲は **1 ~ 360** です。この範囲を超えると自動で修正されます。

- **第1引数：cm**<br>
　この引数は、ドローンを何センチ上昇させるかを設定します。たとえば、この引数に 30 を入れると、ドローンは 30度 時計回りに旋回します。

　以下のサンプルコードでは、ドローンを 90 度右旋回させます。

```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる

drone.cw(90)
```

- このコマンドは **[takeoff コマンド]()** などのドローンを離陸させた後で使用しないとエラーが発生します。

## 関連コマンド

- [back コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/back.md)
- [forward コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/forward.md)
- [down コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/down.md)
- [left コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/left.md)
- [right コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/right.md)
- [ccw コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/ccw.md)
- [flip コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/flip.md)
