import pymysql
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def store_to_database(student_message, corrected_grammar):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO agentai 
                (ID, StudentID, StudentMessage, CorrectedGrammar, CreatedOn, CreatedBy)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            data = (
                str(uuid.uuid4()),         # ID
                "001",                     # StudentID
                student_message,           # StudentMessage
                corrected_grammar,         # CorrectedGrammar
                datetime.now(),            # CreatedOn
                "admin"                    # CreatedBy
            )
            cursor.execute(sql, data)
            connection.commit()
        print("[Database] Grammar correction stored successfully.")
    except Exception as e:
        print("[Database] Error storing data:", e)
    finally:
        connection.close()
