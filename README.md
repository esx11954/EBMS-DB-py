# 仕様

### 発火スクリプト：createBookDB.py
各フォルダ内のpythonモジュールを呼び出してDBを作成する  
各モジュール単体でも実行可能なファイルをoldファイルに格納している  
同名のbatファイルはpython内のログが表示されないので使用しない  
books, user, historyテーブル作成時に生成されるデータはcsvフォルダに格納される  

### 発火方法：cmdから発火スクリプトのパスに移動し、
    python createBookDB.py
※DBのユーザ、パスワードは合わせる必要がある  
※必要なモジュールはpipでインストールする必要がある



### 必要モジュール：
faker  
```
pip install faker
```
mysql.connector  
```
pip install mysql-connector-python
```
