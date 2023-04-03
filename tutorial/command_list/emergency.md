# emergency コマンド

```emergency()```
<br>

 ドローンを緊急停止させるコマンドです。このコマンドを実行すると、飛行中のドローンのモーターを停止させ、**自立的に墜落させます。**
以下のサンプルコードは、Control + C でプログラムが停止された時に emergency コマンドを実行するプログラムになります。
 
```python
from modules.tello import console

drone = console()
drone.takeoff() # ドローンを離陸させる

try:
    # ドローンが 100cm 上昇下降を繰り返す
    while True:
        drone.up(100)
        drone.down(100)

# Control + C が押されたることを例外処理で検知
except KeyboardInterrupt:
    drone.emergency() # ドローンを緊急停止
```

- このコマンドを実行すると、ドローンが緊急停止するとともに、**console プログラムも停止します。**
- emergency が実行された後に、**コマンドを使ってドローンを再度離陸させることはできません。**
- 緊急対策用にこのコマンドを使用してください。常用するとドローンが破損する恐れがあります。

## emergency コマンドの関連コマンド
- [reboot コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/reboot.md)
- [stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/stop.md)
