# downvision コマンド
```downvision(dir)```<br>

　このコマンドは、**dir** 引数を取得します。この引数は 0 または 1 のみを取得します。<br>

　このコマンドを実行することで、カメラデータ取得場所を変更することができます。引数 dir に 1 を与えると、ドローンの下方カメラからのビデオデータを取得できます。引数 dir に 0 を与えると、ドローンの前方メインカメラからカメラデータを取得します。以下のサンプルコードでは、キーボード 1 と 2 を押すことで、カメラビュー位置を切り替えることができます。
```python
from modules.tello import console
import cv2 # opencv をインポート

drone = console()

while True:
    frame = drone.frame # ドローンからカメラデータを取得
    if frame is None or frame.size == 0: # カメラデータが破損または取得できなかった場合は上から再実行
        continue

    cv2.imshow("CAMVIEW", frame) # カメラビューを表示
    key = cv2.waitKey(1) & 0xFF # キーボード入力を感知する変数

    if key == ord("1"):
        drone.downvision(1) # 1キーを押されたら下方カメラへアクセス
    elif key == ord("2"):
        drone.downvision(0) # 2キーが押されたら前方カメラへアクセス
    elif key == 27:
        break # ECS キーが押されたら終了

cv2.destroyAllWindows()
```

## 関連コマンド
- [stream コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/stream.md)
