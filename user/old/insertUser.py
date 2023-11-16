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
DROP TABLE IF EXISTS user;
""")
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    birth DATE,
    sex VARCHAR(10),
    tel VARCHAR(50),
    mail VARCHAR(255),
    address VARCHAR(1000)
);
""")

csv_filename = 'sample_user.csv'

# CSVファイルからデータを読み込み、データベースに挿入
with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
    
        #last_lending_date = None if row['last_lending_date'] == '' else datetime.strptime(row['last_lending_date'], '%Y-%m-%d').date()
        # データベースに挿入
        db_cursor.execute("""
        INSERT INTO user (last_name, first_name, birth, sex, tel, mail, address)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['last_name'], row['first_name'], row['birth'], (row['sex']),
            row['tel'], row['mail'], row['address']
        ))

        db_connection.commit()  # 変更をコミット

db_cursor.close()
db_connection.close()

print('処理完了')