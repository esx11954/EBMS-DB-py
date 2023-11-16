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

db_cursor.execute("""
DROP TABLE IF EXISTS books;
""")
# テーブルが存在しない場合は作成
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre INT,
    publication_year INT,
    isbn VARCHAR(50),
    stock INT,
    lending_status INT
);
""")

csv_filename = 'sample_books_v2.csv'

# CSVファイルからデータを読み込み、データベースに挿入
with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
    
        #last_lending_date = None if row['last_lending_date'] == '' else datetime.strptime(row['last_lending_date'], '%Y-%m-%d').date()
        # データベースに挿入
        db_cursor.execute("""
        INSERT INTO books (title, author, genre, publication_year, isbn, stock, lending_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['title'], row['author'], row['genre'], int(row['publication_year']),
            row['isbn'], row['stock'], row['lending_status']
        ))

        db_connection.commit()  # 変更をコミット

db_cursor.close()
db_connection.close()

print('処理完了')