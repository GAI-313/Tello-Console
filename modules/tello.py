# -*- coding: utf-8 -*-

# 稼働させるのに必要なモジュールをインポート
# V6.2.0

import threading    # 並列処理させるためのモジュール
import socket       # Tello は UDP 通信で PC とデータやりとりするため、ソケット通信を管理するモジュール
import time         # プログラムの一時停止などの時間関連を管理するモジュール
import sys          # プログラムを強制終了することを目的とするモジュール
import cv2          # ビデオデータ、画像処理をするモジュール
import re           # 文字列から数字を取得するために使用するモジュール

# Windows ユーザーの方は以下のプログラム上下にある"""を削除してください
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
    def __init__(self,recv=True, language="jp", setup=False):
        """Tello をコマンドで操作できるようにする Tello-Console のコアとなります。

        info:
            console システムを使用するには、このクラスを任意の変数に代入してください。
            drone = console()

        Args:
            recv_output_frag (bool, optional): ドローンとの通信状況を表示するか否かを設定できます、デフォルトは True。
            False にすると、ドローンからの応答が表示されなくなります。他のデータを表示させたいときに便利です。 
            language (str, optional): エラー、警告、ヒントの言語設定を設定します。デフォルトは"jp"。
            jp: 日本語
            us: 英語
            TaskKill (bool, optional): この引数は使用しないでください。現在停止中です。
            True: （デフォルト）エラーを検知したときにプログラムを終了します。
            False: エラーを検知したときプログラムからのレスポンスを渡します。
        """
        SYS_VER = '7.1.0'
        print('\x1b[32m'+"WELCOME CONSOLE ! TELLO-CONSOLE V%s"%(SYS_VER)+'\x1b[0m') # このモジュールのバージョンを最初に表示します。

        # 必要な変数の初期値を設定
        self.response = None # ドローンからの応答を格納する変数
        self.MAX_WAIT_TIME = 5 # コマンドを送信してから応答があるまでのタイムアウトを定義
        self.timeout_frag = False # ドローンからの応答がなかったらこのフラグが立つ
        self.recv_output_frag = recv # ターミナルに出力結果を表示させるかどうかを苦伐するフラグ
        self.flight_frag = False # ドローンが離陸したら立ち上がるフラグ
        self.flight_timeout_frag = False # 飛行中コマンド送信なしの中13秒経過すると立ち上がるフラグ
        self.vision_frag = False # VPS カメラの画角を反転させるフラグ
        self.killer_frag = False # 各スレッドメソッドを停止（キル）するフラグ。試験用
        self.cap = None # ドローンからのキャプチャデータを格納する変数
        self.frame = None #キャプチャデータを読み込んだ際のデータを格納する変数
        self.current_time = time.time() # 現在の経過時刻を取得
        self.current_time_fun = self.current_time # 現在時刻情報のバックアップ
        self.pre_time = self.current_time # 現在時刻を補完する変数
        self.lang = language # レスポンス時の使用言語
        self.battery_level = 0 # バッテリー情報を記録する変数
        self.allow_loop = False # ビデオスレッドのループフラグ
        self.backup = [0,0,0,0,0,0] # 各ドローンパラメータをバックアップするリスト。Noneデータエラーを回避する。

        self.ret = False # カメラ受信フラグ
        
        # tello との接続を確立させる
        self.local_ip = ''
        self.local_port = 8889
        self.local_vidoeo_port = 11111
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

        # 'command'というコマンドを送信してドローンをSDKモードにする
        self.send_cmd('command', True, setup=True)

        # バッテリー残量チェック
        self.battery_check()

        # SDK バージョンを確認
        self.sdk_check()

        # タイムアウトスレッドを構築
        self.timeout_thread = threading.Thread(target=self._timeout_thread)
        self.timeout_thread.daemon = True
        self.timeout_thread.start()

        if self.lang == "jp":
                print('\x1b[32m'+"セットアップ完了！"+'\x1b[0m')
        else:
            print('\x1b[32m'+"SET UP IS DONE"+'\x1b[0m')
        time.sleep(1)
    
    def battery_check(self):
        """システムチェック：ドローンのバッテリーチェックを行います。

        警告:
            このプログラムはドローンを診断する専用のメソッドです。通常のメソッドとして使用することは前提とされていません。

        """
        battery = self.send_cmd("battery?", setup=True)
        while True:
            if battery != "None response":
                battery = re.sub(r"\D", "", battery)
                battery = int(battery)
                if battery <= 10:
                    if self.lang == "jp":
                        print('\x1b[31m'+"バッテリー残量がわずかです！バッテリーを充電、交換してください！"+'\x1b[0m') # バッテリー残量が10％％以下の場合プログラムは停止する。
                    else:
                        print('\x1b[31m'+"LOW BATTERY PLEASE CHANGE BATTERY AND CHARGE IT."+'\x1b[0m') # バッテリー残量が10％％以下の場合プログラムは停止する。
                    sys.exit()
                elif battery < 50:
                    if self.lang == "jp":
                        print('\x1b[33m'+"注意: バッテリー残量が 50% 以下です。flip コマンドは無効になります。"+'\x1b[0m') # flip コマンドが使えなくなることを警鐘
                    else:
                        print('\x1b[33m'+"WARNING: BATTERY LEVEL IS LESS 50%. CAN'T USE FLIP CMD!"+'\x1b[0m') # flip コマンドが使えなくなることを警鐘

                if self.lang == "jp":
                    print('\x1b[37m'+'現在のバッテリー残量：%d'%(battery)+'\x1b[0m')
                else:
                    print('\x1b[37m'+'Current battery : %d'%(battery)+'\x1b[0m')
                time.sleep(3)
                self.battery_level = battery
                break
            else:
                 battery = self.send_cmd("battery?", setup=True)
    
    def sdk_check(self):
        """システムチェック：ドローンのバファームウェアバージョンの確認を行います。

        警告:
            このプログラムはドローンを診断する専用のメソッドです。通常のメソッドとして使用することは前提とされていません。

        """
        sdk = None
        while sdk is None or sdk == 'None response':
            sdk = self.send_cmd("sdk?", setup=True)
        if int(sdk) < 30:
            if self.lang == "jp":
                print('\x1b[33m'+"警告!:downvision コマンドは使用できません。"+'\x1b[0m')
                print('\x1b[33m'+"ヒント:お使いのドローンのファームウェアを更新してください。"+'\x1b[0m')
                print('\x1b[33m'+"ヒント:TELLO を接続している場合 TELLO CONSOLE の一部機能は使用できません。"+'\x1b[0m')
            else:
                print('\x1b[33m'+"WARNING!: THIS VERSION IS CAN'T USE DOWNVISION CMD !"+'\x1b[0m')
                print('\x1b[33m'+"TIPS!: YOU SHOULD BE UPDATE THIS AIRCRAFT'S FW"+'\x1b[0m')
        else:
            print('SDK: ver.3.0 Tello-Console 全プロセスにアクセスできます')

    def __del__(self):
        '''
        このクラスが削除されると呼び出されるメソッド 'デストラクタ'。
        ほとんど実行されることがないので質素である。
        '''
        print('done')

    def send_cmd(self, cmd,start=None, None_response_cmd=False, setup=False):
        """ドローンにコマンドを送信します。

        info:
            このプログラムは Tello-Console の中核となります。全てのドローンへ送信するコマンドはここで処理されます。
            このメソッドを使って直接ドローンにコマンドを送信することも可能です。

        Args:
            cmd (str): ドローンに送信するコマンドを入力します
            start (_type_, optional): ドローン診断用引数です。使用しないでください.

        Returns:
            str: ドローンからの応答
        """
        try:
            self.socket.sendto(cmd.encode('utf-8'), self.tello_address) # ここでs代入されたコマンドをドローンに送信する

            # Return send cmd
            if self.recv_output_frag is False or setup==True:
                pass
            else:
                if self.lang == 'jp':
                    print('\x1b[37m'+'コマンド<%s>を送信しました…'%(cmd)+'\x1b[0m')
                else:
                    print('send command <%s>...'%(cmd))

            # 応答が来るまで待つ、しかし5秒経過したらタイムアウトする
            if None_response_cmd == True:
                pass
            else:
                timer = threading.Timer(self.MAX_WAIT_TIME, self.set_timeout_frag) 
                timer.start()
                while self.response is None:
                    if self.timeout_frag is True:
                        if self.lang == "jp":
                            print('タイムアウト!')
                        else:
                            print('timeout!')
                        break
                timer.cancel() # タイマーを停止させる

                self.timeout_frag = False
            
            # 応答を確認する
            if self.response is None:
                response = "None response"
            else:
                response = self.response.decode('utf-8')

            if self.recv_output_frag is False or None_response_cmd == True or setup==True:
                pass
            else:
                if self.lang == 'jp':
                    print('\x1b[37m'+'ドローンから応答<%s>を受信しました…'%(response)+'\x1b[0m') # どんなコマンドを送信したかをターミナルに反映        
                else:
                    print('\x1b[37m'+'recv <%s> by drone ...'%(response)+'\x1b[0m') # どんなコマンドを送信したかをターミナルに反映        
                
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
                    sys.exit()
            
            # status 判定
            if cmd == 'takeoff' and response != 'error':
                self.drone_state = 'flight'
            elif cmd == 'land' and response != 'error':
                self.drone_state = 'land'

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
                    print('\x1b[33m'+"FLIGHT CMD ERROR RETRY SEND IT. WAIT 1 sec")
                
                time.sleep(1)
                self.send_cmd(cmd)

            elif response == "error Auto land":
                self.battery_level = self.get_battery()
                if self.battery_level < 12:
                    if self.lang == "jp":
                        print('\x1b[31m'+"バッテリー残量が残りわずかです！自動着陸します。"+'\x1b[0m') # バッテリー残量が 10 % 以下になったら自動着陸してしまう。（仕様）
                    else:
                        print('\x1b[31m'+"CURITICAL LOW BATTERY ! LANDIG! LANDING!"+'\x1b[0m')
                    sys.exit()
                else:
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
        
        except OSError:
            if self.lang == "jp":
                print('\x1b[33m'+"接続エラー。ドローンとの接続に問題が発生しました。"+'\x1b[0m') 
            else:
                print('\x1b[33m'+"CONNECTION ERROR"+'\x1b[0m')
            import traceback
            traceback.print_exc()
            sys.exit()

        except Exception:
            import traceback
            traceback.print_exc()
            sys.exit()

    def _recv_thread(self):
        """ドローンからの応答を監視するメソッドです。
        
        警告:
            threading によって稼働します。通常のメソッドとして使用することは前提としていません。
        """
        while True:
            try:
                if self.killer_frag is True:
                    break
                self.response, ip = self.socket.recvfrom(3000) # ここで応答を受け取る
            
            except (KeyboardInterrupt, Exception):
                break

    def _recv_video_thread(self):
        """ドローンからのビデオ通信を監視するメソッドです。
        
        警告:
            threading によって稼働します。通常のメソッドとして使用することは前提としていません。
        """
        if self.cap is None: # cap に何もない場合はドローンからのカメラデータを格納させる
            self.cap = cv2.VideoCapture(self.tello_video_address)
        if not self.cap.isOpened(): # cap データが解放されていない場合は解放する
            self.cap.open(self.tello_video_address)
        
        time.sleep(0.5)
        while self.allow_loop == True :
            if self.killer_frag is True:
                print('Break')
                break
            try:
                self.ret, frame = self.cap.read() # cap から取り込まれたデータを frame に格納する

                # VPS カメラを取得したら画像を90度反転させる
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
                sys.exit()

    def _timeout_thread(self):
        """通信がタイムアウトするかどうかを監視するメソッドです。
        
        警告:
            threading によって稼働します。通常のメソッドとして使用することは前提としていません。
        """
        pre_battery_level = 0
        while True:
            if self.killer_frag is True:
                print('Break')
                break
            try:
                self.current_time = time.time()

                if self.current_time - self.pre_time > 10:

                    self.battery_level = self.get_battery(stmcall=True)
                    if self.battery_level is None:
                        pass
                    else:
                        if self.battery_level != pre_battery_level:
                            if self.lang == "jp":
                                print('\x1b[37m'+'現在のバッテリー残量：%d'%(self.battery_level)+'\x1b[0m')
                            else:
                                print('\x1b[37m'+'Current battery : %d'%(self.battery_level)+'\x1b[0m')
                    self.pre_time = self.current_time
                    pre_battery_level = self.battery_level
            except KeyboardInterrupt:
                break
            
            except Exception:
                import traceback
                traceback.print_exc()
                sys.exit()
    
    def result_deliver(self, msg):
        return msg
    
    def set_timeout_frag(self):
        """ドローンからの通信が10秒以上なかった場合 frag を立てます。

        警告:
            このプログラムはドローンを診断する専用のメソッドです。通常のメソッドとして使用することは前提とされていません。

        """
        try:
            self.timeout_frag = True
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def thread_closer(self):
        """各スレッドを終了させるメソッド
        """
        print('タスクの終了を試みます')
        self.killer_frag = True
        #self.recv_thread.join()
        #self.recv_video_thread.join()
        #self.timeout_thread.join()
        print('停止')

