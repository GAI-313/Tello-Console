# Takeoff コマンド

```takeoff()```
<br>

　ドローンを離陸させるコマンドです。以下のサンプルコードで、ドローンを離陸させることができます。実行後、ドローンは **land コマンド**、**emergency コマンド** を受け取るまたはバッテリー残量が 10% 以下になるまで飛行し続けます。

- このコマンドを使用すると、**ドローンは 120 cm 上昇します。** 周囲に気をつけて使用してください。

```python
from modules.tello import console

drone = console()

drone.takeoff()
```

## 関連コマンド
- [forward コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/forward.md)
- [land コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/takeoff.md)
- [emergency コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/emergency.md)
