# Tello-Console 7.0.0
# 現在工事中！！！

　このライブラリは TelloSDK をもとに初心者でもわかりやすく Tello ドローンを使ったプログラムを作成、実行できるラッパークラス **tello.py** を提供します。

# 目次

 - **[紹介](#intro)**<br>　Tello-Console に関する簡単な説明
 - **[tello-Console をインストールする方法](#install)**<br>　Tello-Console をインストールする方法を解説します。
   - **[Tello-Console を実行してみる](#taskdo)**<br>　Tello-Console を実行する方法を解説します、これを読む前に**Tello-Console をインストールしている必要があります**
   - **[Tello-Console がどのディレクトリでも実行できるようにする](#directory_setting)**<br>　Tello-Console をどのディレクトリからでも実行できるようにします
 - **[アップデート](#update)**<br>　Tello-Console をアップデートする方法を解説します
 - **[エデュケーション](#educatoin)**<br>　Python、Tello-COnsole を使った勉強向けの記事や telo-Console の簡易的な使用方法をまとめています
  - **[Tello-Console を使う方法（経験者向けの内容です）](#howto)**<br>　Tello-Console を今すぐ扱いたい方はこちらを参考にしてください。
  - **[スタディサポート](#study_support)**<br>　Tello-Console を使って Python を1から勉強してみたい方はこちらを参照してください。
- **[メソッド（Tello-Console コマンド一覧）](#commandlist)**<br>　Tello-Console に用意されているメソッド（コマンド）の一覧です。
- **[リリースノート](#releasenote)**<br>　tello-COnsole のアップデート情報をまとめています。こちらかたアップデートされた tello-Console の追加機能、変更内容などの更新状況を確認できます。

<a id="intro"></a>
# 紹介

　Tello-Console は DJI Ryze Tech Tello-EDU 向けの Python プログラムツールです。この対ブラリを実装することで、ドローン操作メソッドをコマンド感覚で使用でき、Python をこれから始める人でもすぐにドローンを使ったプログラムの実装が可能になります。ベースとした SDK は TelloSDK で、これらに追加機能を多く搭載し最適化したのがこの Tello-Console です。
<br>
**主な特徴**

- **わかりやすいステータス表示**<br>　ドローンに対してどんなコマンドを送信したか、ドローンからどのような応答が来たのか、どのようなエラーが発生したのか、そのエラーの解決方法はあるのか、、などの状況を表示してくれるので、自己解決が容易にできます。また、Tello-Console と Tello 間の通信状況の表示を無効にすることもできます。
- **自動着陸問題を回避できる**<br>　Tello は SDK モード（プログラムによってドローンを操作できるモード）の時、15秒間何もコマンドが送信されないと自動で着陸します。この問題は本ライブラリで回避でき、ドローンを継続して飛行させることができます。
- **カメラへのアクセスが容易**<br>　Tello のカメラへアクセスするには、OpenCV を使用して、frame 変数を取得するだけで使用できます。また、TelloSDK 3.0 によって Tello の前方カメラのみでなく、機体下部のビジョンカメラへのアクセスも可能です。
- **豊富なコマンド**<br>　TelloSDK3.0 をサポートしているため、豊富なコマンドをサポートしているため、柔軟なタスクを組むことができます。
- **アップデートして新機能を使う**<br>　Tello-Console は不規則ながら日々アップデートを重ねます。アップデートをするたびに新たなチュートリアル、機能、修正を施します。アップデートされたライブラリは細かい変更設定をしなくてもそのまま使用することができます。
- **チュートリアルによるコーディングサポート**<br>　Tello-Console をすぐに、楽しく使用できるために、チュートリアルを日々作成中です。初心者でもわかりやすい記事を目指しで現在製作中なので、乞うご期待。

<a id="install"></a>
# インストール

　Tello-Console を導入するには、いくつか手順が必要です。Tello-Console の導入方法は OS によって異なります。OS ごとにインストール方法を紹介します。

> **インストール作業に当たる前に**<br>
> 作業方法をよく読み作業に当たってください。作業を飛ばしてしまうと正常にインストールできない場合があります。

　以下のも記事から各 OS ごとのインストールガイドまでジャンプできます。

- **[Windows に Tello-Console を導入する方法](#install_windows)**
- **[macOS に Tello-Console を導入する方法](#install_mac)**
- **[Ubuntu（Linux） に Tello-Console を導入する方法](#install_ubuntu)**

<a id="install_windows"></a>
## Windows に Tello-Console を導入する方法

　Windows に Tello-Console をインストールする方法を解説します。紹介する導入方法は Windows 10 で検証した方法となります。Windows 11、や、Widnows 10 以前のバージョンのものでは若干操作方法が異なる場合があります。

---
現在作成中…

<a id="install_mac"></a>
## macOS に Tello-Console を導入する方法

　macOS に Tello-Console をインストールする方法を解説します。紹介する導入方法は、**macOS Monterey（12.6）** で検証した導入方法となります。それ以前、以降の macOS では、若干操作方法が異なる場合があります。

1. Command キーとSpace キーを押して SpotLight 検索を開きます。
2. Spotlight 検索欄内に **"ターミナル"** と入力します。
3. 候補として出てきた **"ターミナル.app"** を起動します。
4. 以下のコマンドを**コピペ**してコマンドを実行してください。コマンドの実行は **エンターキー**を押すだけです。
  ```bash
  python -V
  ```
  　すると、**Mac に標準インストールされている Python のバージョンが返されます**。
  <br>
  　この時、Python のバージョンが 3.x.x であれば 手順8 までスキップしてください。（手順5, 手順6 も実行しても構いません。）
  <br>
  　Python のバージョンが **2.x.x** の場合、以下の **手順7** を行ってください。<br>

  5. **この作業は Python のバージョンが 3.x.x の方でも実行して構いません**<br>　ターミナル上に、以下のコマンドを実行してください。
  ```bash
  gcc
  ```
  　そしたら、**"コマンドライン・デペロッッパツール のインストールを実行するか"** を要求されるので、**インストールをクリックしてインストールを実行してください。**

  6.  **この作業は Python のバージョンが 3.x.x の方でも実行して構いません**<br>　以下のコマンドを**コピペして実行**してください。
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  ```
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


8. ターミナルに、以下のコマンドを **1行づつコピペして** コマンドを実行します。
  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  pip3 install opencv-python
  pip3 install pytk
  cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
  ```

　これで **macOS に Tello-Console** の導入は完了です。

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

<a id="taskdo"></a>
## Tello-Console を実行してみる
　インストール作業が無事終了すると、**モームディレクトリ（ユーザーネームの名前のフォルダ）** に Tello-COnsole **ディレクトリ（フォルダのこと）** がダウンロードされています。**Tello-Console ディレクトリに移動して、sample=boot.py サンプルプログラムを実行して正常に Tello-Console が実行されるか試してみましょう**。
<br>
　以下の操作は **Windows、macOS、Ubuntu 共に同じだ行です。**

1. **Tello-COnsole ディレクトリに移動する**<br>　以下のコマンドをコピペして、Tello-Console ディレクトリに移動します。
```bash
cd Tello-Console
```

2. **sample=boot.py を実行する**<br>　以下のコマンドをコピペして、sample_boot.py というサンプルプログラムを python で実行します。
```bash
python sample_boot.py
```
　すると、以下のようなテキストが表示されたら **無事 Tello-Console が実行されたことを表しています。**
```bash
WELCOME CONSOLE ! TELLO-CONSOLE V7.0.0
コマンド<command>を送信しました…
タイムアウト!
ドローンから応答<None response>を受信しました…
エラー！ドローンとの通信に失敗しました！
Tips:ドローンとPCとのWi-Fi接続を確認してください！
```
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
　応答に、**Tello-COnsole** が含まれていたら成功です。

<a id="update"></a>
# アップデート
---
現在作成中

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

- **[Python チュートリアルその1]()**

---
現在作成中

<a id="commandlist"></a>
# メソッド（Tello-Console コマンド一覧）
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
