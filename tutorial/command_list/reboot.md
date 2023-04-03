# reboot コマンド

```reboot()```
<br>

　このコマンドを実行すると、console を停止して、ドローンを再起動させます。以下のサンプルコードは、ドローンを再起動させるプログラムになります。

```python
from modules.tello import console

drone = console()

drone.reboot()
```

- 飛行中にこのコマンドを実行しないでください（今度修正予定）
- 再起動後は、もう一度ドローンとの接続を行なってください。

## 関連コマンド
- [emergency コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/reboot.md)
