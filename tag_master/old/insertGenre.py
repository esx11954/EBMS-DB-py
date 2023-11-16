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
DROP TABLE IF EXISTS genre;
""")
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS genre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genre VARCHAR(255)
);
""")
db_cursor.execute("""
insert into genre (genre) values 
('小説'),
('ビジネス'),
('科学'),
('ミステリー'),
('ファンタジー'),
('歴史'),
('自己啓発'),
('料理')
;
""")

db_connection.commit()  # 変更をコミット

db_cursor.close()
db_connection.close()

print('genreテーブル作成処理完了')