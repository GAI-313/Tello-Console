# コマンドプロンプト利用ガイド

<a id=syntaxhighlight></a>
## コマンドプロンプトで Tello-Console のシンタックスハイライトを有効にする
　Tello-Console からの応答分を、**強調表示** する方法を紹介します。

1. **VScode を開く**
    <br>
    VScode をインストールしていない場合、
    <br>
    **[VScode をインストールする](https://github.com/GAI-313/Tello-Console/blob/master/tutorial/visual_studio_tutorial/install_and_setup_guide.md#windows-に-vscode-をインストールする方法)**
    <br>
    を参照して、VScode をインストールしてください。
2. **Tello-Console の tello.py を開く**
    <br>
    　VScode が開いたら、**Control + O** でファイルエクスプローラを開きます。
    <br>
    　以下の順に沿ってフォルダ階層を移動してください。
    ```
    (C:)ドライブ > ユーザー > ユーザー名 > Tello-Console > modules
    ```
    modules フォルダ内に、**tello.py** というファイルがあるので、これを指定して開きます。
    <br>
    <img src='https://i.imgur.com/M0EN5SR.jpg'>
3. **コメントアウトを外す**
    <br>
    　VScode で、tello.py を開いたら、**14行目の（"""）** と、**25行目の（"""）** を削除してください。
    <br>
    <img src='https://i.imgur.com/6YsegeS.jpg'>
4. Control + S で変更を保存して完了です。

変更後、サンプルコードなどを用いて実行してみましょう。すると、**テキストがハイライト表示されるようになります。**
<br>
<img src='https://i.imgur.com/5bhayMS.jpg'>
<br><br>
**[Tello-Console を実行してみる　に戻る](https://github.com/GAI-313/Tello-Console/tree/windows#tello-console-%E3%82%92%E5%AE%9F%E8%A1%8C%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B)**
