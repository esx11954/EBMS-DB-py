import mysql.connector

def create_tag_master(db_cursor):
    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    DROP TABLE IF EXISTS tag_master;
    """)
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS tag_master (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tag_name VARCHAR(255)
    );
    """)
    db_cursor.execute("""
    insert into tag_master (tag_name) values 
    ('インフラ'),
    ('サーバ'),
    ('開発'),
    ('LINUC'),
    ('LPIC'),
    ('CCNA'),
    ('CCNP'),
    ('ITパスポート'),
    ('基本情報技術者'),
    ('応用情報技術者'),
    ('AWS'),
    ('Oracle'),
    ('DB'),
    ('Java'),
    ('MOS'),
    ('Excel'),
    ('VBA')
    ;
    """)

    print('tag_masterテーブル作成完了')