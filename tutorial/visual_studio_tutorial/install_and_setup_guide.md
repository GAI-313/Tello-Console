# Visual Studio インストールガイド
　ここでは、**Visual Studio** インストールする方法と、設定方法を紹介します。

<a id='install'></a>
# Visual Studio をインストールする
　以下のサイトから Visual Studio のインストールを行います。使用している　OS によってインストールするファイルが異なります。サイト内で OS ごとにインストールガイドが書かれているので、それに沿ってダウンロードします。

- https://code.visualstudio.com/download

<a id='win'></a>
## Windows に VScode をインストールする方法
**[Visual Studio の環境設定を行う に進む](#setting)**

<a id='mac'></a>
## mac に VScode をインストールする方法
- Finder のダウンロードフォルダに、VScode がダウンロードされています。これを **"アプリケーションフォルダ"** に移動します。
- Launchpad から、VScode を開きます。または Spotlight 検索で **"code"** と検索します。

これで mac に VScode のインストールは完了し、VScode が立ち上がります。
<br>
**[Visual Studio の環境設定を行う に進む](#setting)**

<a id='ubu'></a>
## Ubuntu（Linux） に VScode をインストールする方法
**[Visual Studio の環境設定を行う に進む](#setting)**

<a id='setting'></a>
# Visual Studio の環境設定を行う
　VScode をインストールし、VScode が起動すると、このような画面が表示されます。

> 画像は　macOS ですが、他の OS も同じように表示されます。

<br>
<img src='https://i.imgur.com/TMQXae7.png'>
<br>

<a id='jp'></a>
## 日本語化パッケージのインストール
　初めて VScode を起動すると、右下に **日本語化パッケージのインストール** が促されます。こちらの **インストールをクリックして VScode を日本語化しましょう。**
<br>
<img src='https://i.imgur.com/gtUgff0.png'>
<br>
　自動的に　VScode が再起動します。すると、VScode の言語が **日本語** になります。
<br>
<img src='https://i.imgur.com/iSXn0yz.png'>
<br>

<a id='py'></a>
## Python 拡張機能のインストール
　次は Python の拡張機能をインストールする方法を紹介します。この拡張機能をインストールすることで、VScode で Python を記述する効率が格段に良くなります。

1. 拡張機能タブをクリックします。
  <br>
  <img src='https://i.imgur.com/kYKpWf6.png'>
  <br>

2. 拡張機能の検索欄をクリックします
  <br>
  <img src='https://i.imgur.com/6FYVfeU.png'>
  <br>

3. 検索欄に **"python"** と検索します
  <br>
  <img src='https://i.imgur.com/wyzwftl.png'>
  <br>
  
4. **Python** の **"インストール"** をクリックします
  <br>
  <img src='https://i.imgur.com/KBwoTPj.png'>
  <br>

インストールボタンが消えたら、Python 拡張機能のインストールは完了です！
<br>
<img src='https://i.imgur.com/0uravvI.png'>
<br>

<a id='code'></a>
## code コマンドを有効にする
　CUI のコマンドで、```code``` コマンドを有効にすることで、指定したパス、ファイルを VScode で開くことができるようになります。

1. **VScode のシェルを開く**
  - **Windows、Ubuntu をお使いの場合、以下のショートカットキーを実行してください。**<br>
    Control キー + Shift キー + P
  - **macOS をお使いの場合、以下のショートカットキーを実行してください。**<br>
    command キー + Shift キー + P

  するとこのようなポップアップが表示されます。
  <br>
  <img src='https://i.imgur.com/hJZVuLv.png'>
2. **"Command: Install 'code' command in PATH"** をシェル内に入力する
  <br>
  <img src='https://i.imgur.com/I3XGmzh.png'>
  <br>

  **シェルコマンド：PATH ~~~** という選択欄が出るので、これをクリックします。

すると、パスワード入力が要求された後に以下のようなポップアップがでます。これが表示されたら成功です。

> 画像は macOS ですが、Widnows、Ubuntu でも同じようなポップアップが出ます。

<img src='https://i.imgur.com/UmP4jAD.png'>
<br>

### code コマンドの確認
　code コマンドの設定が完了したら、確認として実際に code コマンドを実行してみましょう。
#### Widnwos の場合
---
現在作成中

#### macOS の場合
Tello-Console を code コマンドで VScode から開いてみましょう。以下のコマンドで、Tello-Console ディレクトリに移動します。
```bash
cd ~/Tello-console
```
現在いるディレクトリ（カレントディレクトリ）を指定して、code コマンドを実行します。
```bash
code .
```
すると、Tello-COnsoke ディレクトリが VScode 上で開きます。初めて指定したディレクトリを VScode 上で開くと、このように **開いたファイルを信用するかどうか** を訪ねれらるので、**はい。信頼します。** をクリックしてください。

> ホームディレクトリ上全てのディレクトリを VScode 上で開くことを許可したい場合は、信頼ボタンの上にある **"親フォルダーXX内全てのファイルの作成者を信頼します"** にチェックを入れてください。

<br>
<img src='https://i.imgur.com/rn4UC9K.png'>
<br>

これで VScode の環境設定、構築は完了です！

#### Ubuntu（Linux）の場合
---
現在作成中
