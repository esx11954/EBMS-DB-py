#import mysql.connector

def create_book_DB(cursor):
    cursor.execute("DROP DATABASE IF EXISTS EBMS;")
    cursor.execute("CREATE DATABASE EBMS;")
    cursor.execute("use EBMS;")
    # cursor.close()

    print('EBMSデータベース作成完了')
