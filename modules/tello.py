# -*- coding: utf-8 -*-

# 稼働させるのに必要なモジュールをインポート
# V6.2.0

import threading    # 並列処理させるためのモジュール
import socket       # Tello は UDP 通信で PC とデータやりとりするため、ソケット通信を管理するモジュール
import time         # プログラムの一時停止などの時間関連を管理するモジュール
import sys          # プログラムを強制終了することを目的とするモジュール
import cv2          # ビデオデータ、画像処理をするモジュール
import re           # 文字列から数字を取得するために使用するモジュール

# Windows ユーザーの方は以下のプログラム上下にある """ を削除してください
"""
import ctypes
 
ENABLE_PROCESSED_OUTPUT = 0x0001
ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING
 
kernel32 = ctypes.windll.kernel32
handle = kernel32.GetStdHandle(-11)
kernel32.SetConsoleMode(handle, MODE)
"""
# Windows ユーザーの方はこのテキストの上のプログラム上下にある """ を削除してください


# メインクラス
class console:
# このクラスが呼び出されたら最初に実行される init 関数
    def __init__(self,recv_output_frag=None, langage="jp"):
        '''
        ドローンと PC との接続を確認、確立させたのち、以下の確認を行います。
        SDK バージョンの確認。
        バッテリー残量の確認。
        これらの確認が取れたら、
        ビデオ通信の安定化。
        を行います。
        '''
        SYS_VER = '6.3.0'
        print('\x1b[32m'+"WELCOME CONSOLE ! TELLO-CONSOLE V%s"%(SYS_VER)+'\x1b[0m') # このモジュールのバージョンを最初に表示します。

        # 必要な変数の初期値を設定
        self.response = None # ドローンからの応答を格納する変数
        self.MAX_WAIT_TIME = 3 # コマンドを送信してから応答があるまでのタイムアウトを定義
        self.timeout_frag = False # ドローンからの応答がなかったらこのフラグが立つ
        self.recv_output_frag = recv_output_frag # ターミナルに出力結果を表示させるかどうかを苦伐するフラグ
        self.flight_frag = False # ドローンが離陸したら立ち上がるフラグ
        self.flight_timeout_frag = False # 飛行中コマンド送信なしの中13秒経過すると立ち上がるフラグ
        self.vision_frag = False
        self.cap = None # ドローンからのキャプチャデータを格納する変数
        self.frame = None #キャプチャデータを読み込んだ際のデータを格納する変数
        self.error_msg = None # メインプログラムにこのクラス内で発生したエラーを返すための変数
        self.current_time = time.time() # 現在の経過時刻を取得
        self.current_time_fun = self.current_time
        self.pre_time = self.current_time # 現在時刻を補完する変数
        self.request = "command" # timeout_thread に送信するデフォルトのコマンド
        self.lang = langage # レスポンス時の使用言語
        
        # tello との接続を確立させる
        self.local_ip = ''
        self.local_port = 8889
        self.local_video_port = 11111
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port)) # ここでドローンとの接続を行う

        # _recv_thread の並列実行のためのセットアップ
        self.recv_thread = threading.Thread(target=self._recv_thread)
        self.recv_thread.daemon = True
        self.recv_thread.start()

        # tello の ipアドレスと接続ポートを確認
        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.tello_video_address = 'udp://@0.0.0.0:11111'

        # コマンドログ
        self.cmd_log = []

        # 'command'というコマンドを送信してドローンをSDKモードにする
        self.send_cmd('command', True)

        # バッテリー残量チェック
        self.battery_check()

        # 'streamon'コマンドでビデオ通信用ポートを解放する
        self.send_cmd('streamon')

        # SDK バージョンを確認
        self.sdk_check()

        # ビデオ受信メソッド _recv_video_thread を並列実行させる
        self.recv_video_thread = threading.Thread(target=self._recv_video_thread)
        self.recv_video_thread.daemon = True
        self.recv_video_thread.start()

        # タイムアウトスレッドを構築
        self.timeout_thread = threading.Thread(target=self._timeout_thread)
        self.timeout_thread.daemon = True
        self.timeout_thread.start()

        while True:
            if self.frame is not None:
                if self.lang == "jp":
                    print('\x1b[32m'+"セットアップ完了！"+'\x1b[0m')
                else:
                    print('\x1b[32m'+"SET UP IS DONE"+'\x1b[0m')
                time.sleep(1)
                break
    
    def battery_check(self):
        """
        ドローンのバッテリー残量を確認し、正常にプログラムを実行できるかどうかを診断します。
        """
        battery = self.send_cmd("battery?")
        while True:
            if battery != "None response":
                battery = re.sub(r"\D", "", battery)
                if int(battery) <= 10:
                    if self.lang == "jp":
                        print('\x1b[31m'+"バッテリー残量がわずかです！バッテリーを充電、交換してください！"+'\x1b[0m') # バッテリー残量が10％％以下の場合プログラムは停止する。
                    else:
                        print('\x1b[31m'+"LOW BATTERY PLEASE CHANGE BATTERY AND CHARGE IT."+'\x1b[0m') # バッテリー残量が10％％以下の場合プログラムは停止する。
                    sys.exit()
                elif int(battery) < 50:
                    if self.lang == "jp":
                        print('\x1b[33m'+"注意: バッテリー残量が 50% 以下です。flip コマンドは無効になります。"+'\x1b[0m') # flip コマンドが使えなくなることを警鐘
                    else:
                        print('\x1b[33m'+"WARNING: BATTERY LEVEL IS LESS 50%. CAN'T USE FLIP CMD!"+'\x1b[0m') # flip コマンドが使えなくなることを警鐘
                time.sleep(3)
                break
            else:
                 battery = self.send_cmd("battery?")
    
    def sdk_check(self):
        """
        ドローンのファームウェアバージョンを確認し、正常にプログラムを実行できるかどうかを診断します。
        """
        sdk = self.send_cmd("sdk?")
        while True:
            if sdk == "None response":
                sdk = self.send_cmd("sdk?")
            else:
                if int(sdk) < 30:
                    if self.lang == "jp":
                        print('\x1b[33m'+"警告!:downvision コマンドは使用できません。"+'\x1b[0m')
                        print('\x1b[33m'+"ヒント:お使いのドローンのファームウェアを更新してください。"+'\x1b[0m')
                    else:
                        print('\x1b[33m'+"WARNING!: THIS VERSION IS CAN'T USE DOWNVISION CMD !"+'\x1b[0m')
                        print('\x1b[33m'+"TIPS!: YOU SHOULD BE UPDATE THIS AIRCRAFT'S FW"+'\x1b[0m')
                break

    def __del__(self):
        '''
        このクラスが削除されると呼び出されるメソッド 'デストラクタ'。
        ほとんど実行されることがないので質素である。
        '''
        print('done')

    def send_cmd(self, cmd,start=None):
        try:
            '''
            ドローンにコマンドを送信するメソッドです。
            このメソッドがこのクラスにおいて最も重要なところで、ほぼ全てのメソッドはこのメソッドによって機能しています。
            このメソッドには以下の引数を必要とします。
            cmd = str : ドローンに送信するコマンド文を格納します。
            start = None or True : 通常時はこの引数を必要としません。この引数はイニャライザでのみ使われます。
            '''
            self.cmd_log.append(cmd) # ここで再入されたコマンドをログに格納する
            self.socket.sendto(cmd.encode('utf-8'), self.tello_address) # ここでs代入されたコマンドをドローンに送信する
            if self.lang == 'jp':
                print('\x1b[37m'+'コマンド<%s>を送信しました…'%(cmd)+'\x1b[0m')
            else:
                print('send command <%s>...'%(cmd))

            # タイマーを動かすスレッドを回す。
            timer = threading.Timer(self.MAX_WAIT_TIME, self.set_timeout_frag)
            timer.start()

            # 応答が来るまで待つ、しかし3秒経過したらタイムアウトする
            while self.response is None:
                if self.timeout_frag is True:
                    if self.lang == "jp":
                        print('タイムアウト!')
                    else:
                        print('timeout!')
                    break
            timer.cancel() # タイマーを停止させる

            self.pre_time = self.current_time
            self.timeout_frag = False
            
            # 応答を確認する
            if self.response is None:
                response = "None response"
            else:
                response = self.response.decode('utf-8')
                self.cmd_log.append(cmd)
                # どんなエラーや問題が出たのかをここで処理する

            if self.recv_output_frag is False:
                pass
            else:
                if self.lang == 'jp':
                    print('\x1b[37m'+'ドローンから応答<%s>を受信しました…'%(response)+'\x1b[0m')# どんなコマンドを送信したかをターミナルに反映        
                else:
                    print('\x1b[37m'+'recv <%s> by drone ...'%(response)+'\x1b[0m')# どんなコマンドを送信したかをターミナルに反映        
                
            self.response = None # 応答変数を初期化

            if cmd == "command" and start is True: # ここでドローンと正常に接続されているかどうかを判定する
                if response == "None response":
                    if self.lang == "jp":
                        print('\x1b[31m'+"エラー！ドローンとの通信に失敗しました！"+'\x1b[0m')
                        print('\x1b[33m'+"Tips:ドローンとPCとのWi-Fi接続を確認してください！"+'\x1b[0m')
                        error_msg = ["エラー！ドローンとの通信に失敗しました！", "Tips:ドローンとPCとのWi-Fi接続を確認してください！"]
                    else:
                        print('\x1b[31m'+"ERROR CAN'T START CONSOLE! DRONE IS NOT FOUND.PLZ CONNECT THE DRONE!"+'\x1b[0m')
                        print('\x1b[33m'+"TIPS: CHECK THE WI-FI CONNECTION TO DRONE"+'\x1b[0m')
                    self.error_msg = "None_Defined_Drone"
                    self.result_deliver(error_msg)
                    sys.exit()

            # エラー判定
            if "unknown command" in response:
                if self.lang == "jp":
                    print('\x1b[31m'+"コマンドエラー！未知のコマンド" + cmd + " を取得しました。プログラムは強制停止します。"+'\x1b[0m') # 未知のコマンドが送信されたらプログラムは停止する
                else:
                    print('\x1b[31m'+"COMMAND ERROR! YOU SEND UNKNOWN COMMAND >>> " + cmd +'\x1b[0m') # 未知のコマンドが送信されたらプログラムは停止する
                sys.exit()
            
            if response == "error Not joystick" or response == "error Run timeout": # コマンド送信時にタイムアウト、もしくは joystick エラーが発生した際に渡されたコマンドを再送信する。
                if self.lang == "jp":
                    print('\x1b[33m'+"飛行コマンドエラー！再試行します…")
                else:
                    print('\x1b[33m'+"FLIGHT CMD ERROR RETRY SEND IT")
                self.send_cmd(cmd)

            elif response == "error Auto land":
                if self.lang == "jp":
                    print('\x1b[31m'+"重度なエラーが発生しました。自動着陸します。"+'\x1b[0m') # 何かしらの原因でmドローンが自動着陸した際に発生するエラー。代替はローバッテリー。
                else:
                    print('\x1b[31m'+"EMERGENCY ERROR OCCURED !"+'\x1b[0m') # 何かしらの原因でmドローンが自動着陸した際に発生するエラー。代替はローバッテリー。
            
            elif response == "error No valid imu":
                if self.lang == "jp":
                    print('\x1b[33m'+"IMU パンクエラー！姿勢維持のため機体をホバリングさせます。"+'\x1b[0m') # IMU に異常をきたしたまたはドローンの姿勢書くが期待値以上に傾いている場合に発生するエラー。この時ドローンをホバリングさせる。
                else:
                    print('\x1b[33m'+"IMU VALID ERROR TOO MUCH DRONE ATTITUDE!"+'\x1b[0m') # IMU に異常をきたしたまたはドローンの姿勢書くが期待値以上に傾いている場合に発生するエラー。この時ドローンをホバリングさせる。
                self.stop()
            return response
        
        except KeyboardInterrupt:
            sys/exit()
        except OSError:
            if self.lang == "jp":
                print('\x1b[33m'+"接続エラー。ドローンとの接続に問題が発生しました。"+'\x1b[0m') # IMU に異常をきたしたまたはドローンの姿勢書くが期待値以上に傾いている場合に発生するエラー。この時ドローンをホバリングさせる。
            else:
                print('\x1b[33m'+"CONNECTION ERROR"+'\x1b[0m') # IMU に異常をきたしたまたはドローンの姿勢書くが期待値以上に傾いている場合に発生するエラー。この時ドローンをホバリングさせる。
            sys/exit()
            
        except OSError:
            # ドローンとの接続中に 0SError が発生する原因は Wi-Fi接続中にプログラムを実行することである。そのためのアドバイス文を送りプログラムを停止させる。
            if self.lang == "jp":
                print('\x1b[31m'+"接続エラー！ドローンのと接続に問題が発生しました。"+'\x1b[0m')
                print('\x1b[33m'+"ドローンとのWi-Fiによる接続が完全に終了していない状態でプログラムは実行できません。\nドローンが他のデバイスに既に接続されている場合はプログラムを実行できません。"+'\x1b[0m')
            else:
                print('\x1b[31m'+"CONNECTION ERROR THIS DRONE's SSID HAVE A ISSUES!"+'\x1b[0m')
                print('\x1b[33m'+"MAYBE NOT READY TO CONNECT THE DRONE. PLZ WAIT AFTER RETRY"+'\x1b[0m')
            sys.exit()

        except Exception:
            import traceback
            traceback.print_exc()

    def _recv_thread(self):
        '''
        ドローンからの応答を監視するメソッドです。
        threading によって稼働します。通常のメソッドとして使用することは前提としていません。
        '''
        while True:
            try:
                self.response, ip = self.socket.recvfrom(3000) # ここで応答を受け取る
            
            except (KeyboardInterrupt, Exception):
                break

    def _recv_video_thread(self):
        '''
        ドローンからのビデオデータを取得し、エンコードするメソッドです。エンコードされたビデオデータは self.frame に格納されます。
        threading によって稼働します。通常のメソッドとして使用することは前提としていません。
        '''
        if self.cap is None: # cap に何もない場合はドローンからのカメラデータを格納させる
            self.cap = cv2.VideoCapture(self.tello_video_address)
        if not self.cap.isOpened(): # cap データが解放されていない場合は解放する
            self.cap.open(self.tello_video_address)
        
        time.sleep(0.5)
        while True:
            try:
                ret, frame = self.cap.read() # cap から取り込まれたデータを frame に格納する

                if self.vision_frag == True:
                    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                else:
                    frame = frame

                self.frame = frame
            except KeyboardInterrupt:
                break
            except Exception:
                import traceback
                traceback.print_exc()

    def _timeout_thread(self):
        '''
        ドローンのタイムアウト（コマンド未送信状態が15秒経過するとドローンが着陸してしまう）する問題を回避、監視するメソッドです。
        threading によって稼働します。通常のメソッドとして使用することは前提としていません。
        '''
        while True:
            try:
                self.current_time = time.time()
                #print(int(self.current_time-self.pre_time),self.response)

                if self.current_time - self.pre_time > 10:

                    self.send_cmd(self.request)
                    self.pre_time = self.current_time
            except KeyboardInterrupt:
                break
            
            except Exception:
                import traceback
                traceback.print_exc()
    
    def result_deliver(self, msg):
        return msg

