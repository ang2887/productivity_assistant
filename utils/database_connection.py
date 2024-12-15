# database_connection.py 6

import os
from dotenv import load_dotenv
import psycopg2

def get_db_connection():
    print("Connecting to the database...")
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    print("Database connection established.")
    return conn, conn.cursor()

# Load environment variables
load_dotenv()

database_url = (
    os.getenv('DATABASE_URL') or
    os.getenv('DATABASE_URL_LOCAL') or
    os.getenv('DATABASE_URL_DOCKER')
)

if not database_url:
    raise ValueError('No database URL found')
print(f"Using database URL: {database_url}")

os.environ['DATABASE_URL'] = database_url

# Test the connection
try:
    conn, cursor = get_db_connection()
    cursor.execute('SELECT 1;')
    print("Database connected successfully")
    conn.close()
except Exception as e:
    print(f"Database connection failed: {e}")

    