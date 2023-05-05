# Python で四則演算をしてみよう
　この記事では、**Python を初めて始める方** に向けてのドキュメント **第2回** となります。**第1回** をお読みでない方は、
**第1回** 
を参照してください。
<br><br>

**目次**

- **[四則演算 とは](#0)**
- **[Python を開く](#1)**
- **[Python を CUI 上から実行する](#2)**

<a id="0"></a>
## 四則演算 とは
　四則演算とは、皆さんが小学生で学んだ

- 足し算
- 引き算
- 掛け算
- 割り算

の **4つの基本的な計算方法** のことを指します。このドキュメントでは、**Python を使って四則演算を行う方法** について説明します。

<a id="1"></a>
## Python を開く
　それでは Python プロンプトを開きましょう。

1. **CUI を開く**<br>
    ここでいう CUI とは、

    - Windows のコマンドプロンプト
    - macOS のターミナル
    - Linux の端末

    のことを指します。
2. **以下のコマンドを実行する**<br>
    ```
    python
    ```
    > **エラー対策**<br>
    > 以下のようなエラーが起きた場合、次の手順を行うことで解決します。
    > ```
    > bash: command not found: python
    > ```
    > または
    > ```
    > bash: コマンド 'python' が見つかりません
    > ```
    > **解決方法**<br>
    > このエラーは ```python``` というコマンド名が見つからなかったことで発生します。Linux や最新の macOS では、Python を扱う際に ```python``` ではなく ```python3``` というコマンドを採用しています。<br>
    > つまり、```python3``` コマンドを代用すればお使いの環境で Python を使用できるようになります。よって以下のコマンドを実行してください。
    > ```
    > python3
    > ```

3. **確認**<br>
    CUi の表示が以下のようになったことを確認したら、次に進んでください。
    ```
    Python 3.8.2 (default, Apr  8 2021, 23:19:18) 
    [Clang 12.0.5 (clang-1205.0.22.9)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    ```

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
