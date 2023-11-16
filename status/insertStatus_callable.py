import mysql.connector

def create_status(db_cursor):
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

    print('statusテーブル作成完了')