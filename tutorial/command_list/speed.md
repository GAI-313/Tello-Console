# speed コマンド
```speed(cm)```<br>

　このコマンドは、**cm** 引数を取得します。この引数は int 型で受け取る必要があります。範囲は 10~100 をとります。<br>

　この引数を渡すことで、任意の速度で飛行コマンドを実行させます。以下のサンプルコードは、飛行速度を変更して飛行コマンドを実行します。

```python
from modules.tello import console

drone = console()

drone.takeoff() # ドローンを離陸させる
drone.speed(10) # 10cm/s で飛行するようにする
drone.forward(100)
drone.speed(100) # 100cm/s で飛行するようにする
drone.back(100) 
drone.land()
```

## 関連コマンド
- [wait コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/wait.md)
- [stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/stop.md)
