# stop コマンド

```stop()```
<br>

　このコマンドを実行すると、飛行または移動しているドローンをその場で停止させることができます。ここでいう停止とは、モーターを停止させるのではなく移動を中止させてその場でホバリングさせることを指します。以下のサンプルコードでは、Control + C が押されたらドローンの飛行を中止させ、5秒後に着陸させます。

```python
from modules.tello import console

drone = console()

drone.takeoff()

try:
    # ドローンが 100cm 上昇下降を繰り返す
    while True:
        drone.up(100)
        drone.down(100)

# Control + C が押されたることを例外処理で検知
except KeyboardInterrupt:
    drone.stop() # ドローンを停止
    drone.stop(5) # 5 秒待機
    drone.land # ドローンを着陸
```

- **[rc コマンド]()** からの出力も全て停止させます。
- ホバリングをさせることを意図していますが、環境によって正常に穂バイ＼リングできない場合があります。
- 安全にドローンを停止させたい場合は、stop コマンドの後に **[land コマンド]()** で着陸させると良いでしょう。

## 関連コマンド
- [land コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/land.md)
- [emergency コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/emergency.md)
