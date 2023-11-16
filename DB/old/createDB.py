import mysql.connector

cnx = None

cnx = mysql.connector.connect(
    user='root',  # ユーザー名
    password='root', 
    host='localhost'  # ホスト名(IPアドレス）
)

cursor = cnx.cursor()

cursor.execute("DROP DATABASE IF EXISTS bookdb;")
cursor.execute("CREATE DATABASE bookdb;")
cursor.close()

print('bookdbデータベース作成完了')
