import mysql.connector
from DB import createDB_callable
from book_master import insertBook_master_callable
from user import insertUser_callable
from history import insertHistory_callable
from tag_master import insertTag_master_callable
from status import insertStatus_callable
from book import insertBooks_callable
from general_user_master import insertGeneraluser_master_callable
from login import insertLogin

if __name__ == '__main__':
    print('処理開始')
    cnx = None
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='root', 
        host='localhost'  # ホスト名(IPアドレス）
    )

    border = '-----------------------------------------------------------------'
    cursor = cnx.cursor()
    createDB_callable.create_book_DB(cursor)
    print(border)
    insertBook_master_callable.insert_book_master(cursor)
    print(border)
    insertGeneraluser_master_callable.create_general_user_master(cursor)
    print(border)
    insertTag_master_callable.create_tag_master(cursor)
    print(border)
    insertBooks_callable.insert_books(cursor)
    print(border)
    insertUser_callable.create_user(cursor)
    print(border)
    insertHistory_callable.create_history(cursor)
    print(border)
    insertStatus_callable.create_status(cursor)
    print(border)
    insertLogin.create_login_table(cursor)
    print(border)

    
    
    cnx.commit()
    cursor.close()
    cnx.close()
    print('EBMS作成完了')