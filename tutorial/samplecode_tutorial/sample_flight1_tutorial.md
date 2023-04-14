# sample_flight1.py チュートリアル
　このサンプルコードは、Tello-Console の最も基本である部分を扱うサンプルコードになります。**VScode** を使って sample_flight1.py の中身をみてみましょう。<br>

## 1. CUI を開く。
　CUI について知りたい方は、
**[CUI とは](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/for_mac/terminal_command_guide_1.md)** 
をお読みください。

    - Windows をお使いの方は、**コマンドプロンプト** を開きます。
    - macOS をお使いの方は、**ターミナル** を開きます。
    - Linux(Ubuntu) をお使いの方は、**端末（ターミナル）** を開きます。

## 2.Tello-Console ディレクトリへ移動する
　Windows の方は以下のコマンドを実行してください。
```bash
cd %homepath%\Tello-Console
```
　macOS、Linux(Ubuntu) の方は以下のコマンドを実行してください。
```bash
cd ~/Tello-Console
```

## 3. sample_flight1py を VScode で開く
　以下のコマンドを入力して、sampleboot.py を VScode から開きます。<br>
　VScode をインストールしていない方は、
**[VScode をインストールする](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#visual-studio-code-をインストールする)** 
セクションを参照して VScode をインストールしてください。
```bash
code sample_flight1py
```
これで VScode から sample_flight1py を参照することができます。

## 4. sample_flight1.py をみてみよう
　VScode が開くと、sample_flight1.py を参照することができます。このサンプルコードの全体図は、以下となります。
```python
from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する

drone.takeoff() # takeoff メソッドを呼び出しドローンを離陸させます。

drone.wait(15) # wait メソッドで5秒間ドローンを待機させます。

drone.land() # ドローンは自動着陸します
```
　このサンプルコードでは、ドローンを離陸させ、15秒ホバリングさせたのちに着陸させるプログラムになります。このサンプルコードを流開することで以下のスキルが身についきます。

- Tello-Console を使ってドローンを離着陸させる方法
- Tello-Console を使ってドローンを任意の時間ホバリングさせる方法

## 5. 説明
```python
from modules.tello import console # modules ディレクトリ内の tello.py にある console クラスをインポートする

drone = console() # console クラスを任意の変数に格納して console のインスタンスを生成する
```
