import os
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    db_server = os.getenv("DB_SERVER", "127.0.0.1")
    db_user = os.getenv("DB_USER", None)
    db_pass = os.getenv("DB_PASSORD", None)
    try:
        if db_pass:
            conn = psycopg2.connect("host={} dbname=sparkifydb user={}, password={}".format(db_server, db_user, db_pass))
        else:
            conn = psycopg2.connect("host={} dbname=sparkifydb user={}".format(db_server, db_user))
        conn.set_session(autocommit=True)
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    if conn is not None:
        conn.close()
    
    # connect to sparkify database
    try:
        if db_pass:
            conn = psycopg2.connect("host={} dbname=sparkifydb user={} password={}".format(db_server, db_user, db_pass))
        else:
            conn = psycopg2.connect("host={} dbname=sparkifydb user={}".format(db_server, db_user))
        cur = conn.cursor()
        return cur, conn
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    cur, conn = create_database()
    try:
        drop_tables(cur, conn)
        create_tables(cur, conn)
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
