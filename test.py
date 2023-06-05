from modules.tello import console
import cv2 # opencv をインポート

drone = console()
drone.stream(1)
#drone.set_resolution("low")
drone.downvision(0)

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
