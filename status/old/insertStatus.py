import mysql.connector

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
DROP TABLE IF EXISTS status;
""")
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(255)
);
""")
db_cursor.execute("""
insert into status (status) values 
('Available'),
('Not Available'),
('lost');

""")

db_connection.commit()  # 変更をコミット

db_cursor.close()
db_connection.close()

print('statusテーブル作成処理完了')