# ドローン操作メソッド群
    def takeoff(self):
        """ドローンを離陸させます。

        Returns:
            str: 実行結果
        """
        try:
            return  self.send_cmd('takeoff')
        except:
            import traceback
            traceback.print_exc()
            sys.exit()


    def land(self):
        """ドローンを着陸させます。

        Returns:
            str: 実行結果
        """
        try:
            return self.send_cmd('land')
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def throwfly(self):
        """throwfly モードを有効にします。

        throwfly モードとは:
            throwfly モードは、ドローンを軽く投げて飛行させるモードです。使用する際は回転するプロペラに気をつけてください。

        Returns:
            str: 実行結果
        """
        try:        
            response = self.send_cmd('throwfly')
            return response
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
        

    def motor_start(self):
        """ドローンのモーターを起動します。

        Returns:
            str: 実行結果
        """
        try:        
            response = self.send_cmd('motoron')
            return response
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def motor_stop(self):
        """ドローンのモーターを停止します。

        Returns:
            str: 実行結果
        """
        try:        
            response = self.send_cmd('motoroff')
            return response
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def emergency(self):
        """ドローンを緊急停止させ、プログラムを停止します。

        警告:
            このプログラムを実行するとドローンはモーターとプログラムは停止します。飛行中の場合機体が破損する恐れがあります。
            
        Returns:
            str: 実行結果
        """
        try:
            return self.send_cmd('emergency')
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def reboot(self):
        """ドローンを再起動します

        Returns:
            str: 実行結果
        """
        try:
            self.send_cmd('reboot')
            print('\x1b[31m'+"再起動します"+'\x1b[0m')
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def stop(self):
        """ドローンを停止させます。あらゆる移動シークエンスを停止させます。

        info:
            ドローンが飛行中または移動中にこのプログラムを実行すると、ドローンをその場でホバリングさせます。

        Returns:
            str: 実行結果
        """
        try:
            self.send_cmd("rc 0 0 0 0")
            return self.send_cmd('stop')
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def rc(self, elron, elevator, srotol, lador):
        """ドローンにプロポスティック操作を入力します。各スティックの出力値をドローンへと送信し、精密なオペレートを可能にします。

        Args:
            elron (int): 左右移動：（正の値：右移動、負の値：左移動）範囲：-100 ~ 100
            elevator (int): 前後移動：（正の値：前移動、負の値：後移動）範囲：-100 ~ 100
            srotol (int): 上下移動：（正の値：上昇、負の値：下降）範囲：-100 ~ 100
            lador (int): 旋回移動：（正の値：時計回り、負の値：反時計回り）範囲：-100 ~ 100

        Returns:
            str: 実行結果
        """
        try:
            if elron > 100:
                elron = 100
            elif elron < -100:
                elron = -100
            if elevator > 100:
                elevator = 100
            elif elevator < -100:
                elevator = -100
            if srotol > 100:
                srotol = 100
            elif srotol < -100:
                srotol = -100
            if lador > 100:
                lador = 100
            elif lador < -100:
                lador = -100

            return self.send_cmd('rc {} {} {} {}'.format(elron, elevator, srotol, lador), None_response_cmd=True)
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def forward(self,cm):
        """ドローンを任意の距離（cm）前進させます。

        Args:
            cm (int): 前進させる距離 範囲：20 ~ 500
            入力値が 20 以下、または 500 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
            if cm < 20:
                cm = 20
            if cm > 500:
                cm = 500
            return self.send_cmd("forward {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def back(self,cm):
        """ドローンを任意の距離（cm）後進させます。

        Args:
            cm (int): 後進させる距離 範囲：20 ~ 500
            入力値が 20 以下、または 500 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
            if cm < 20:
                cm = 20
            if cm > 500:
                cm = 500
            return self.send_cmd("back {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def right(self,cm):
        """ドローンを任意の距離（cm）右進させます。

        Args:
            cm (int): 右進させる距離 範囲：20 ~ 500
            入力値が 20 以下、または 500 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
            if cm < 20:
                cm = 20
            if cm > 500:
                cm = 500
            return self.send_cmd("right {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def left(self,cm):
        """ドローンを任意の距離（cm）左進させます。

        Args:
            cm (int): 左進させる距離 範囲：20 ~ 500
            入力値が 20 以下、または 500 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
            if cm < 20:
                cm = 20
            if cm > 500:
                cm = 500
            return self.send_cmd("left {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def up(self,cm):
        """ドローンを任意の距離（cm）上昇させます。

        Args:
            cm (int): 上昇させる距離 範囲：20 ~ 500
            入力値が 20 以下、または 500 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
        
            if cm < 20:
                cm = 20
            if cm > 500:
                cm = 500
            return self.send_cmd("up {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def down(self,cm):
        """ドローンを任意の距離（cm）下降させます。

        Args:
            cm (int): 下降させる距離 範囲：20 ~ 500
            入力値が 20 以下、または 500 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
            if cm < 20:
                cm = 20
            if cm > 500:
                cm = 500
            return self.send_cmd("down {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def cw(self,dig):
        """ドローンを任意の角度（度）時計回り（右旋回）させます。

        Args:
            dig (int): 旋回させる距離 範囲：1 ~ 360
            入力値が 1 以下、または 360 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
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
        """ドローンを任意の角度（度）反時計回り（左旋回）させます。

        Args:
            dig (int): 旋回させる距離 範囲：1 ~ 360
            入力値が 1 以下、または 360 以上である場合、自動的に補完されます。

        Returns:
            str: 実行結果
        """
        try:
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
        """ドローンを任意の4方向にフリップ（宙返り）させます。

        caution:
            このコマンドはドローンのバッテリー残量が 50% 以上の場合のみ使用できます。

        Args:
            dir (str): f = 前方へフリップ/ b = 後方へフリップ/ r = 右方向へフリップ/ l = 左方向へフリップ

        Returns:
            str: 実行結果
        """
        try:
            return self.send_cmd("flip {}".format(dir))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def go(self, x,y,z,speed):
        """ドローンを任意の方向へ任意の速度で移動させます。旋回はできません。

        Args:
            x (int): 前後移動する距離（cm）を設定します。負の値を入力すると後方へ移動します。範囲：-500 ~ 500（-20 ~ 20 の範囲は入力できません）
            y (int): 上下移動する距離（cm）を設定します。負の値を入力すると下降します。範囲：-500 ~ 500（-20 ~ 20 の範囲は入力できません）
            z (int): 左右移動する距離（cm）を設定します。負の値を入力すると右移動します。範囲：-500 ~ 500（-20 ~ 20 の範囲は入力できません）
            s (int): このコマンドによって移動する機体の速度（cm/s）を設定します。範囲：0 ~ 100

        Returns:
            str: 実行結果
        """
        try:        
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
            
            response = self.send_cmd("go %d %d %d %d"%(x,y,z,speed))
            return response
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def curve(self, x1, y1, z1, x2, y2, z2, speed):
        """始点から終点までの位置を基に機体がカーブを描きます。

        Args:
            x1 (int): _description_
            y1 (int): _description_
            z1 (int): _description_
            s2 (int): _description_
            y2 (int): _description_
            z2 (int): _description_
            speed (int): _description_
        """
        try:
            response = self.send_cmd("curve %d %d %d %d %d %d %d"%(x1,y1,z1,x2,y2,z2,speed))
            return response
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

# ドローンの設定を変更するメソッド群
    def wait(self, sec):
        """任意の時間（秒）ドローンを待機させます。飛行中の場合任意の時間（秒）ホバリングします。

        Args:
            sec (int/float): 待機時間（秒）

        Returns:
            なし
        """
        try:
            res = "Drone is wait: %d sec"%(sec)
            time.sleep(sec)
            print(res)
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def speed(self,cm):
        """ドローンの飛行速度を設定します。移動コマンド実行前にこのプログラムを記述することでドローンの飛行速度を変更できます。

        Args:
            cm (int): ドローンの飛行速度（cm/s）を設定します。

        Returns:
            str: 実行結果
        """
        try:
            if cm < 10:
                cm = 10
            if cm > 100:
                cm = 100
            return self.send_cmd("speed {}".format(cm))
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def missionpad_detection(self, switch):
        try:
            if switch == 1:
                cmd = "mon"
            elif switch == 0:
                cmd = "moff"
            return self.send_cmd(cmd)
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def set_fps(self, fps):
        """ドローンからのカメラビューの fps を設定します。

        tips:
            処理を軽減したい場合は、low に設定するといいでしょう。

        Args:
            fps (str): low、middle、high の3つのみ取得します。
            low: 5fps、middle: 15fps、high:30fps

        Returns:
            str: 実行結果
        """
        try:
            if fps == "high" or fps == "middle" or fps == "low":
                return self.send_cmd("setfps "+fps)
            else:
                pass
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def set_bitrate(self, bitratelevel):
        """ドローンからのカメラビューのビットレートを設定します。

        Args:
            bitratelevel (int): 0 から 5 までの値を取ります。それ以外の範囲の値は入力しないでください。
            0: 自動
            1: 1Mbps
            2: 2Mbps
            ...

        Returns:
            str: 実行結果
        """
        try:
            if bitratelevel == 0:
                bitratelevel = "auto"
            else:
                bitratelevel = str(bitratelevel) + "Mbps"
            return self.send_cmd("setfps "+bitratelevel)
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def set_resolution(self, resolusion):
        """カメラビューの 画質 を取得します。

        tips:
            処理を軽減したい場合は、low に設定するといいでしょう。

        Args:
            fps (str): low、middle、high の3つのみ取得します。
            low: 480p、high:720p

        Returns:
            str: 実行結果
        """
        try:
            if resolusion == "high" or resolusion == "low":
                return self.send_cmd("setresolution "+resolusion)
            else:
                pass
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def set_wifi(self, ssid, password):
        try:
            if ssid is None or password is None:
                print('コマンドエラー。引数が足りません。このこのコマンドはスキップします。')
            else:
                response = self.send_cmd('wifi %s %s'%(ssid, password))
                sys.exit()
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def downvision(self, angle):
        """カメラを切り替えます。（下方カメラへのアクセスを有効にします）

        Args:
            angle (int): 0 と 1 のみ受け付けます。
            0: ドローンの前方時カメラに切り替えます。
            1: ドローンの下方カメラに切り替えます。

        Returns:
            str: 実行結果
        """
        try:
            if angle == 1:
                self.vision_frag = True # カメラ画角を90度反転させるフラグを立てる
            else:
                self.vision_frag = False # カメラ画角を90度反転させるフラグを下げる

            print("Changing ...")
            time.sleep(2)
            return self.send_cmd('downvision {}'.format(angle))

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def stream(self, video=1):
        """ドローンからのカメラデータ取得の有効、向こうの設定を行います。
        
        info:
            このコマンドを使用しなくても、デフォルトでドローンからカメラビューにアクセスできます。

        Args:
            video (int, optional): 0 と 1 のみを取ります。デフォルトの値 =  1.
            0: ドローンからのカメラビュー取得を無効にします。
            1: ドローンからのカメラビュー取得を有効にします。

        Returns:
            str: 実行結果
        """
        try:
            if video == 1:
                response = self.send_cmd('streamon', setup=True)
                ### ビデオデータを取得するスレッドの起動
                # ビデオ受信メソッド _recv_video_thread を並列実行させる
                self.recv_video_thread = threading.Thread(target=self._recv_video_thread)
                self.recv_video_thread.daemon = True
                self.allow_loop = True
                self.recv_video_thread.start()

                print('ビデオデータを取得中…')
                while self.frame is None:
                    continue
                print('ビデオデータを取得しました')

            elif video == 0:
                ### ビデオデータスレッドを停止
                self.allow_loop = False
                self.recv_video_thread.join()
                response = self.send_cmd('streamoff',setup=True)
                print('ビデオデータ通信を終了しました')
            
            return response
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def set_ap(self, ssid, password):
        try:
            if ssid is None or password is None:
                print("SSID、password が見つかりません。このコマンドは実行できません。")
            else:
                response = self.send_cmd("ap %s %s"%(ssid, password))
                print("%s\nドローンをステーションモードに切り替えます。3秒後に再起動します！")
                sys.exit()
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

# ドローンステータス取得メソッド群
    def get_flighttime(self):
        """ドローンの総飛行時間を取得します。

        Returns:
            str: 実行結果
        """
        try:
            response = self.send_cmd('time?')
            if response != "None response":
                if "s" in response and not "None" in response:
                    response = re.sub(r"\D", "", response)
                    self.backup[0] = int(response)
                    return int(response) 
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_flighttime()
                return self.backup[0]

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
 
    def get_tof(self):
        """ドローン下部に搭載された ToF センサーから、対地高度（mm）を取得します。

        Returns:
            int: ドローンから地表間との高度（mm）、最低値：100
        """
        try:
            response = self.send_cmd('tof?')

            if "mm" in response:
                response = re.sub(r"\D", "", response)

                if response != "None":
                    self.backup[1] = int(response)
                else:
                    response = self.backup[1]

                return int(response)
            
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_tof()
                return self.backup[1]
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def get_height(self):
        """IMU からドローンが離陸した地点からの相対高度（cm）を取得します。

        get_tof コマンドとの違い:
                get_tof コマンド：地表からドローンの高度を mm で取得
                get_height（このコマンド）: 離陸地点を基準にしてドローンの高度を cm で取得

        Returns:
            int: 相対高度 cm
        """
        try:
            response = self.send_cmd('height?')

            if "dm" in response:
                response = re.sub(r"\D", "", response)
                self.backup[2] = int(response)
                return int(response)
            
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_height()
                return self.backup[2]
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()

    def get_battery(self, stmcall=False):
        """ドローンのバッテリー残量を取得します。

        Returns:
            int: バッテリー残量（%）
        """
        try:
            response = self.send_cmd('battery?', setup=stmcall)
            if response == "None response" or response == "ok" or 'mm' in response or "erorr" in response:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_battery()
                return self.backup[3]
            else:
                response = re.sub(r"\D", "", response)
                self.backup[3] = int(response)
                return int(response)
        
        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def get_speed(self):
        """speed コマンドによって設定された値を返します。

        Returns:
            int: 設定された速度 10 ~ 100
        """
        try:
            response = self.send_cmd('speed?')
            if response is None:
                return self.backup[4]
            response = self.backup[4]
            return float(response)

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
    
    def get_imu(self):
        """ドローンの姿勢角を IMU から取得します。

        Returns:
            list: [pitch, roll, yaw]
        """
        try:
            res = self.send_cmd('attitude?')

            if 'pitch' in res:
                res = re.findall(r"\d+", res)
                response = [int(s) for s in res]
                self.backup[5] = response
                return response
            
            else:
                if self.lang == "jp":
                    print("応答に問題がありました。再度試行します。")
                else:
                    print("RESPONSE ERROR SEND AGAIN")
                self.get_imu()
                return self.backup[5]

        except:
            import traceback
            traceback.print_exc()
            sys.exit()
