# Tello-Console 7.0.2

English version is **[here](https://github.com/GAI-313/Tello-Console/blob/eng/README.md)**

# 現在工事中！！！
不定期に更新します。ご了承ください。<br>

　このライブラリは 
[TelloSDK](https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf) 
をもとに初心者でもわかりやすく Tello ドローンを使ったプログラムを作成、実行できるラッパークラス **tello.py** を提供します。

# 目次

 - **[紹介](#intro)**<br>　Tello-Console に関する簡単な説明と紹介をまとめています。
 - **[Tello-Console をインストールする方法](#install)**<br>　Tello-Console をインストールする方法を解説します。
    - **[Tello-Console を実行してみる](#taskdo)**<br>　Tello-Console を実行する方法を解説します、これを読む前に**Tello-Console をインストールしている必要があります。**
 - **[アップデート](#update)**<br>　Tello-Console をアップデートする方法を解説します
 - **[エデュケーション](#educatoin)**<br>　Pythonの でプログラミングをする方法や、Tello-Console の簡易的な使用方法をまとめています。
    - **[Tello-Console を使う方法（経験者向けの内容です）](#howto)**<br>　Tello-Console を今すぐ扱いたい方はこちらを参考にしてください。
    - **[スタディサポート](#study_support)**<br>　Tello-Console を使うまえに１から Python を勉強してみたい方はこちらを参照してください。Tello-Console をつかってドローンをプログラミングするまでの道のりを記述しています。
    - **[サンプルコードチュートリアル](#samplecode_tutorial)**
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

  > ~~コマンドプロンプトについて詳しく知りたい場合は、**[コマンドプロンプト　コマンドガイド]()** を参照してください。~~
    現在作成中。

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

  実行して、**Microsoft Store** が開いたら、**手順3** から順番に作業を進めてください。Microsoft Store アプリが開かずにコマンドプロンプトの表示が変わったら **[手順4](#winp4)** から作業を進めてください。あなたの環境にはすでに python がインストールされています。

3. **python をインストールする**
  <br>

  　**MicroSoft Store** が開いたら、**インストール** をクリックして、表示されている **python** をインストールします。
  <center>
  <img src='https://i.imgur.com/NF2hJqH.jpg' height=400>
  </center>
  <br>

  **インストールボタン** が、**スタートピンに固定** に表示が変わったらインストールは完了です。コマンドプロンプトに戻り、もう一度 **python** コマンドを実行してください。

<a id='winp4'></a>
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
  ```

6. Tello-Console をインストールするには、**git**  をインストールする必要があります。
  <br>

  　Tello Console は、Git というプログラムを共有できる場所からインストールする必要があります。そのためにここで git をセットアップを行います。<br>

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

7. **Tello-Console をダウンロードする**
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


**[Tello-Console を実行してみる に進む](#taskdo)**

<a id="install_mac"></a>
## macOS に Tello-Console を導入する方法

　macOS に Tello-Console をインストールする方法を解説します。紹介する導入方法は、**macOS Monterey（12.0）** で検証した導入方法となります。それ以前、以降の macOS では、若干操作方法が異なる場合があります。

1. Command キーとSpace キーを押して SpotLight 検索を開きます。
2. Spotlight 検索欄内に **"ターミナル"** と入力します。
3. 候補として出てきた **"ターミナル.app"** を起動します。

> **ターミナルの外観設定をしていない方へ**<br>

    　**[ターミナルの外観を最適化する](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/for_mac/terminal_setting_tutorial.md#ターミナルの外観を最適化する)** を参照し、ターミナルの外観を設定してください。Tello-Console を実行する際の表示に問題が発生します。（今後対策予定）

4. 以下のコマンドを**コピペ**してコマンドを実行してください。コマンドの実行は **エンターキー**を押すだけです。
    <a id='mac_checkpyv'></a>
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

7. **この作業は Python のバージョンが 3.x.x の方は実行しないでください**<br>　以下のコマンドを**コピペして実行**してください。すると **Python 3.8.x がインストールされます。**<br>
    > **[お使いの Mac の Pytrhon のバージョンを調べる方法](#mac_checkpyv)**
    
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
  cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
  ```

　これで **macOS に Tello-Console** の導入は完了です。<br>

　Tello-Console を使用してプログラムを作成するには、VScode がお勧めです。こちらで VScode のインストール方法を案内しています。（初心者向け）

　- **[macOS に VScode をインストールする方法](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#mac-に-vscode-をインストールする方法)**

**[Tello-Console を実行してみる](#taskdo)** に移動する。

<a id="install_ubuntu"></a>
## Ubuntu（Linux） に Tello-Console を導入する方法
　Ubuntu に Tello-Console をインストールする方法を解説します。紹介する導入方法は、**Ubuntu 20.04 LTS** で検証した導入方法となります。それ以前、以降の Ubuntu では、若干操作方法が異なる場合があります。

> 報告<br>
    来月（2023/4）に ChromeOS に Tello-Console をインストールする方法をこのセクションに追記予定です。

1. Control キーと ALT キーと T キーを押して **端末（ここではターミナルと呼ぶことにする）** を開きます。
2. ターミナルに、以下のコマンドを **1行づつコピペして** コマンドを実行します。コマンドの実行は **エンターキー** を押すだけです。実行すると、**はじめにパスワードの入力が求められます。** ログイン時のパスワードを入力してエンターキーを押してください。

  ```bash
  sudo apt update
  suto apt install -y python3-pip3 git
  pip3 install opencv-python3
  cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
  ```

　これで **Ubuntu に Tello-Console** の導入は完了です。

**これで Tello-Console** のインストールは完了です。<br>

　Tello-Console を使用してプログラムを作成するには、VScode がお勧めです。こちらで VScode のインストール方法を案内しています。（初心者向け）

　- **[macOS に VScode をインストールする方法](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#ubu)**

<a id="taskdo"></a>
## Tello-Console を実行してみる
　インストール作業が無事終了すると、**ホームディレクトリ（ユーザーネームの名前のフォルダ）** に Tello-Console **ディレクトリ（フォルダのこと）** がダウンロードされています。**Tello-Console ディレクトリに移動して、sample_boot.py サンプルプログラムを実行して正常に Tello-Console が実行されるか試してみましょう**。
<br>

　以下の操作は **Windows、macOS、Ubuntu 共に同じです。**

1. **Tello-Console ディレクトリに移動する**<br>　以下のコマンドをコピペして、Tello-Console ディレクトリに移動します。
```bash
cd Tello-Console
```

2. **sample_boot.py を実行する**<br>　以下のコマンドをコピペして、sample_boot.py というサンプルプログラムを python で実行します。
```bash
python sample_boot.py
```

>**SyntaxError が出た場合**<br>　Python3 をインストールした方は、実行コマンド ```python``` を、```python3``` で実行してください。
  ```bash
  python3 sample_boot.py
  ```
　すると、以下のようなテキストが表示されたら **無事 Tello-Console が実行されたことを表しています。**<br>

実行結果↓
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

**[コマンドプロンプトで Tello-Console のシンタックスハイライトを有効にする](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/windows/cmd_tutorial.md#コマンドプロンプトで-tello-console-のシンタックスハイライトを有効にする)**
<br>

を参照してください。

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
　ここでは、Tello-Console の使用方法や、プログラミングをするのにあたり必要なスキルを学べるカリキュラムを用意しています。以下の目次からあなたのスキルに合った学習を進めることができます。（現在作成中）

- **Python 初心者**
    現在作成中
- **python 経験者（基本的な構文を理解している）**
    現在作成中
- **python 経験者（関数、クラスを理解し、オブジェクト指向のプログラムを作成できる）**
    現在作成中
- **とにかくドローンをプログラムしたい方には**
    現在作成中
- **画像処理を専門に学びたい方**
    現在作成中
<a id="study_support"></a>
## スタディサポート
　Tello-Console は、ドローンを使ってプログラミングの楽しさ、面白さを知ってもらうことを目的に作られました。以下の記事一覧を散走することで、**Python、CUI コマンド、Tello-Console の使用方法、画像処理**に関する知識を習得できます。（現在作成中）

- **[Python チュートリアルその1](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/python_tutorial_1.md#python-チュートリアルその1)**

<a id="samplecode_tutorial"></a>
## サンプルコードチュートリアル
　Tello-Console にデフォルトでダウンロードされているサンプルコードについて解説します。各サンプルコードの内容から、Tello-Console コマンドの使用方法を学ことができます。

- **[sample_boot.py]()**<br>
　Tello-Console を使うための基本
- **[sample_flight1.py]()**<br>
　Tello-Console を使い、Tello を離着陸させる方法
- **[sample_flight2.py]()**<br>
　簡易操作コマンドの使用方法
- **[sample_get_status1.py]()**<br>
　Tello から飛行データを取得する
- **[sample_video1.py]()**<br>
　Tello のカメラにアクセスする方法
- **[sample_video2.py]()**<br>
　Tello のカメラにアクセスし、キーボードでドローンを操作する方法
---
現在作成中
<a id="howto"></a>
## Tello-Console を使う方法（経験者向けの内容です）
　Tello-Console の本体は、```Tello-Console/modukes``` ディレクトリにある **tello.py の中にある console クラス** です。これを呼び出すことで使用することができます。<br>

　console クラスを使用するには、**必ず tello-Console ディレクトリ内でプログラムを記述してください。** （PYTHONPATH を使い環境に反映させる方法を模索中です。）
```python3
from modules.tello import console
```
　console クラスを、任意の変数に格納することでインスタンス化（活性化）し、インスタンス化された時点で console クラスのドローンへの接続準備およびドローンに対する診断を行います。
```python3
from modules.tello import console

drone = console()
```
　console クラスに用意された各メソッドが **ドローンを操作するためのコマンド** として機能します。例えば、Tello を離陸、着陸させるなら、このように書けば実装できます。詳しい情報は **[メソッド、コマンド一覧]()** または VScode からサマリーを参照してください。
```python3
from modules.tello import console

drone = console() # インスタンス化。ここで 変数 drone が console クラスと同等となる

drone.takeoff() # takeoff メソッドを実行し、ドローンを離陸させる

drone.land() # land メソッドを実行し、ドローンを着陸させる
```
　Tello-Concolse コマンド（メソッド）については、
**[メソッド（Tello-Console コマンド一覧）](#commandlist)**
を参照してください。
<a id="commandlist"></a>
# メソッド（Tello-Console コマンド一覧）
---
現在作成中

<a id="releasenote"></a>
# リリースノート
## Tello-Console Ver.7.0.2
　チュートリアルの作成、修正を行いました（3／20）
　いくつかのバグを修正しました。（3／16）

- get コマンドから取得されるデータから None が返される問題を修正しました。
- 全体の動作を軽量化させました。
- 通信プロトコルを最適化しました。

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
