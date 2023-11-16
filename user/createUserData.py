import random
import faker
import csv
from datetime import datetime, timedelta



fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

sample_data = []

for _ in range(250):

    stock = random.randint(0, 2)
    lending_status = 'Not Available' if stock == 0 else 'Available'
    tmp_date = datetime.now() - timedelta(days=random.randint(7, 365))
    last_lending_date = tmp_date.strftime('%Y-%m-%d')
    due_date = (tmp_date + timedelta(days=31)).strftime('%Y-%m-%d')
    
    user = {
        'last_name': fake.last_name(),
        'first_name': fake.first_name(),
        'birth': fake.date_of_birth(minimum_age=16, maximum_age=100).strftime('%Y-%m-%d'),
        'sex': random.choice(['M', 'F']),
        'tel': fake.phone_number(),
        'mail': fake.email(),
        'address': fake.address().replace("\n", " ")
        #'due_date': due_date
    }
    sample_data.append(user)
#    print(user)

# 生成されたサンプルデータを表示
#for book in sample_data:
#   print(book)
#


csv_filename = 'sample_user.csv'

# CSVファイルにデータを書き込む
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['last_name', 'first_name', 'birth', 'sex', 'tel', 'mail', 'address']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # ヘッダーを書き込む

    for book in sample_data:

        writer.writerow(book)  # 各書籍のデータを行として書き込む

print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')
