# import pymysql.cursors
from dotenv import dotenv_values

import psycopg2.extras

config = dotenv_values(".env")
class DBConnection:
    conn = psycopg2.connect(
        host=config.get('HOST'),
        database=config.get('DATABASE'),
        user=config.get('USER'),
        password=config.get('PASSWORD'),
        cursor_factory=psycopg2.extras.RealDictCursor
    )
    print("database connected")
    cursor = conn.cursor()

"""HOST=localhost
USER=postgres
PASSWORD=root
DATABASE=classroom
PORT=5432"""