# left コマンド

```left(cm)```
<br>

 このコマンドは、以下の引数を取得します。引数に入れる値は **int** で、範囲は **20 ~ 500** です。この範囲を超えると自動で修正されます。

- **第1引数：cm**<br>
　この引数は、ドローンを何センチ左移動させるかを設定します。たとえば、この引数に 30 を入れると、ドローンは 30cm 左移動します。

　以下のサンプルコードでは、ドローンを 40 cm 左移動させます。

```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる

drone.left(40)
```

- このコマンドは **[takeoff コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/takeoff.md)** などのドローンを離陸させた後で使用しないとエラーが発生します。

## 関連コマンド
- [forward コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/forward.md)
- [up コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/up.md)
- [down コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/down.md)
- [back コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/back.md)
- [right コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/right.md)
- [ccw コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/ccw.md)
- [cw コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/cw.md)
- [flip コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/flip.md)
