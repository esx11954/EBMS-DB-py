import random
import faker
import csv
from datetime import datetime, timedelta



fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

sample_data = []

date_string = "2022-05-29"
dt = datetime.strptime(date_string, "%Y-%m-%d")
dtobj = dt.date()
#print(dtobj)
#print(dtobj + timedelta(days=random.randint(0, 3)))

for _ in range(500):

    returned = random.choice(['T', 'F']);
    due_date = (dtobj + timedelta(days=31))
    returned_date = 'NULL' if returned == 'F' else (due_date + timedelta(days=random.randint(-7, 7))).strftime('%Y-%m-%d')
    
    data = {
        'book_id': random.randint(1, 1000),
        'user_id': random.randint(1, 250),
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


csv_filename = 'sample_history.csv'

# CSVファイルにデータを書き込む
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['book_id', 'user_id', 'checkout_date', 'due_date', 'return_date', 'returned']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # ヘッダーを書き込む

    for book in sample_data:

        writer.writerow(book)  # 各書籍のデータを行として書き込む

print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')
