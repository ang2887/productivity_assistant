# database_connection.py 4

import os
from dotenv import load_dotenv
import psycopg2
import logging 


logging.basicConfig(level=logging.DEBUG)  # Add this at the top

def get_db_connection():
    logging.debug("Attempting to connect to the database...")
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    logging.debug("Database connection established.")
    return conn, conn.cursor()

load_dotenv()

database_url = (
    os.getenv('DATABASE_URL') or
    os.getenv('DATABASE_URL_LOCAL') or
    os.getenv('DATABASE_URL_DOCKER')
)

if not database_url:
    raise ValueError('no database url found')
print(f'using database url: {database_url}')

os.environ['DATABASE_URL'] = database_url

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn, conn.cursor()

try:
    conn, cursor = get_db_connection()
    cursor.execute('SELECT 1;')
    print('database connected successfully')
    conn.close()
except Exception as e:
    print(f'database connection failed: {e}')    