# ドローン操作メソッド群    
    def set_timeout_frag(self):
        try:
            """
            このメソッドはコマンドを送信して任意の時間が経過してもドローンからの応答がなかった際に実行されるフラグメソッドです。このメソッドが実行されると timeout エラーが発生します。
            """
            self.timeout_frag = True
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def wait(self, sec):
        try:
            """
            waiit : ドローンを引数分待機させる。飛行中は引数分ホバリングします。
            引数: sec = int or float = ドローンの待機時間(sec/秒)
            ドローンを time.sleep で待機させます。そのため本クラスを使用するスクリプトに time モジュールは必要ありません。
            このメソッドはドローンからのレスポンスは受け付けないため、直接結果を反映します。
            """
            res = "Drone is wait: %d sec"%(sec)
            time.sleep(sec)
            print(res)
            return res
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def takeoff(self):
        try:
            '''
            takeoff: ドローンを自動離陸させる。
            引数は取りません。
            '''
            return  self.send_cmd('takeoff')
        except:
            import traceback
            traceback.print_exc()
            sys.exit()


    def land(self):
        try:
            '''
            land: ドローンを自動着陸させる、
            引数は取りません。
            '''
            return self.send_cmd('land')
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def emergency(self):
        try:
            '''
            emergency: ドローンのモーターを停止させます。
            飛行中に実行されるとドローンは揚力を失いその場で墜落します。
            引数は取りません。
            '''
            return self.send_cmd('emergency')
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def stop(self):
        try:
            '''
            stop: ドローンを停止させます。飛行中でもこのコマンドが実行されると移動を停止しその場でホバリングさせます。
            引数は取りません。
            '''
            self.send_cmd("rc 0 0 0 0")
            return self.send_cmd('stop')
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def rc(self, elron, elevator, srotol, lador):
        try:
            '''
            rc: ドローンにRCコントローラー出力を送信します。
            引数: elron, elevator, srotol, laddor = int (-100 < all args < 100)
            ドローンの 2ch コントローラー同様の出力値を4つの引数で送信します。
            elron = 期待左右移動　負の値だと左移動になります。
            elevator = 機体前進後進移動　負の値だと後進します。
            srotol = 機体上昇下降移動　負の値だと下降します。
            laddor = 機体左右旋回　負の値だと機体は左回転します。
            '''

            return self.send_cmd('rc {} {} {} {}'.format(elron, elevator, srotol, lador))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def speed(self,cm):
        try:
            '''
            speed: ドローンの飛行スピードを設定します。
            引数 cm = int (ドローンを毎秒何 cm/s で飛行させるか定義します。 10 < cm < 100)
            '''
            if cm < 10:
                cm = 10
            if cm > 100:
                cm = 100
            return self.send_cmd("speed {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def forward(self,cm):
        try:
            '''
            forward : ドローンを前進させます。
            引数 cm = int (ドローンを何 cm 前進させるか定義します。 20 < cm < 500)
            '''
            if cm < 20:
                cm = 20
            if cm > 250:
                cm = 250
            return self.send_cmd("forward {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def back(self,cm):
        try:
            '''
            back : ドローンを後進させます。
            引数 cm = int (ドローンを何 cm 後進させるか定義します。 20 < cm < 500)
            '''
            if cm < 20:
                cm = 20
            if cm > 250:
                cm = 250
            return self.send_cmd("back {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def right(self,cm):
        try:
            '''
            right : ドローンを右移動させます。
            引数 cm = int (ドローンを何 cm 右移動させるか定義します。 20 < cm < 500)
            '''
            if cm < 20:
                cm = 20
            if cm > 250:
                cm = 250
            return self.send_cmd("right {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def left(self,cm):
        try:
            '''
            left : ドローンを左移動させます。
            引数 cm = int (ドローンを何 cm 左移動させるか定義します。 20 < cm < 500)
            '''
            if cm < 20:
                cm = 20
            if cm > 250:
                cm = 250
            return self.send_cmd("left {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def up(self,cm):
        try:
            '''
            up : ドローンを上昇させます。
            引数 cm = int (ドローンを何 cm 上昇させるか定義します。 20 < cm < 500)
            '''
            if cm < 20:
                cm = 20
            if cm > 250:
                cm = 250
            return self.send_cmd("up {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def down(self,cm):
        try:
            '''
            down : ドローンを下降させます。
            引数 cm = int (ドローンを何 cm 下降させるか定義します。 20 < cm < 500)
            '''
            if cm < 20:
                cm = 20
            if cm > 250:
                cm = 250
            return self.send_cmd("down {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def cw(self,dig):
        try:
            '''
            cw : ドローンを右旋回（時計回り）させます。
            引数 dig = int (ドローンを何度右旋回させるか定義します。 1 < cm )
            '''
            if dig < 1:
                dig = 1
            if dig > 360:
                dig = 360
            return self.send_cmd("cw {}".format(dig))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def ccw(self,dig):
        try:
            '''
            ccw : ドローンを右旋回（反時計回り）させます。
            引数 dig = int (ドローンを何度左旋回させるか定義します。 1 < cm )
            '''
            if dig < 1:
                dig = 1
            if dig > 360:
                dig = 360
            return self.send_cmd("ccw {}".format(dig))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def flip(self, dir):
        try:
            '''
            flip : ドローンを任意の方向にフリップ（宙返り）させます。バッテリー残量が50%以下だと利用できません。
            引数 dir = str (f, b, l, r の指定された文字列を使用。)
            f = 前方にフリップ
            b = 後方にフリップ
            l = 左方向にフリップ
            r = 右方向にフリップ
            '''
            return self.send_cmd("flip {}".format(dir))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def go(self, x,y,z,s):
        try:
            """
            go : ドローンを任意の方向へ飛行させます。
            引数 x, y, z, s = int (それぞれ設定範囲あり。)
            x = ドローンの水平横移動。正の値の場合は全身、負の値の場合は後進 -500 < x < -20, 20 < x < 500
            y = ドローンの水平横移動。正の値の場合は右移動、負の値の場合は左移動 -500 < x < -20, 20 < x < 500
            z = ドローンの上昇横移動。正の値の場合は上昇、負の値の場合は下降 -500 < x < -20, 20 < x < 500
            s = ドローンの飛行スピードを設定(cm/s) 10 < x < 100
            """
            if x > 500:
                x = 500
            elif x < -500:
                x = 500
            elif x < 20 and x > 0:
                x = 20
            elif x > -20 and x < 0:
                x = -20
            
            if y > 500:
                y = 500
            elif y < -500:
                y = 500
            elif y < 20 and y > 0:
                y = 20
            elif y > -20 and y < 0:
                y = -20
            
            if z > 500:
                z = 500
            elif z < -500:
                z = 500
            elif z < 20 and z > 0:
                z = 20
            elif z > -20 and z < 0:
                z = -20
            
            if s < 10:
                s = 10
            if s > 100:
                s = 100
            
            response = self.send_cmd("go %d %d %d %d"%(x,y,z,s))
            return response
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def motor_start(self):
        try:
            '''
            motor_start : rc コマンドを使用してモーターを自動起動させます。
            ドローンは離陸しません。飛行中にこのコマンドを使用しないでください。
            '''
            response = self.send_cmd('rc -100 -100 -100 100')
            time.sleep(1)
            return response
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

# ドローンの設定を変更するメソッド群
    def downvision(self, angle):
        try:
            '''
            downvision : 下方カメラ、前方カメラを切り替えます。
            引数 angle = int (0 ,1 以外の数字は使用できません。)
            angle = 1 : 下方カメラに切り替わります。
            angle = 0 : 前方カメラに切り替わります。
            '''
            if angle == 1:
                self.vision_frag = True
            else:
                self.vision_frag = False
            
            return self.send_cmd('downvision {}'.format(angle))

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def stream(self, video=1):
        try:
            """
            stream : ドローンのビデオデータ通信を有効、無効に設定します。
            引数 video = int (0, 1 以外の数字は使用できません。)
            video = 1 : ドローンのビデオデータ通信を有効にします。
            video = 0 : ドローンのビデオデータ通信を無効にします。
            """
            if video == 1:
                response = self.send_cmd('streamon')
            elif video == 0:
                response = self.send_cmd('streamoff')
            
            return response
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

# ドローンステータス取得メソッド群
    def get_flighttime(self):
        try:
            response = self.send_cmd('time?')
            if response != "None response":
                if "s" in response:
                    response = re.sub(r"\D", "", response)
                    return int(response) 
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_tof()
            return response

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
 
    def get_tof(self):
        try:
            '''
            get_tof : ドローン下部に搭載された ToF センサーから対地高度を取得します。
            返り値: ToF からの対地高度 (int / mm)
            '''
            response = self.send_cmd('tof?')

            if "mm" in response:
                response = re.sub(r"\D", "", response)

                if response != "None":
                    buckup = response
                else:
                    response = buckup

                return int(response)
            
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_tof()
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def get_height(self):
        try:
            '''
            get_height : IMU センサーをもとに現在の飛行高度を取得します。
            返り値: IMU データからの飛行高度 (int / cm)
            注意: ToF とは違う高度を返す場合がありますが、get_height から得る高度は相対高度。get_tofから得る高度は絶対高度です。
            正確な高度を求める場合は get_tof をお勧めします。
            '''
            response = self.send_cmd('height?')

            if "dm" in response:
                response = re.sub(r"\D", "", response) 
                return int(response)
            
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_tof()
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def get_battery(self):
        try:
            '''
            get_battery : ドローンからのバッテリー残量を取得します。
            返り値:ドローンのバッテリー残量 (int / % 0 ~ 100)
            '''
            response = self.send_cmd('battery?')
            if response == "None response" or response == "ok":
                pass
            else:
                return int(response)
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def get_speed(self):
        try:
            '''
            get_speed : ドローンの現在の飛行スピードを取得します
            返り値: ドローンに設定された飛行スピード (float / cm/s)
            '''
            response = self.send_cmd('speed?')
            return float(response)

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def get_imu(self):
        try:
            '''
            get_imu : ドローンの現在の飛行スピードを取得します
            返り値: ドローンに設定された飛行スピード (float / cm/s)
            '''
            res = self.send_cmd('attitude?')

            if 'pitch' in res:
                res = re.findall(r"\d+", res)
                response = [int(s) for s in res]
                buckup = response
                return response
            
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_imu()

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    # その他の設定メソッド群
    def ask_cmd(self, cmd):
        try:
            """
            ask_cmd : コマンドタイムアウト時に一定感覚で送信するコマンドの設定を変更します。
            引数 cmd = 定期的に送信するコマンド (str) 小窓ではない文字列を記述するとエラーになります。
            """
            self.request = cmd
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
