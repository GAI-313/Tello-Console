# Tello-Console 7.1.0

<center>
<img src="https://i.imgur.com/zYsdoJo.jpg">
</center>

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
 - **[Tello-Console をどのディレクトリからでも実行できるようにする](#pythonpath)**<br>　どの場所からでも Tello-Console を実行できるようにする方法を解説します。
 - **[エデュケーション](#educatoin)**<br>　Pythonの でプログラミングをする方法や、Tello-Console の簡易的な使用方法をまとめています。
    - **[スタディサポート](#study_support)**<br>　Tello-Console を使う前に１から Python を勉強してみたい方はこちらを参照してください。Tello-Console をつかってドローンをプログラミングするまでの道のりを記述しています。
    - **[TELLO EDU ユーザーガイド](#user-guide)**<br>　TELLO EDU 本体の使用方法を解説します。
    - **[サンプルコードチュートリアル](#samplecode_tutorial)**
    - **[Tello-Console を使う方法（経験者向けの内容です）](#howto)**<br>　Tello-Console を今すぐ扱いたい方はこちらを参考にしてください。
- **[メソッド（Tello-Console コマンド一覧）](#commandlist)**<br>　Tello-Console に用意されているメソッド（コマンド）の一覧です。
- **[リリースノート](#releasenote)**<br>　tello-Console のアップデート情報をまとめています。こちらからアップデートされた Tello-Console の追加機能、変更内容などの更新状況を確認できます。

<a id="intro"></a>
# 紹介

　Tello-Console は DJI Ryze Tech Tello-EDU 向けの Python プログラムツールです。このライブラリを実装することで、ドローン操作メソッド（ドローンを操作するためのプログラム関数）をコマンド感覚で使用でき、Python をこれから始める人でもすぐにドローンを使ったプログラムの実装が可能になります。ベースとした SDK は 
[TelloSDK](https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf)
 で、これらに追加機能を多く搭載し最適化したものが Tello-Console です。
<br>

**主な特徴**

- **わかりやすいステータス表示**<br>　ドローンに対してどんなコマンドを送信したか、ドローンからどのような応答が来たのか、どのようなエラーが発生したのか、そのエラーの解決方法はあるのか、などの状況を表示してくれるので、自己解決が容易にできます。また、Tello-Console と Tello 間の通信状況の表示を無効にすることもできます。
- **自動着陸問題を回避できる**<br>　Tello は SDK モード（プログラムによってドローンを操作できるモード）の時、15秒間何もコマンドが送信されないと自動で着陸します。この問題は本ライブラリではデフォルトで無効になっているため、ドローンを継続して飛行させることができることで柔軟なプログラムを構築できます。
- **カメラへのアクセスが容易**<br>　Tello のカメラへアクセスするには、OpenCV を使用して、frame 変数を取得するだけで使用できます。<br>　また、
[TelloSDK 3.0](https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf) 
によって Tello の前方カメラだけでなく、機体下部のビジョンカメラへのアクセスも可能です。
- **豊富なコマンド**<br>　TelloSDK3.0 のコマンドに加え、オリジナルのコマンドも搭載しているため、柔軟かつ複雑なタスクを組むことができます。詳しくはコマンド一覧を参照してください。
- **アップデートして新機能を使う**<br>　Tello-Console は不定期に更新します。アップデートをするたびに新たなチュートリアル、機能、修正を施します。詳しい更新情報はリリースノートを参照してください。
- **チュートリアルによるコーディングサポート**<br>　Tello-Console をすぐに、楽しく使用できるために、チュートリアルを日々作成中です。初心者でもわかりやすい記事を目指して現在製作中なので、乞うご期待。

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

### 1.コマンドプロンプトを開く
　検索バーに **cmd** と入力して、**コマンドプロンプト** を開きます。
> ~~コマンドプロンプトについて詳しく知りたい場合は、**[コマンドプロンプト　コマンドガイド]()** を参照してください。現在作成中。

<center>
<img src='https://i.imgur.com/s8JJNEA.png' height=400>
</center>

### 2.python コマンドを入力する
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

### 3.python をインストールする
  　**MicroSoft Store** が開いたら、**インストール** をクリックして、表示されている **python** をインストールします。
  <center>
  <img src='https://i.imgur.com/NF2hJqH.jpg' height=400>
  </center>
  <br>

  **インストールボタン** が、**スタートピンに固定** に表示が変わったらインストールは完了です。コマンドプロンプトに戻り、もう一度 **python** コマンドを実行してください。

<a id='winp4'></a>
### 4.確認
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

### 5.必要なパッケージをインストールする
  　以下のコマンドを **1行づつコピペして** 実行します。
```bash
pip3 install opencv-python
```

### 6.Tello-Console をインストールする
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

### 7.Tello-Console をダウンロードする
　コマンドプロンプトに戻り、以下のコマンドを **1行づつコピペして** 実行します。
```Bash
cd %homepath%
git clone https://github.com/GAI-313/Tello-Console.git
```

> **コマンドプロンプトで git コマンドが認識されない場合**<br>
        上記の git コマンドを実行したとき、以下のようなエラーが表示された場合、**以下の手順** に沿って Tello-Console をインストールしてください。<br>       　
  <center>
  <img src='https://i.imgur.com/PEJ8Xjh.jpg'>
  </center>
  <br>
  
  1. **Git for Bash を開く**<br>
      git for bash とは、先ほど説明した **コマンドプロンプトみたいなウィンドウ** のことです。<br>
      <center>
      <img src='https://i.imgur.com/IobUWSP.jpg' height=300>     
      </center>
      <br>
        もし、上記のウィンドウが表示されていない場合は、**検索バー** で **"git"** と入力して候補に出てきた **"Git Bash"** を実行してください。<br>
        
  2. **コマンドを実行**<br>
      　以下のコマンドを **１行ずつコピペ実行してください。** Git Bash は、**ショートカットキー Control + V** が利用できません。右クリックして **Paste** をクリックしてください。<br>
      ```
      cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
      ```
      <center>
      <img src='https://i.imgur.com/UgwW41M.jpg' height=300>
      </center>

これで **WindowsにTello-Console のインストールする作業は完了です！！**

> **ヒント**
    <br>
    　Tello-Console ディレクトリをエクスプローラ上でクイックアクセスに登録しておくことで、素早くアクセスすることができるようになります。


**[Tello-Console を実行してみる に進む](#taskdo)**

<a id="install_mac"></a>
## macOS に Tello-Console を導入する方法

　macOS に Tello-Console をインストールする方法を解説します。紹介する導入方法は、**macOS Monterey（12.0）** で検証した導入方法となります。それ以前、以降の macOS では、若干操作方法が異なる場合があります。

### 1.ターミナルを開く
1. Command キーとSpace キーを押して SpotLight 検索を開きます。
2. Spotlight 検索欄内に **"ターミナル"** と入力します。
3. 候補として出てきた **"ターミナル.app"** を起動します。

> **ターミナルの外観設定をしていない方へ**<br>
> **[ターミナルの外観を最適化する](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/for_mac/terminal_setting_tutorial.md#ターミナルの外観を最適化する)** を参照し、ターミナルの外観を設定してください。Tello-Console を実行する際の表示に問題が発生します。（今後対策予定）

### 2.Pythonのセットアップ
　macOS はバージョンまたはお使いの環境によって Python の環境も異なります。ここではあなたが使用している Mac に標準インストールされている Python のチェックと Python のセットアップ方法を紹介します。<br>

以下のコマンドを**コピペ**してコマンドを実行してください。コマンドの実行は **エンターキー**を押すだけです。
<a id='mac_checkpyv'></a>
```bash
python -V
```
　このコマンドは、Mac に標準でインストールされている Python のバージョンを確認するコマンドです。この時、**お使いの Mac の環境によって応答してくるテキストが異なります。**
以下の項目に該当した場合、項目をクリックしてセットアップを行ってください。
- [**zsh: command not found: python** または **bash: command not found: python** と返された場合](#pya)
- [**python 2.x.x** と返された場合](#pyb)
- [**python 3.x.x** と返された場合](#pyc)

<a id="pya"></a>
### A. zsh: command not found: python または bash: command not found: python と返された場合
　このテキストが表示された場合、```python``` というコマンドが使用できない状態を表しています。```python3``` コマンドが使用できるか確認してみましょう。以下のコマンドをターミナルで実行してください。
```bash
python3 -V
```
```python 3.x.x``` という応答がされたら、お使いの Mac では python3 コマンドが有効であることを表しています。以下のコマンドをターミナルで実行して、python コマンドでも python3 コマンドを実行できるようにします。<br>
　まずは現在のシェル環境を変更します。以下のコマンドをターミナルで実行してください。
```bash
chsh -s /bin/bash
```
次に、**Command + Q** でターミナルを終了し、再度ターミナルを開いてください。<br>
　再度ターミナルが開いたら、以下のコマンドを実行してください。このコマンドは ```python``` というコマンドで ```python3``` コマンドを実行できるようエイリアスを作成するコマンドです。
```bash
echo "alias python='python3'" >> ~/.bash_profile
```
同様に以下のコマンドも実行してください。
```bash
echo "alias pip='pip3'" >> ~/.bash_profile
```
　これで python の設定は完了です。```python -V``` コマンドを実行して python3 のバージョンが表示されることを確認してください。
```bash
python -V
```
　これで Tello-Console をインストールする準備が整いました。
 
<a id="pyb"></a>
### B. python 2.x.x と返された場合
　このテキストが返されたら、現在お使いの Mac にインストールされている Python のバージョンが python2 系列であることを示しています。Tello-Console は **Python2 環境では実行できません。** ここではお使いの Mac に Python3 をインストールする方法を紹介します。<br>
　以下のコマンドを実行して、**コマンドライン・デベロッパ・ツール** のインストールを行います。
```bash
gcc
```
　すると、画面上に以下のようなポップアップが表示されるので、**インストール** をクリックしたのちに **同意** をクリックしてください。
<center>
<img src='https://i.imgur.com/91TaW55.png' height=300>
</center>

> Mac が電源に繋がれていないと電源に接続するように促されます。インストール作業には少々時間がかかるため、電源に接続することを推奨します。

インストールが完了したら、以下のコマンドを実行してシェルの環境を変更します。
```bash
chsh -s /bin/bash
```
次に、**Command + Q** でターミナルを終了し、再度ターミナルを開いてください。<br>
　再度ターミナルが開いたら、以下のコマンドを実行してください。
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
　このコマンドを実行すると、途中 **パスワードの入力が求められます。** パスワードを入力した後に、**RETURN キーを押すように要求される** ので、要求されたらエンターキーを押してください。<br>
　正常にコマンドのプロセスが終了したら、以下のコマンドを実行して、**Python 3** をインストールします。
```bash
brew install python@3.8
```
　Python 3 のインストールが完了したら、以下のコマンドを実行してください。このコマンドを実行することで Mac 内に点在する Python 3 関連のパッケージを統一します。
```bash
ln -s /usr/local/opt/python@3.8/bin/python3.8 /usr/local/bin/python3.8
```
　以下のコマンドを実行して、Python 3 系列がインストオールされているか確認してください。
```bash
python -V
```
　もし、返されたテキストが ```python 2.x.x``` である場合、以下の手順に沿ってください。
1. 以下のコマンドを実行してください。このコマンドは ```python``` というコマンドで ```python3``` コマンドを実行できるようエイリアスを作成するコマンドです。
    ```bash
    echo "alias python='python3'" >> ~/.bash_profile
    ```
2. 同様に以下のコマンドも実行してください。
    ```bash
    echo "alias pip='pip3'" >> ~/.bash_profile
    ```

　これで python コマンドで python3 コマンドを実行できるようになりました。<br>
　返されたテキストが ```python 3.x.x``` である場合、Python のセットアップは完了です。これで Tello-Console をインストールする準備が整いました。

<a id="pyc"></a>
### C. python 3.x.x と返された場合 
　Python のセットアップは必要ありませんが、以下のコマンドを実行して、シェルの環境を変更してください。
```bash
chsh -s /bin/bash
```
次に、**Command + Q** でターミナルを終了し、再度ターミナルを開いてください。<br>
　これで Tello-Console をインストールする準備が整いました。

### 3. Tello-Console をインストールする
　次に Tello-Console をインストールします。Tello-Console をインストールするには、事前にいくつかのライブラリをインストールする必要があります。以下の手順に沿ってインストール作業を行なってください。<br>
　ターミナルを開き、以下のコマンドを実行して pip をインストールするための python スクリプトをインストールします。
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
すると、このコマンドを実行したフォルダ内に ```get-pip.py``` という python スクリプトがインストールされます。以下のコマンドでこのスクリプトを実行します。
```bash
python3 get-pip.py
```
これでお使いの Mac で pip を使って python のパッケージをインストールできるようになりました。以下のコマンドを使って画像処理を扱うのに必要となる openCV をインストオールします。
```
pip3 install opencv-python
```
　最後に、Git を使って Tello-Console をインストールします。Git コマンドを使うことで、GitHub にある Tello-Console を Mac に持ってくることができます。以下のコマンドを実行してください。
```
cd ~ && git clone https://github.com/GAI-313/Tello-Console.git
```
　これで **macOS に Tello-Console** の導入は完了です。<br>
　Tello-Console を使用してプログラムを作成するには、VScode がお勧めです。こちらで VScode のインストール方法を案内しています。（初心者向け）

　- **[macOS に VScode をインストールする方法](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#mac-に-vscode-をインストールする方法)**

**[Tello-Console を実行してみる](#taskdo)** に移動する。

<a id="install_ubuntu"></a>
## Ubuntu（Linux） に Tello-Console を導入する方法
　Ubuntu に Tello-Console をインストールする方法を解説します。紹介する導入方法は、**Ubuntu 20.04 LTS** で検証した導入方法となります。それ以前、以降の Ubuntu では若干、操作方法が異なる場合があります。

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
　インストール作業が無事終了すると、**ホームディレクトリ（ユーザーネームの名前のフォルダ）** に Tello-Console **ディレクトリ（フォルダのこと）** がダウンロードされています。**Tello-Console ディレクトリに移動して、sample_boot.py サンプルプログラムを実行して正常に Tello-Console が実行されるか試してみましょう**。<br>

- Windows をお使いの方
    1. コマンドプロンプトを開く
    2. 以下のコマンドを **1行ずつ** 実行して Tello-Console ディレクトリへ移動する
        ```bash
        cd %homepath%
        cd Tello-Console
        ```
- macOS、Linux ChromeOS をお使いの方
    1. ターミナル（端末）を開く
    2. 以下のコマンドを実行して Tello-Console ディレクトリへ移動する
        ```bash
        cd ~/Tello-Console
        ```
### sample_boot.py を実行する
　当セクション内の目次

- [サンプルコードの実行](#sample_a)
- [Linux で python に関するエラーが発生する場合](#sample_a)
- [Windows のシンタックスハイライト設定](#sample_c)

<a id="sample_a"></a>
　Tello-Console ディレクトリ内には豊富なサンプルコードが用意されています。ここでは、正常に Tello-Console が機能するかどうか確認するためにサンプルコードの一つである **sample_boot.py** を実行してみましょう。<br>
　```sample_boot.py``` を実行するには、コマンドプロンプトまたはターミナルで以下のコマンドを実行します。このコマンドは WIndows、macOS、Linux 共通です。
```bash
python sample_boot.py
```

<a id="sample_b"></a>
> Linux を使用している方へ<br>
> 　Linux を使用している方で、```python``` コマンドを実行すると、以下のようなエラーが発生する可能性があります。
> ```bash
> コマンド： 'python' が見つかりません。もしかして：
> command 'python3' from deb python3
> command 'python' from deb python-is-python3
> ```
> または
> ```bash
> command 'python' not found, did you mean:
> 
> command 'python3' from deb python3
> command 'python' from deb python-is-python3
> ```
> この場合、python コマンドの代わりに python3 コマンドで python を実行してください。これらのエラーは python 2 系列の python が環境に存在しないことを表しています。

すると、以下のようなテキストが表示されたら **無事 Tello-Console が実行されたことを表しています。**<br>

実行結果↓
```bash
WELCOME CONSOLE ! TELLO-CONSOLE Vx.x.x
タイムアウト!
エラー！ドローンとの通信に失敗しました！
Tips:ドローンとPCとのWi-Fi接続を確認してください！
```

<a id="sample_c"></a>
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
<a id="pythonpath"></a>
# Tello-Console をどのディレクトリからでも実行できるようにする
　Tello-Console を使うには、基本的に **Tello-Console ディレクトリ内でしか動作しません。** ですが、このセクションを参照することでどのディレクトリからでも tello-Console をつかったコーディングが可能になります。<br>

　OS によって設定方法が異なります。お使いの OS の項目をクリックして進んでください。

> この作業は若干難しく、ファイルパスに関する知識が求められます。作業を進める際は気を付けて進んでください。

- [Windows の場合](#pypath_win)
- [macOS の場合](#pypath_mac)
- [Linux の場合](#pypath_linux)

<a id="pypath_win"></a>
## Windows の場合
### 1. システム環境変数の設定を開く
　検索バーに ```env``` と入力して、上位に候補として出てきた **システム環境変数の設定** を開きます。<br>

　次に、設定内の **環境変数(N)** をクリックします。<br>

　**システム環境変数(S)** の綱目欄下にある **新規(N)** をクリックします。

### 2. tello.py のパスを入力する
　新しいシステム変数の変数名に、**PYTHONPATH** と書きます。すべて大文字です。<br>
　つぎに、変数値に **Tello-Console の tello.py までのパス** を入力します。以下の手順に沿って tello.py を追加します。

1. **ファイルの参照(D)...** をクリックします。
2.  フォルダ一覧が表示されたら、あなたのユーザー名をクリックしてください。するとTello-Console が一覧にでてきます。
3. Tello-Console の modules フォルダを指定して、 **"OK"** をクリックしてください。
4. 変数値に以下のような文字列が追加されたことを確認してください。
    ```
    C:\Users\ユーザー名\Tello-Console\modules\tello.py
    ```

そしたら **"OK"** をクリックして、PYTHONPATH を追加してください。

### 3. 確認
　コマンドプロンプトまたは VScode（Visual Studio）を使って tello ライブラリをインポートできるか確認してください。<br>
　ここから少しややこしいのですが、今回の作業で **Tello-Console を呼び出す方法が変わります。** どういうことかというと、PYTHONPATH に tello.py を登録する前は、python に Tello-Console を呼び出す際以下のように記述しました。
```python
from modules.tello import console
```
　しかし、PYTHONPATH に登録したときは、modules ディレクトリ内にある tello.py を直接登録したことで、以下のように記述します。
```python
from tello import console
```
　このように、**modules を記述する必要がなくなります** 。```from modules...``` の記述方法が通用するのは **Tello-Console ディレクトリ内のみ** となりますので気をつけてください。<br>
　話は戻りますが、**Tello-Console 以外のディレクトリ** で以下の作業を行なってください。

1. コマンドプロンプトを開きます。
2. ```python``` コマンドを入力してください。
3. コマンドプロンプトの入力欄が ```>>>``` になったら、以下のコードを入力してください。
    ```from tello import console```
4. エンターキーを押してコードを実行します。この時、何もエラーが出なければ成功です。逆に以下のようなエラーが発生したら失敗です。
    ```ImporttError```
### 2. 
<a id="pypath_mac"></a>
## macOS の場合
　以下の手順に沿って作業を進めてください。
### 1. modules ディレクトリに移動する
　ターミナルを開き、以下のコマンドを実行してください。
```bash
cd ~/Tello-Console/modules
pwd
```
　すると、下のような **modules ディレクトリまでのパス** が表示されます。

> お使いの環境によって下のパスの表記が異なります。以下のパスはあくまで例です。

```bash
/usr/home/NAME/Telllo-Console/modules
```
その返されたパスをコピーしてください。

### 2. 環境変数に書き加える
　環境変数とはパソコンの環境を構成するのに必要な変数のことを言います。Python のライブラリのパスを補完する環境変数 ```PYTHONPATH``` に **Tello-Console の modules ディレクトリまでのパス** を記述します。<br>
　以下のコマンドを書いてください。**<PATH>** の部分には **先ほどコピーした modules ディレクトリまでのパス** を記述します。そのまま書いて実行しないでください！
```bash
echo "export PYTHONPATH=$PYTHONPATH:<PATH>" >> ~/.bash_profile
```
　最後にターミナルを以下のコマンドを実行して再読み込みします。
```bash
source ~/.bash_profile
```
### 3. 確認
　Python を使って確認しましょう。ターミナルを開き、現在いるディレクトリ（カレントディレクトリ）を変更します。
```bash
cd ~
```
　次に、Python をターミナル上で開きます。
```
python
```
　すると、このように Python コマンドラインがターミナル内で開きます。
```bash
Python 3.8.2 (default, Apr  8 2021, 23:19:18) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
　ここに以下のコードを書いてください。
```python
from modules.tello import console
```
　上のコードを記述してエンターキーを押して実行してください。
```
>>> from modules .tello import console
```
　実行した時、何も表示されず次の入力欄が出たら成功です。
```
>>> from modules .tello import console
>>>
```
　続いて、以下のコードを書いて実行すると、Tello-Console の接続シークエンスが実行されます。
```python
drone = console()
```
　これを実行すると以下のように、ドローンに接続されていないため、強制的に Python プロンプトが終了されます。
```
>>> drone = console()
WELCOME CONSOLE ! TELLO-CONSOLE Vx.x.x
タイムアウト!
エラー！ドローンとの通信に失敗しました！
Tips:ドローンとPCとのWi-Fi接続を確認してください！
$
```
　これでどのディレクトリにいても Tello-Console が使用できるようになりました。<br>
**[エデュケーションに進む](#education)**
<a id="pypath_linux"></a>
## Linux の場合
現在有効な手順を調査中

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

- **[Python チュートリアルその1 Python を始めよう](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/python_tutorial_1-1.md)**
- **[Python チュートリアルその2 四則演算 ](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/python_tutorial_2.md)**

<a id="user-guide"></a>
## TELLO EDU ユーザーガイド
　[こちら](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/basic_tutorial/how2use_telloedu.md#tello-edu-ユーザーガイド) から TELLO EDU の基本的な使用方法をまとめています。
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
　Tello-Console の本体は、```Tello-Console/modules``` ディレクトリにある **tello.py の中にある console クラス** です。これを呼び出すことで使用することができます。<br>

　console クラスを使用するには、**必ず tello-Console ディレクトリ内でプログラムを記述してください。** （PYTHONPATH を使い環境に反映させる方法を模索中です。）
```python3
from modules.tello import console
```
　console クラスを、任意の変数に格納することでインスタンス化（活性化）し、インスタンス化された時点で console クラスのドローンへの接続準備およびドローンに対する診断を行います。
```python3
from modules.tello import console

drone = console()
```
　console クラスに用意された各メソッドが **ドローンを操作するためのコマンド** として機能します。例えば、Tello を離陸、着陸させるなら、このように書けば実装できます。詳しい情報は **[メソッド、コマンド一覧](#commandlist)** または VScode からサマリーを参照してください。
```python3
from modules.tello import console

drone = console() # インスタンス化。ここで 変数 drone が console クラスと同等となる

drone.takeoff() # takeoff メソッドを実行し、ドローンを離陸させる

drone.land() # land メソッドを実行し、ドローンを着陸させる
```
　Tello-Console コマンド（メソッド）については、
**[メソッド（Tello-Console コマンド一覧）](#commandlist)**
を参照してください。
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
- **[takeoff コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/takeoff.md)**
- **[motor_start コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/motor_start.md)**

### 着陸、モーター関連コマンド
- **[land コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/land.md)**
- **[motor_stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/motor_stop.md)**

### 安全、緊急停止コマンド
- **[emergency コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/emergency.md)**
- **[stop コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/stop.md)**

### 簡易操作コマンド
- **[up コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/up.md)**
- **[down コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/down.md)**
- **[forward コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/forward.md)**
- **[back コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/back.md)**
- **[left コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/left.md)**
- **[right コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/right.md)**
- **[cw コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/cw.md)**
- **[ccw コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/ccw.md)**
- **[flip コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/flip.md)**

### 高度操作コマンド
- **[rc コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/rc.md)**
- **[go コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/go.md)**
- **[curve コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/curve.md)**

<a id='cmd_b'></a>
## 設定コマンド
- **[reboot コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/reboot.md)**
- **[wait コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/wait.md)**

<a id='cmd_c'></a>
## 取得コマンド
- **[get_flighttime コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_flighttime.md)**
- **[get_height コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_height.md)**
- **[get_tof コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_tof.md)**
- **[get_imu コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_imu.md)**
- **[get_speed コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_speed.md)**
- **[get_battery コマンド](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/command_list/get_battery.md)**
---
現在作成中

<a id="releasenote"></a>
# リリースノート
## Tello-Console Ver.7.1.0
　このバージョンではドキュメントの修正及び重要なプログラムの修正を含みます。<br>
　以下の機能を修正しました。

- ビデオ通信機能の大幅な変更<br>
    　以前の Tello-Console（Ver 7.1.0 前）では、console クラスが呼び出された時にカメラデータを取得していましたが、今回のバージョンから **コマンドからビデオデータを取得する** 仕様に変更となりました。
    これにより、既存していた以下のコマンドの仕様が変更となります。

    - stream コマンド
        - 更新前<br>
            ドローンにビデオストリームを開始または停止するようリクエストする
        - 更新後<br>
            ドローンにビデオストリームを開始または停止するとともにビデオデータをエンコードするスレッドを管理し、スムーズにビデオデータを取得または廃棄できるように対応。

    この修正は **Chrome OS で OpenCV が正常に機能しない** 問題を一時的に回避するために作成されました。これにより **サンプルコードの仕様が一部変更となります。**

　以下の機能を追加しました。
- ビデオデータ受信時にタイムアウト機能を追加<br>
    　ビデオデータを受信する際に、5秒間ビデオデータを取得できなかったらコマンドをスキップするタイムアウト機構を追加しました。OpenCV を使用時にタイムアウトが発生したらプログラムを停止するよう促すイメージデータを渡します。

　Chrome OS を使用している方はこのバージョンに **必ずアップデートしてください。** アップデート方法は **Tello-Console をアップデートする** セクションを参照してください。

## Tello-Console Ver.7.0.2
　チュートリアルの作成、修正を行いました。（3／20）<br>
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
