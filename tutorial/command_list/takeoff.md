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

## takeoff コマンドの関連コマンド

- [land コマンド]()
- [emergency コマンド]()
- 

## 類似のコマンド

- [motor_start コマンド]()
