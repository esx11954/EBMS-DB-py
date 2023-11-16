import random
import faker
import csv
from datetime import datetime, timedelta
import mysql.connector


def create_user(db_cursor):
    fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

    sample_data = []
    now_date = datetime.now()

    men = ['深澤', '小林', '林', '安井', '荻原', '山田', '小宮山', '新渡戸', '仁科',
           '青木', '石崎', '石田', '太田', '大手', '鴇巣', '泊', '尾久', '本領', '末永']
    for _ in range(30):

        note = ''
        stock = random.randint(0, 2)
        if stock == 1:
            note = fake.text()
        
        user = {
            'last_name': fake.last_name(),
            'first_name': fake.first_name(),
            'birth': fake.date_of_birth(minimum_age=16, maximum_age=100).strftime('%Y-%m-%d'),
            'sex': random.choice(['M', 'F']),
            'tel': fake.phone_number(),
            'mail': fake.email(),
            'address': fake.address().replace("\n", " "),
            'in_charge': random.randint(1, 19),
            'note': note,
            'reg_date': (now_date + timedelta(days=random.randint(-400, -100))).strftime('%Y-%m-%d')
        }
        sample_data.append(user)
    #    print(user)

    # 生成されたサンプルデータを表示
    # for book in sample_data:
    #   print(book)
    #

    csv_filename = './csv/sample_user.csv'

    # CSVファイルにデータを書き込む
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['last_name', 'first_name', 'birth',
                      'sex', 'tel', 'mail', 'address', 'in_charge', 'note', 'reg_date']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()  # ヘッダーを書き込む

        for book in sample_data:

            writer.writerow(book)  # 各書籍のデータを行として書き込む

    print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')

    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    DROP TABLE IF EXISTS user_master;
    """)
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_master (
        id INT AUTO_INCREMENT PRIMARY KEY,
        last_name VARCHAR(255),
        first_name VARCHAR(255),
        birth DATE,
        sex VARCHAR(10),
        tel VARCHAR(50),
        mail VARCHAR(255),
        address VARCHAR(1000),
        in_charge INT,
        note VARCHAR(1000),
        reg_date DATE
    );
    """)

    csv_filename = './csv/sample_user.csv'

    # CSVファイルからデータを読み込み、データベースに挿入
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:

            #last_lending_date = None if row['last_lending_date'] == '' else datetime.strptime(row['last_lending_date'], '%Y-%m-%d').date()
            # データベースに挿入
            db_cursor.execute("""
            INSERT INTO user_master (last_name, first_name, birth, sex, tel, mail, address, in_charge, note, reg_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row['last_name'], row['first_name'], row['birth'], (
                    row['sex']),
                row['tel'], row['mail'], row['address'], row['in_charge'], row['note'], row['reg_date']
            ))

    print('userテーブル作成完了')
