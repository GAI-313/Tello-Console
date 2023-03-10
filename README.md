# Tello-Console 7.0.0
# 現在工事中！！！
不定期に更新します。ご了承ください。<br>

　このライブラリは 
[TelloSDK](https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf) 
をもとに初心者でもわかりやすく Tello ドローンを使ったプログラムを作成、実行できるラッパークラス **tello.py** を提供します。

# 目次

 - **[紹介](#intro)**<br>　Tello-Console に関する簡単な説明と紹介をまとめています。
 - **[Tello-Console をインストールする方法](#install)**<br>　Tello-Console をインストールする方法を解説します。
   - **[Tello-Console を実行してみる](#taskdo)**<br>　Tello-Console を実行する方法を解説します、これを読む前に**Tello-Console をインストールしている必要があります。**
   - **[Tello-Console がどのディレクトリでも実行できるようにする](#directory_setting)**<br>　Tello-Console をどのディレクトリからでも実行できるようにします。
 - **[アップデート](#update)**<br>　Tello-Console をアップデートする方法を解説します
 - **[エデュケーション](#educatoin)**<br>　Pythonの でプログラミングをする方法や、Tello-Console の簡易的な使用方法をまとめています。
   - **[Tello-Console を使う方法（経験者向けの内容です）](#howto)**<br>　Tello-Console を今すぐ扱いたい方はこちらを参考にしてください。
   - **[スタディサポート](#study_support)**<br>　Tello-Console を使うまえに１から Python を勉強してみたい方はこちらを参照してください。Tello-Console をつかってドローンをプログラミングするまでの道のりを記述しています。
- **[メソッド（Tello-Console コマンド一覧）](#commandlist)**<br>　Tello-Console に用意されているメソッド（コマンド）の一覧です。
- **[リリースノート](#releasenote)**<br>　tello-Console のアップデート情報をまとめています。こちらからアップデートされた Tello-Console の追加機能、変更内容などの更新状況を確認できます。

<a id="intro"></a>
# 紹介

　Tello-Console は DJI Ryze Tech Tello-EDU 向けの Python プログラムツールです。このライブラリを実装することで、ドローン操作メソッド（ドローンを操作するためのプログラム関数）をコマンド感覚で使用でき、Python をこれから始める人でもすぐにドローンを使ったプログラムの実装が可能になります。ベースとした SDK は 
[TelloSDK](https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf)
 で、これらに追加機能を多く搭載し最適化したのがこの Tello-Console です。
<br>

**主な特徴**

- **わかりやすいステータス表示**<br>　ドローンに対してどんなコマンドを送信したか、ドローンからどのような応答が来たのか、どのようなエラーが発生したのか、そのエラーの解決方法はあるのか、、などの状況を表示してくれるので、自己解決が容易にできます。また、Tello-Console と Tello 間の通信状況の表示を無効にすることもできます。
- **自動着陸問題を回避できる**<br>　Tello は SDK モード（プログラムによってドローンを操作できるモード）の時、15秒間何もコマンドが送信されないと自動で着陸します。この問題は本ライブラリではデフォルトで無効になっているため、ドローンを継続して飛行させることができることで柔軟なプログラムを構築できます。
- **カメラへのアクセスが容易**<br>　Tello のカメラへアクセスするには、OpenCV を使用して、frame 変数を取得するだけで使用できます。また、
[TelloSDK 3.0](https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf) 
によって Tello の前方カメラのみでなく、機体下部のビジョンカメラへのアクセスも可能です。
- **豊富なコマンド**<br>　TelloSDK3.0 をサポートしているため、豊富なコマンドをサポートしているため、柔軟なタスクを組むことができます。
- **アップデートして新機能を使う**<br>　Tello-Console は不規則ながら日々アップデートを重ねます。アップデートをするたびに新たなチュートリアル、機能、修正を施します。アップデートされたライブラリは細かい変更設定をしなくてもそのまま使用することができます。
- **チュートリアルによるコーディングサポート**<br>　Tello-Console をすぐに、楽しく使用できるために、チュートリアルを日々作成中です。初心者でもわかりやすい記事を目指しで現在製作中なので、乞うご期待。

<a id="install"></a>
# インストール

　Tello-Console を導入するには、いくつか手順が必要です。Tello-Console の導入方法は OS によって異なります。OS ごとにインストール方法を紹介します。

> **インストール作業を行う前に（初心者の方は必ずお読みください）**<br>
> 作業方法をよく読み作業に当たってください。作業を飛ばしてしまうと正常にインストールできない場合があります。

　以下の記事から各 OS ごとのインストールガイドまでジャンプできます。

- **[Windows に Tello-Console を導入する方法](#install_windows)**
- **[macOS に Tello-Console を導入する方法](#install_mac)**
- **[Ubuntu（Linux） に Tello-Console を導入する方法](#install_ubuntu)**

<a id="install_windows"></a>
## Windows に Tello-Console を導入する方法

　ここでは、**Windows に Tello-Console をインストールする方法** を解説します。紹介する導入方法は Windows 10 で検証した方法となります。Windows 11、や、Widnows 10 以前のバージョンのものでは若干操作方法が異なる場合があります。

> 現在 WIndows では Tello からのカメラビューアクセスに遅延が発生する問題を抱えています。現在調査中ですが、可能であれば Linux での運用を強くお勧めします。

1. **コマンドプロンプトを開く**
  <br>

  　検索バーに **cmd** と入力して、**コマンドプロンプト** を開きます。

  > コマンドプロンプトについて詳しく知りたい場合は、**[コマンドプロンプト　コマンドガイド]()** を参照してください。

  <center>
  <img src='https://i.imgur.com/s8JJNEA.png' height=400>
  </center>

2. **python コマンドを入力する**
  <br>

  　黒いウィンドウが表示されたら、そこに **python** と入力してください。
  <center>
  <img src='https://i.imgur.com/naM8CLc.jpg' height=400>
  </center>

  　入力したら、エンターキーを押して入力されたコマンドを実行します。
  <center>
  <img src='https://i.imgur.com/NieH4D8.jpg' height=200>
  </center>
  <br>

  実行して、**MicroSoft Store** が開いたら、**手順3** から順番に作業を進めてください。microsoft store アプリが開かずにコマンドプロンプトの表示が変わったら **手順4** から作業を進めてください。あなたの環境にはすでに python がインストールされています。

3. **python をインストールする**
  <br>

  　**MicroSoft Store** が開いたら、**インストール** をクリックして、表示されている **python** をインストールします。
  <center>
  <img src='https://i.imgur.com/NF2hJqH.jpg' height=400>
  </center>
  <br>

  **インストールボタン** が、**スタートピンに固定** に表示が変わったらインストールは完了です。コマンドプロンプトに戻り、もう一度 **python** コマンドを実行してください。

4. **確認**
  <br>

  　python を実行すると、以下のように表示が切り替わります。このように末尾が ```>``` から ```>>>``` に変わったら **無事 Python のインストールは成功です！**

  <center>
  <img src='https://i.imgur.com/bXEUUGR.jpg'>
  </center>
  <br>

  ```quit()``` を実行して Python 実行モードを終了します。

  <center>
  <img src='https://i.imgur.com/mDn1daw.jpg'>
  </center>
  <br>

5. **必要なパッケージをインストールする**
  <br>

  　以下のコマンドを **1行づつコピペして** 実行します。
  ```bash
  pip3 install opencv-python
  pip3 install pytk
  ```

6. Tello-Console をインストールするには、**git**  をインストールする必要があります。
  <br>

  　以下のリンクから、**Git for Windows** をダウンロードします。以下のサイトにある **Download** をクリックします。

  - https://gitforwindows.org

  <br>
  <center>
  <img src='https://i.imgur.com/NEutaG8.jpg' height=400>
  </center>
  <br>

  　ダウンロードフォルダにダウンロードされたインストーラがあります。これを実行します。

  <br>
  <center>
  <img src='https://i.imgur.com/vBbu7VT.jpg' height=400>
  </center>
  <br>

  　インストールウィザードの **"Next"** を、インストール進捗バーが表示されるまでひたすらクリックしてください。

  <br>
  <center>
  <img src='https://i.imgur.com/qWd7LG6.jpg' height=400>
  </center>
  <br>

  　インストール進捗バーが表示されて、これが消えたら、下のようなウィンドウが表示されます。このウィンドウにある **"Launch Git Bash"** にチェックを入れてください。

  <br>
  <center>
  <img src='https://i.imgur.com/MKm5S1q.jpg' height=400>
  </center>
  <br>

  もう一つ黒い **コマンドプロンプトみたいなウィンドウ** が表示されたら完了です。

7. **Tello-COnsole をダウンロードする**
  <br>

  　コマンドプロンプトに戻り、以下のコマンドを **1行づつコピペして** 実行します。
  ```Bash
  cd %homepath%
  git clone https://github.com/GAI-313/Tello-Console.git
  ```

  > **コマンドプロンプトで git コマンドが認識されない場合**<br>

   上記の git コマンドを実行したとき、以下のようなエラーが表示された場合、**以下の手順** に沿って Tello-Console をインストールしてください。
    　
   <center>
   <img src='https://i.imgur.com/PEJ8Xjh.jpg'>
   </center>
   <br>

   1. **Git for Bash を開く**<br>

     git for bash とは、先ほど説明した **コマンドプロンプトみたいなウィンドウ** のことです。
     <center>
     <img src='https://i.imgur.com/IobUWSP.jpg' height=300>     
     </center>
     <br>

 　もし、上記のウィンドウが表示されていない場合は、**検索バー** で **"git"** と入力して候補に出てきた **"Git Bash"** を実行してください。<br>  
      　
   2. **コマンドを実行**<br>

   以下のコマンドを **１行ずつコピペ実行してください。** Git Bash は、**ショートカットキー Control + V** が利用できません。右クリックして **Paste** をクリックしてください。
   <center>
   <img src='https://i.imgur.com/UgwW41M.jpg' height=300>
   </center>
   <br>
   ```
   cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
   ```

これで **WindowsにTello-Console のインストールする作業は完了です！！**

> **ヒント**
  <br>
  　Tello-Console ディレクトリをエクスプローラ上でクイックアクセスに登録しておくことで、素早くアクセスすることができるようになります。

  <br>

**[Tello-Console を実行してみる](#taskdo)**

<a id="install_mac"></a>
## macOS に Tello-Console を導入する方法

　macOS に Tello-Console をインストールする方法を解説します。紹介する導入方法は、**macOS Monterey（12.0）** で検証した導入方法となります。それ以前、以降の macOS では、若干操作方法が異なる場合があります。

1. Command キーとSpace キーを押して SpotLight 検索を開きます。
2. Spotlight 検索欄内に **"ターミナル"** と入力します。
3. 候補として出てきた **"ターミナル.app"** を起動します。

> **ターミナルの外観設定をしていない方へ**<br>

　**[ターミナルの外観を最適化する](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/for_mac/terminal_setting_tutorial.md#ターミナルの外観を最適化する)** を参照し、ターミナルの外観を設定してください。Tello-Console の実行に支障が出ます。

4. 以下のコマンドを**コピペ**してコマンドを実行してください。コマンドの実行は **エンターキー**を押すだけです。
  ```bash
  python -V
  ```
  　すると、**Mac に標準インストールされている Python のバージョンが返されます**。
  <br>

  　この時、Python のバージョンが 3.x.x であれば 
  　**[手順 8](#mac=8)
  　 までスキップしてください。** （手順5, 手順6 も実行しても構いません。）
  <br>

  　Python のバージョンが **2.x.x** の場合、以下の **[手順5](#mac_5)** から順番に行ってください。<br>

<a id="mac_5"></a>
5. **この作業は Python のバージョンが 3.x.x の方でも実行して構いません**<br>　ターミナル上に、以下のコマンドを実行してください。
  ```bash
  gcc
  ```
  　そしたら、**"コマンドライン・デペロッッパツール のインストールを実行するか"** を要求されるので、**インストールをクリックしてインストールを実行してください。**

  <center>
  <img src='https://i.imgur.com/91TaW55.png' height=300>

  **インストールをクリック**

  <img src='https://i.imgur.com/Nxt6LLN.png' height=300>

  **同意をクリック**

  <img src='https://i.imgur.com/IadpJgt.png' height=300>

  **お使いの Mac が電源と接続されていない場合、このような警告が出ます。環境によって時間がかかるため電源に接続した状態で実行することをおすすめします。**
  </center>

6.  **この作業は Python のバージョンが 3.x.x の方でも実行して構いません**<br>　以下のコマンドを**コピペして実行**してください。
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  ```

  <center>
  <img src='https://i.imgur.com/aUccos8.png' height=300>
  </center>

  **途中パスワードの入力が求められます。パソコンにログインする際のパスワードを入力してください**<br>

  <center>
  <img src='https://i.imgur.com/LGgZf84.png' height=500>
  </center>

  　コマンドが実行されると、途中ターミナルに **Press RETURN to continue or any other key to abort** という表示が出てきます。そしたら **エンターキーを押してください**。

7. **この作業は Python のバージョンが 3.x.x の方は実行しないでください**<br>　以下のコマンドを**コピペして実行**してください。すると **Python 3.8.x がインストールされます。**
  ```bash
  brew install python@3.8
  ```
  そしたら次に以下のコマンドを実行してください。
  ```bash
  ln -s /usr/local/opt/python@3.8/bin/python3.8 /usr/local/bin/python3.8
  ```
  これで **Python 3.x.x のインストールは完了** です。

<a id="mac_8"></a>
8. ターミナルに、以下のコマンドを **1行づつコピペして** コマンドを実行します。
  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  pip3 install opencv-python
  pip3 install pytk
  cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
  ```

　これで **macOS に Tello-Console** の導入は完了です。<br>

　Tello-Console を使用してプログラムを作成するには、VScode がお勧めです。こちらで VScode のインストール方法を案内しています。

　- [macOS に VScode をインストールする方法](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#mac-に-vscode-をインストールする方法)

**[Tello-Console を実行してみる](#taskdo)** に移動する。

<a id="install_ubuntu"></a>
## Ubuntu（Linux） に Tello-Console を導入する方法
　Ubuntu に Tello-Console をインストールする方法を解説します。紹介する導入方法は、**Ubuntu 20.04 LTS** で検証した導入方法となります。それ以前、以降の Ubuntu では、若干操作方法が異なる場合があります。

1. Control キーと ALT キーと T キーを押して **端末（ここではターミナルと呼ぶことにする）** を開きます。
2. ターミナルに、以下のコマンドを **1行づつコピペして** コマンドを実行します。コマンドの実行は **エンターキー**を押すだけです**。実行すると、**はじめにパスワードの入力が求められます。** ログイン時のパスワードを入力してエンターキーを押してください。

  ```bash
  sudo apt update
  suto apt install -y python3-pip3 git
  pip3 install opencv-python3
  pip3 install pytk
  cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
  ```

　これで **Ubuntu に Tello-Console** の導入は完了です。

**これで Tello-Console** のインストールは完了です。本クラスを簡単に使用できるよう、使用するエディタは **VScode** を推奨しております。
**[こちら](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#visual-studio-インストールガイド)** 
のセクションで VScode のダウンロードガイドを案内しております。

<a id="taskdo"></a>
## Tello-Console を実行してみる
　インストール作業が無事終了すると、**モームディレクトリ（ユーザーネームの名前のフォルダ）** に Tello-COnsole **ディレクトリ（フォルダのこと）** がダウンロードされています。**Tello-Console ディレクトリに移動して、sample_boot.py サンプルプログラムを実行して正常に Tello-Console が実行されるか試してみましょう**。
<br>

　以下の操作は **Windows、macOS、Ubuntu 共に同じだ行です。**

1. **Tello-Console ディレクトリに移動する**<br>　以下のコマンドをコピペして、Tello-Console ディレクトリに移動します。
```bash
cd Tello-Console
```

2. **sample_boot.py を実行する**<br>　以下のコマンドをコピペして、sample_boot.py というサンプルプログラムを python で実行します。
```bash
python sample_boot.py
```
　すると、以下のようなテキストが表示されたら **無事 Tello-Console が実行されたことを表しています。**

>**SyntaxError が出た場合**<br>　Python3 をインストールした方は、実行コマンド ```python``` を、```python3``` で実行してください。
  ```bash
  python3 sample_boot.py
  ```

```bash
WELCOME CONSOLE ! TELLO-CONSOLE V7.0.0
コマンド<command>を送信しました…
タイムアウト!
ドローンから応答<None response>を受信しました…
エラー！ドローンとの通信に失敗しました！
Tips:ドローンとPCとのWi-Fi接続を確認してください！
```

#### Windows：コマンドプロンプトでテキストがカラー表示されない問題

　上記のサンプルコードを実行すると、macOS、Ubuntu などでは、以下のように **テキストカラーが反映された状態** で表示されます。
<br>

　Windowsでは、以下のように、色で強調表示されず、文字列末尾に謎のテキストが添付された状態で生じされてしまいます。
<br>
<img src='https://i.imgur.com/xnWk96M.jpg'>
<br>

この問題を解決するには、
<br>

**[コマンドプロンプトで Tello-Console のシンタックスハイライトを有効にする](https://github.com/GAI-313/Tello-Console/blob/windows/tutorial/windows/cmd_tutorial.md#%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88%E3%81%A7-tello-console-%E3%81%AE%E3%82%B7%E3%83%B3%E3%82%BF%E3%83%83%E3%82%AF%E3%82%B9%E3%83%8F%E3%82%A4%E3%83%A9%E3%82%A4%E3%83%88%E3%82%92%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B)**
<br>

を参照してください。
  
<a id="directory_setting"></a>
## Tello-Console がどのディレクトリでも実行できるようにする
　Tello-Cnsole は、
**Tello-Console ディレクトリにある modules ディレクトリ内にある tello.py**
が本体です。このプログラムを呼び出すことで Tello-Console を利用できるようになるのですが、今のままだと **Tello-Console ディレクトリ内にある python 実行ファイル（拡張子が .py のやつ）しか tello.py を読み込むことができません。**
<br>

　好きなディレクトリから Tello-Console を実行できるように、一手間加えてみましょう。この操作は
**Windows と macOS、Ubuntu で操作方法が異なります。**
<br>
<br>

>**警告：**<br>
>　**この作業は難易度が少々高いです。以下の解説が理解できない場合はお勧めしません。作業に失敗すると少々面倒な>ことになります。**

以下のも記事から各 OS ごとのガイドまでジャンプできます。

- **[WIndows でTello-Console がどのディレクトリでも実行できるようにする](#path_windows)**
- **[macOS、Ubuntu でTello-Console がどのディレクトリでも実行できるようにする](#path_)**

<a id="path_windows"></a>
### WIndows でTello-Console がどのディレクトリでも実行できるようにする

1. 検索バーに **"環境変数"** と入力します。　
2. 検索結果脳候補に **"コントロールパネルのシステム環境変数を編集"** が表示されます。これを実行します。
3. **"環境変数(N)"** をクリックします
  <br>
  <img src='https://i.imgur.com/s2XZogN.jpg'>
  <br>

4. **"ユーザー環境変数(U)"** の **新規(N)** をクリックします。
  <br>
  <img src='https://i.imgur.com/DSPpN9i.jpg'>
  <br>

5. 新しいユーザー変数で、**変数名を "PYTHONPATH"** にします。
  <br>
  <img src='https://i.imgur.com/FkYLIrS.jpg'>
  <br>

6. **ディレクトリの参照** をクリックします。
7. **ユーザー名** フォルダをクリックして、その中にある **Tello-Console** から、**modules** ディレクトリを指定します。フォルダー(F)が、**"modules"** になっていることを確認してください。確認したら **"OK"** をクリックします。
<br>
<img src='https://i.imgur.com/YHCgMTl.jpg'>
<img src='https://i.imgur.com/GUbEWac.jpg'>
<br>

8. 以下のようになっていることを確認して 
**"OK"** をクリックします。
  <br>
  <img src='https://i.imgur.com/4Q45Fpt.jpg'>
  <br>

  > モザイクの部分はあなたのユーザー名です。
9. システムのプロパティに戻ったら **"OK"** をクリックします。

これで設定は完了です。

> **注意！**
  <br>

  　お使いの環境によって、以上の設定をしても **PYTHONPATH が反映されない問題が生じています。** 現在調査中です。

---
現在作成中

<a id="path_"></a>
### macOS、Ubuntu でTello-Console がどのディレクトリでも実行できるようにする
　macOS と、Ubuntu では、この操作は同じです。

1. **Tello-Console の絶対パスを取得する**<br>　以下のコマンドを順番に実行してください。
  ```bash
  cd ~/Tello-COnsole/modules/
  pwd
  ```
  　すると、以下のように **ルートディレクトリから Tello-Console の modules ディレクトリまでの絶対パス**が返されます。以下がその例です。
  ```bash
  $ pwd
  /Users/USERNAME/Tello-console/modules
  ```
  　**USERNAME** はお使いの PC にログインしているユーザーの名前が入ります。**この返された1行をコピペしてください。**

2. **PYTHONPATH 環境変数に modules ディレクトリを追加する**<br>　まず、以下のコマンドをコピペしてください。**まだエンターキーを押して実行しないでください！**
  ```bash
  export PYTHONPATH="
  ```
  　次に、**先ほどコピーした modules ディレクトリまでの絶対パスを貼り付けます。**

  > 下のコマンドは例です。これをこのままコピペしないでください。

  ```bash
  export PYTHONPATH="/Users/USERNAME/Tello-console/modules
  ```
  　貼り付けたら、最後に **" （ダブルクォーテーション）** を入力して、以下のような状態になったら
  **エンターキーを押して実行してください**

  > 下のコマンドは例です。これをこのままコピペしないでください。

  ```bash
  export PYTHONPATH="/Users/USERNAME/Tello-console/modules"
  ```

　これで Tello-Console がどのディレクトリからでもアクセスできるようになりました。確認として、以下のコマンドを実行して、**Tello-Console のパスが表示されているかどうか確認しましょう**。
```bash
echo $PYTHONPATH
```
<center>
<img src='https://i.imgur.com/khmsXng.png' height=200>
</center>

　応答に、**Tello-COnsole** が含まれていたら成功です。

<a id="update"></a>
# アップデート
　Tello-Console は不定期にアップデートを行います。[Tello-Console リリースノート](#releasenote) を定期的に参照して、バージョンが変更されていることを確認してください。

## WIndows の場合
1. **git for bash を開く**
2. 以下のコマンドを順番に実行してください。
  ```bash
  cd ~/Tello-Console
  git pull
  ```
## macOS の場合
1. **ターミナルを開く**
2. 以下のコマンドを順番に実行してください。
  ```bash
  cd ~/Tello-Console
  git pull
  ```
## Ubuntu（Linux） の場合
1. **端末（ターミナル）を開く**
2. 以下のコマンドを順番に実行してください。
  ```bash
  cd ~/Tello-Console
  git pull
  ```

<a id="education"></a>
# エデュケーション
　ここでは、Tello-Console の使用方法や、プログラミングをするのにあたり必要なスキルを学べるカリキュラムを用意しています。（現在作成中）

<a id="howto"></a>
## Tello-Console を使う方法（経験者向けの内容です）
　Tello-Console の本体は、```Tello-Console/modukes``` ディレクトリにある **tello.py の中にある console クラス** です。これを呼び出すことで使用することができます。<br>

　**[PYTHONPATH に modules ディレクトリを登録した場合](#directory_setting)**、新規 python ファイルに、以下のような import 文を記述することで、tello.py の中にある **console** を使用できます。
```python3
from modules.tello import console
```
　console クラスを、任意の変数に格納することでインスタンス化（活性化）し、インスたん化された時点で console クラスのドローンへの接続準備およびドローンに対する診断を行います。
```python3
from modules.tello import console

drone = console()
```
　console クラスに用意された各メソッドが **ドローンを操作するためのコマンド** として機能します。例えば、Tello を離陸、着陸させるなら、このように書けば実装できます。
```python3
from modules.tello import console

drone = console() # インスタンス化。ここで 変数 drone が console クラスと同等となる

drone.takeoff() # takeoff メソッドを実行し、ドローンを離陸させる

drone.land() # land メソッドを実行し、ドローンを着陸させる
```
　Tello-Concolse コマンド（メソッド）については、
**[メソッド（Tello-Console コマンド一覧）](#commandlist)**
を参照してください。

<a id="study_support"></a>
## スタディサポート
　Tello-Console は、ドローンを使ってプログラミングの楽しさ、面白さを知ってもらうことを目的に作られました。以下の記事一覧を散走することで、**Python、CUI コマンド、Tello-Console の使用方法、画像処理**に関する知識を習得できます。

- **[Python チュートリアルその1](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/python_tutorial_1.md#python-チュートリアルその1)**

---
現在作成中

<a id="commandlist"></a>
# メソッド（Tello-Console コマンド一覧）

　ここでは、Tello-Console が提供するコマンドを一覧で表示します。コマンド名をクリックすると、該当コマンドの詳細が表示されます。

- **[コントロールコマンド](#cmd_a)**<br>
　ドローンを操作するのに使用するコマンド群です。
- **[設定コマンド](#cmd_b)**<br>
　ドローンの設定を変更するのに使用するコマンド群です。
- **[取得コマンド](#cmd_c)**<br>
　ドローンからの情報を取得するのに使用するコマンド群です。

<a id='cmd_a'></a>
## コントロールコマンド

### 離陸関連コマンド
- **[takeoff コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/takeoff.md)**
- **[motor_start コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/motor_start.md)**

### 着陸、モーター関連コマンド
- **[land コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/land.md)**
- **[motor_stop コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/motor_stop.md)**

### 安全、緊急停止コマンド
- **[emergency コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/emergency.md)**
- **[stop コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/stop.md)**

### 簡易操作コマンド
- **[up コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/up.md)**
- **[down コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/down.md)**
- **[forward コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/forward.md)**
- **[back コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/back.md)**
- **[left コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/left.md)**
- **[right コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/right.md)**
- **[cw コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/cw.md)**
- **[ccw コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/ccw.md)**
- **[flip コマンド](https://github.com/GAI-313/Tello-Console/blob/command/tutorial/command_list/flip.md)**

### 高度操作コマンド
- **[rc コマンド]()**
- **[go コマンド]()**
- **[curve コマンド]()**

<a id='cmd_b'></a>
## 設定コマンド

<a id='cmd_c'></a>
## 取得コマンド
---
現在作成中

<a id="releasenote"></a>
# リリースノート
## Tello-Console Ver.7.0.0
　TelloSDK 3.0 に対応した各コマンドを追加しました。特徴的な真コマンドは以下の通りです。

- **throwfly**<br>　スロウフライモード（機体を投げて離陸させるモード）を有効にします。
- **missionpad_detection**<br>　Tello EDU のミッションパッドの検出を有効にします。
- **set_fps**<br> カメラの fps を変更します

そのほかにも数多くのコマンドを新たに追加しました。TelloSDK 3.0 は、Tello EDU のみ対応しています。一部コマンドは、通常の Tello、Tello アイアンマンエディションでは使用できません。
<br>

**そのほかの変更内容、追加機能**

- **全体のリファクタリング**<br>　tello.py、サンプルコードをみやすくしました。
- **引数サマリーの対応**<br>　VScode で各メソッドにカーソルを当てるとそのメソッドに関する情報を表示されるようにしました。
- **（試験段階）引数 TaskKill を追加**<br>　Tello-Console がエラーによって停止された時、プログラム全体を終了（タスクキル）を行うか否かを選択できる引数を追加しました。これは試験段階です。常用は推奨しません。
- **（試験段階）Docker の対応**<br>　Tello-Console を搭載した Ubuntu コンテナの作成を行う Dockerfile を追加しました。これは試験的なものです。
