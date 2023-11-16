import random
import faker
import csv
from datetime import datetime, timedelta
import mysql.connector


fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

# MySQLデータベースへの接続を確立
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bookdb"
)
db_cursor = db_connection.cursor()

# テーブルが存在しない場合は作成
db_cursor.execute("""
DROP TABLE IF EXISTS history;
""")
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user_id INT,
    checkout_date DATE,
    due_date DATE,
    return_date DATE,
    returned VARCHAR(10)
);
""")

csv_filename = 'sample_history.csv'

# CSVファイルからデータを読み込み、データベースに挿入
with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
    
        if row['returned'] == 'T':
        # データベースに挿入
            db_cursor.execute("""
            INSERT INTO history (book_id, user_id, checkout_date, due_date, return_date, returned)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['book_id'], row['user_id'], row['checkout_date'], (row['due_date']),
                row['return_date'], row['returned']
            ))
        else:
            db_cursor.execute("""
            INSERT INTO history (book_id, user_id, checkout_date, due_date, returned)
            VALUES (%s, %s, %s, %s, %s)
            """, (
                row['book_id'], row['user_id'], row['checkout_date'], (row['due_date']), row['returned']
            ))
            

        db_connection.commit()  # 変更をコミット

db_cursor.close()
db_connection.close()

print('処理完了')