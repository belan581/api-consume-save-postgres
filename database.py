import json
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(database=os.getenv('POSTGRES_DB'),
                        host=os.getenv('POSTGREST_HOST'),
                        user=os.getenv('POSTGRES_USER'),
                        password=os.getenv('POSTGRES_PASSWORD'),
                        port=os.getenv('5432'))

conn.autocommit = True
cursor = conn.cursor()

def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS ARTICLES(
            source json NULL,\
            author character varying(200) NULL,\
            title character varying(250) NULL,\
            description text NULL,\
            url character varying(300) NULL,\
            urlToImage character varying(350) NULL,\
            publishedAt date NULL,\
            content text NULL);'''
    
    cursor.execute(sql)

def insert_data(data):
    query = """ insert into ARTICLES\
                select * from json_populate_recordset(NULL::ARTICLES, %s) """
    cursor.execute(query, (json.dumps(data, indent=2),))
    conn.commit()

def close_connection():
    conn.close()
    print("Connection was closed correctly!")