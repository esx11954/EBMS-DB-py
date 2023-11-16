import random
import faker
import csv
from datetime import datetime, timedelta
#import mysql.connector

def insert_books(db_cursor):
    fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

    # genres = ['小説', 'ビジネス', '科学', 'ミステリー', 'ファンタジー', '歴史', '自己啓発', '料理']
    sample_data = []
    now_date = datetime.now()
    
    eb = 'eb'
    mn = 1

    for _ in range(20):

        stock = random.randint(0, 2)
        status = 2 if stock == 0 else 1
        # tmp_date = datetime.now() - timedelta(days=random.randint(7, 365))
        # last_lending_date = tmp_date.strftime('%Y-%m-%d')
        # due_date = (tmp_date + timedelta(days=31)).strftime('%Y-%m-%d')
        
        book = {
            'manage_number': eb + str(mn).zfill(4),
            'book_master_id': random.randint(1, 5),
            'status': status,
            'reg_date': (now_date + timedelta(days=random.randint(-200, -5))).strftime('%Y-%m-%d')
        }

        mn += 1
        sample_data.append(book)
        #print(book)

    # 生成されたサンプルデータを表示
    #for book in sample_data:
    #   print(book)
    #


    csv_filename = './csv/sample_books_v3.csv'

    # CSVファイルにデータを書き込む
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['manage_number', 'book_master_id', 'status', 'reg_date']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()  # ヘッダーを書き込む

        for book in sample_data:
            """
            status = random.choice(['Available', 'Not Available'])
            last_lending_date = None if status == 'Available' else (datetime.now() - timedelta(days=random.randint(7, 365))).strftime('%Y-%m-%d')
            
            book['status'] = status
            book['last_lending_date'] = last_lending_date
            """
            writer.writerow(book)  # 各書籍のデータを行として書き込む

    print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')

    db_cursor.execute("""
    DROP TABLE IF EXISTS books;
    """)
    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        manage_number VARCHAR(255),
        book_master_id INT,
        status INT, 
        reg_date DATE
    );
    """)

    csv_filename = './csv/sample_books_v3.csv'

    # CSVファイルからデータを読み込み、データベースに挿入
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
        
            # データベースに挿入
            db_cursor.execute("""
            INSERT INTO books (manage_number, book_master_id, status, reg_date)
            VALUES (%s, %s, %s, %s)
            """, (
                row['manage_number'], row['book_master_id'], row['status'], row['reg_date']
            ))

    print('booksテーブル作成完了')
    