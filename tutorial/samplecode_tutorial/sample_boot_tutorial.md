# sample_boot.py チュートリアル
　このサンプルコードは、Tello-Console の最も基本である部分を扱うサンプルコードになります。**VScode** を使って sample_boot.py の中身をみてみましょう。<br>

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

## 3. sample_boot.py を VScode で開く
　以下のコマンドを入力して、sampleboot.py を VScode から開きます。<br>
　VScode をインストールしていない方は、
**[VScode をインストールする](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#visual-studio-code-をインストールする)** 
セクションを参照して VScode をインストールしてください。
```bash
code sample_boot.py
```
これで VScode から sample_boot.py を参照することができます。

## 4. sample_boot.py を見てみよう
　VScode が開くと、sample_boot.py を参照することができます。このサンプルコードの全体図は、以下となります。
```python
from modules.tello import console

drone = console()
```
　sample_boot.py は、たった2行のスクリプトで構成されているとても単純なサンプルコードです。このサンプルコードを実行することで、Tello-Console のメインプログラムである **tello.py** が起動し、ドローンと PC が正常に接続されているかを確認したのち、ドローンに ```command``` コマンドを送信して、ドローンをプログラミングで操作できるようにするモード、**SDK モード** に切り替えます。PC がドローンと接続されていない場合は、ドローンが接続されていない趣旨を CUI 上に表示します。

## 5. 説明
　このサンプルコードでは、**Tello-Console を Python スクリプト上で使用するための最も基本的なスキル** を学ことができます。このサンプルコードの意味を理解して、Tello-Console の基礎を学びましょう。

### 5.1 インポート
```python
from modules.tello import console
```
　ここでは、```console``` というクラスをインポート（挿入）します。この ```console``` クラスが、Tello-Console のメインプログラムです。
```python
from modules.tello
```
　これの意味は、Tello-Console ディレクトリ内の ```modules``` ディレクトリ内にある ```tello.py``` を参照するという意味です。実際にエクスプローラーや Finder、CUI などを使って modules デゥレクトりを参照してみてください。tello という名前の Python スクリプトがあるのがわかるでしょう。
```python
import console
```
　ここで、先ほどの ```tello.py``` の中にある ```console``` をインポートします。以下のコードは、modules ディレクトリ内にある tello.py の一部を抜粋したものです。
```python
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
```
　上部に ```class console``` と書かれていますよね？このコードでは、この console という名前のついたクラスという大きな関数を呼び出しているのです。クラスについてはインターネットで調べるとたくさん解説があるのでそちらを参照してください。<br>
　このコードを書かなければ、Tello-Console を使用することができません。必ず一番上部に書きましょう。

### 5.2 起動
```python
drone = console()
```
　ここで、インポートされた console クラスを ```drone``` という変数に格納しています。このように **任意の変数に console クラスを格納すると、console 内に記述された起動プログラムが実行されます！```<br>
　また、このように任意の変数にクラスを格納したことで、console 内の機能全てが格納した変数内で動作するため、console クラス内で用意されているドローン操作用のプログラムをコマンド間隔で使用できるようになります。

### 6. おさらい
**sample_boot.py** では、

1. tello.py（メインプログラム）から console クラスをインポートする
2. インポートされた console クラスを任意の変数（drone）に格納して console を起動する

という作業を行なっています。この2行は Tello-Console を使用するときに必ず使用しますので、ぜひこの記述方法と意味を理解してください。
