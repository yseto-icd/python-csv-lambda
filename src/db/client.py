import os
import sys
import pymysql

    
def connect():
    user = os.environ['DB_USER']
    password = os.environ['DB_PASSWORD']
    uri = os.environ['DB_URI']
    try:
        print('connect to db')
        conn = pymysql.connect(host=uri, user=user, passwd=password, db='test', connect_timeout=5)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        raise e

    return conn

def find(conn):
    with conn.cursor() as cur:
        cur.execute("select * from test")
        result = cur.fetchall()
        for data in result:
            print(data)

def insert(conn, target_list):
    with conn.cursor() as cur:
        for data in target_list:
            in_id = data["id"]
            in_name = data[" name"]
            cur.execute(f"insert into test (id, name) values({in_id}, '{in_name}')")
        conn.commit()
        cur.execute("select * from test")
        for row in cur:
            print(row)
    conn.commit()

