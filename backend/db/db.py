# DB
import psycopg2
from psycopg2.extensions import connection, cursor
from typing import Tuple

from config.loader import config, ConfigSchema

def connect() -> Tuple[connection, cursor]:
    try:
        # Create connection obj
        conn = psycopg2.connect(
            dbname=config[ConfigSchema.DATABASE][ConfigSchema.DBNAME],
            user=config[ConfigSchema.DATABASE][ConfigSchema.DB_USERNAME],
            password=config[ConfigSchema.DATABASE][ConfigSchema.DB_PASSWORD],
            host=config[ConfigSchema.DATABASE][ConfigSchema.DB_HOST],
            port=config[ConfigSchema.DATABASE][ConfigSchema.DB_PORT]
        )
        
        # Create cursor
        cursor = conn.cursor()
        
        # Return connection
        return conn, cursor
    except Exception as error:
        print(f'Error: failed to connect to PostgreSQL\n{error}')

def disconnect(conn: connection, cursor: cursor) -> None:
    cursor.close()
    conn.close()
