import random
import faker
import csv
from datetime import datetime, timedelta
#import mysql.connector

def insert_book_master(db_cursor):
    fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

    sample_data = []
    now_date = datetime.now()
    
    image_url = ['lpic1.jpg', 'lpic2.jpg', 'ccna.jpg', 'ccnp.jpg', 'java', 'it_pass.jpg', 'oracle.jpg', 'mos.jpg']
    #'genre': random.choice(image_url),

    for _ in range(5):

        json = '{\"tags\": ['
        comma = ','
        end = ']}'
        count = random.randint(1, 5)
        for _ in range(count):
            tagId = random.randint(1, 10)
            json += str(tagId)
            if(_ + 1 != count):
                json += comma
            
        json += end
        
        stock = random.randint(0, 2)
        status = 2 if stock == 0 else 1
        
        book = {
            'title': fake.catch_phrase(),
            'author': fake.name(),
            'tags': json,
            'stock': stock,
            'status': status,
            'image_url': random.choice(image_url)
        }
        sample_data.append(book)
        #print(book)

    # 生成されたサンプルデータを表示
    #for book in sample_data:
    #   print(book)
    #


    csv_filename = './csv/sample_book_master_v2.csv'

    # CSVファイルにデータを書き込む
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['title', 'author', 'tags', 'stock', 'status', 'image_url']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()  # ヘッダーを書き込む

        for book in sample_data:
            writer.writerow(book)  # 各書籍のデータを行として書き込む

    print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')

    db_cursor.execute("""
    DROP TABLE IF EXISTS book_master;
    """)
    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS book_master (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        tags VARCHAR(255),
        stock INT,
        status INT, 
        image_url VARCHAR(255)
    );
    """)

    csv_filename = './csv/sample_book_master_v2.csv'

    # CSVファイルからデータを読み込み、データベースに挿入
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
        
            # データベースに挿入
            db_cursor.execute("""
            INSERT INTO book_master (title, author, tags, stock, status, image_url)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['title'], row['author'], row['tags'],
                row['stock'], row['status'], row['image_url']
            ))

    print('book_masterテーブル作成完了')
    