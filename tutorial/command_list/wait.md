# wait コマンド
```wait(sec)```<br>

　このコマンドは、**sec** 引数を取得します。この引数は int または float 型で受け取る必要があります。<br>

　この引数を渡すことで、任意の時間ドローンを待機させることができます。以下のサンプルコードは、5秒間ドローンを待機させます。

```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる
drone.wait(5) # 5秒間待機
drone.land()
```

## 関連コマンド
- [speed コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/speed.md)
