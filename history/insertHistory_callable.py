import random
import faker
import csv
from datetime import datetime, timedelta
import mysql.connector

def create_history(db_cursor):
    fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

    sample_data = []

    date_string = "2022-05-29"
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    dtobj = dt.date()
    #print(dtobj)
    #print(dtobj + timedelta(days=random.randint(0, 3)))

    for _ in range(500):

        returned = random.choice(['T', 'F'])
        due_date = (dtobj + timedelta(days=31))
        returned_date = 'NULL' if returned == 'F' else (due_date + timedelta(days=random.randint(-7, 7))).strftime('%Y-%m-%d')
        
        data = {
            'book_id': random.randint(1, 5),
            'user_id': random.randint(1, 30),
            'checkout_date': dtobj.strftime('%Y-%m-%d'),
            'due_date': due_date.strftime('%Y-%m-%d'),
            'return_date': returned_date,
            'returned': returned
        }
        sample_data.append(data)
    #    print(data)
        dtobj = (dtobj + timedelta(days=random.randint(0, 1)))

    # 生成されたサンプルデータを表示
    #for book in sample_data:
    #   print(book)
    #


    csv_filename = './csv/sample_history.csv'

    # CSVファイルにデータを書き込む
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['book_id', 'user_id', 'checkout_date', 'due_date', 'return_date', 'returned']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()  # ヘッダーを書き込む

        for book in sample_data:

            writer.writerow(book)  # 各書籍のデータを行として書き込む

    print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')


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

    csv_filename = './csv/sample_history.csv'

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

    print('historyテーブル作成完了')