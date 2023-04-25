# Python を始めよう
　この記事では、**Python を初めて始める方** に向けてのドキュメントとなります。Python を始める方はぜひご覧ください！
<br><br>

**目次**

- **[Python とは](#0)**
- **[Python を導入する](#1)**
- **[Python を CUI 上から実行する](#2)**

<a id="0"></a>
## python とは
　Python とは、**プログラミング言語の一種** です。プログラミング言語は、Python の他に以下のようなものがあります。

- C
- Rust
- C ++
- Java
- Ruby
- その他たくさん…

　Python は、**機械学習（AI）開発** 、**ロボット、ドローン開発** に特化したプログラミング言語で、特にロボット開発ではよく Python が採用されています。また、**Instagram** や **Youtube** なども **Python** で動いています。<br>
　Python は他の言語に比べてコードの書き方がとてもシンプルです。例えば、```Hello World !``` を出力するプログラムを、各プログラミング言語で見てみましょう。

- Jave
    ```java
    public class Hoge {
      public static void main (String [] args) {
        System.out.println ("Hello world!");
      }
    }
    ```

- C 言語
    ```cpp
    #include <stdio.h>
    int main() {
         printf("Hello World\n");
         return 0;
     }
    ```

- Ruby
    ```ruby
    puts "Hello, World!"
    ```

- Python
    ```python
    print("Hello World")
    ```

　比較すると、Python はかなりシンプルでわかりやすい構文でしょう。初めはプログラミング、Python に対してとても難しさを覚えるかもしれませんが、意味やコツさえ理解すれば簡単にプログラミングを楽しむことができます。<br>
　また、Python の構文を理解できるようになると、他の言語もなんとなく理解できるようになります！それでは、次のセクション **[Python を導入する](#1)** に移動しましょう！
　
<a id="1"></a>
## python を導入する
 お使いの PC に Python を導入しましょう。お使いの PC の **OS** によってインストール方法が異なります。以下の項目から、お使いの PC の OS を選択して進んでください。<br>
 下のリンクを押すと、Tello-Console のインストールセクションに飛びます。インストールセクションに Python のセットアップ方法がまとめられているので参照してください。

- **[Windows](https://github.com/GAI-313/Tello-Console#windows-に-tello-console-を導入する方法)**
- **[macOS](https://github.com/GAI-313/Tello-Console#macos-に-tello-console-を導入する方法)**
- **[Linux](https://github.com/GAI-313/Tello-Console#ubuntulinux-に-tello-console-を導入する方法)**

　それぞれの OS で CUI **コマンドライン**（コマンドプロンプト、ターミナル、端末のこと）を開き、以下のコマンドを実行して Python が正常に動作することを確認しましょう。
```
python
```
　成功すると、以下のような表示が出てきます。入力欄が ```>>>``` になったら成功です。
```
Python 3.8.2 (default, Apr  8 2021, 23:19:18) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
　次のセクション **[Python を CUI 上から実行する](#2)** に移動してください。

<a id="2"></a>
## python を CUI 上から実行する
　ここでおさらいです。CUI **コマンドライン** （コマンドプロンプト、ターミナル、端末のこと）を開き、以下のコマンドを実行して Python が正常に動作することを確認しましょう。
```
python
```
　成功すると、以下のような表示が出てきます。入力欄が ```>>>``` になったら成功です。
```
Python 3.8.2 (default, Apr  8 2021, 23:19:18) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
　この状態は、**コマンドライン上で Python のインターフェースを開いています。** この状態で、Python のコードを記述すると、1行づつプログラムが実行されます。実際に Python を使用するときはこのような使い方はせず、**プログラムファイル** を作ってそこにコードをまとめて書いて実行します。今回は先にこの Python インターフェースを使って Python の使い方について学びましょう。<br>
　試しに、以下のコードを書いてみましょう。

```python
print("Hello World !")
```
　```"``` は **ダブルクォーテーション** といい、日本語キーボードの **2** の部分にあります。US キーボードを使用している方は、```'``` **シングルクォーテーション** が使いやすいでしょう。<br>
　コードを書いたら、エンターキーを押しましょう。すると、以下のように ```Hello world``` と文字が出力されます。

```
>>> print("Hello World")
Hello world
>>>
```
　以下のように書くと、エラーが出てしまいます。<br>

**ダブルクォーテーションまたはシングルクォーテーションで文字列を括っていない**
```python
>>> print(Hello World)
  File "<stdin>", line 1
    print(Hello World)
                ^
SyntaxError: invalid syntax
>>> 
```
**ダブルクォーテーションまたはシングルクォーテーションを末尾に書いていない**
```python
>>> print("Hello World)
  File "<stdin>", line 1
    print("Hello World)
                      ^
SyntaxError: EOL while scanning string literal
>>> 
```
**ダブルクォーテーションとシングルクォーテーションが混在している**
```python
>>> print("Hello World')
  File "<stdin>", line 1
    print("Hello World')
                       ^
SyntaxError: EOL while scanning string literal
>>> 
```
　```Hello World``` 以外にも、以下のように文字列を書き換えれば、文字列を好きに表示させることができます。

```python
print("こんにちは")
```
```python
print("I'll be Back ...")
```
```python
print("吾輩は猫である。名前はまだない。")
```
　それでは、お好きな文字列を表示してみましょう。この括弧内に記述した要素を表示する ```print()``` を、**print関数（プリント関数）** と言います。後ほど詳しく説明します。<br>
　Python インターフェースを終了する方法は、入力欄に ```quit()``` と入力してエンターキーを押して実行するだけです。<br>
　次のドキュメントでは、**Python で計算する方法** を紹介します。<br><br>
次のドキュメント >>> **[Python で計算式を書く。〜四則演算]()**
