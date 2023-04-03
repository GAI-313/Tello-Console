# flip コマンド

```flip(dir)```
<br>

　このコマンドは、任意の方向に宙返りさせます。<br>

　以下の引数を取得します。引数に入れる値は **str** で、**"f"** 、**"b"** 、**"r"** 、**"l"** のみ利用できます。これ以外の値を入れるとエラーとなります。

- **第1引数：dir**<br>
　この引数は、ドローンをどの方向に宙返りさせるかを設定します。たとえば、この引数に "f" を入れると、ドローンは 前方に宙返りします。

　以下のサンプルコードでは、ドローンを 40 cm 前進させます。

    - **"f"** : 前方に宙返りさせます
    - **b"** : 後方に宙返りさせます
    - **"r"** : 右方に宙返りさせます
    - **"l"** : 左方に宙返りさせます

以下のサンプルコードは、前方、後方、右、左方向の順番でドローンを宙返りさせます。
```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる

drone.flip("f")
drone.flip("b")
drone.flip("r")
drone.flip("l")
```

- このコマンドは、**ドローンのバッテリー残量が 50 % 以上** の状態でのみ機能します。バッテリー残量が 50% を切ると、このコマンドは使用できません。<br>
　Telllo-Console は、注意としてバッテリー残量が 50% を下回ると以下の注意文を表示して flip コマンドが使用できない趣旨を伝えます。
    ```bash
    注意: バッテリー残量が 50% 以下です。flip コマンドは無効になります。
    ```

## 関連コマンド

- [back コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/back.md)
- [up コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/up.md)
- [down コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/down.md)
- [left コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/left.md)
- [right コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/right.md)
- [ccw コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/ccw.md)
- [cw コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/xw.md)
