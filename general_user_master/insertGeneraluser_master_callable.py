import mysql.connector


def create_general_user_master(db_cursor):
    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    DROP TABLE IF EXISTS general_user_master;
    """)
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS general_user_master (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(255)
    );
    """)
    db_cursor.execute("""
    insert into general_user_master (user_name) values 
    ('深澤'),
    ('小林'),
    ('林'),
    ('安井'),
    ('荻原'),
    ('山田'),
    ('小宮山'),
    ('新渡戸'),
    ('仁科'),
    ('青木'),
    ('石崎'),
    ('石田'),
    ('太田'),
    ('大手'),
    ('鴇巣'),
    ('泊'),
    ('尾久'),
    ('本領'),
    ('末永')
    ;
    """)

    print('general_user_masterテーブル作成完了')
