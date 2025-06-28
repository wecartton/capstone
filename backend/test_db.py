from flask import Flask
from sqlalchemy import text
from models.user import db
from config import get_config

app = Flask(__name__)
app.config.from_object(get_config())

print(f"Attempting to connect to: {app.config['SQLALCHEMY_DATABASE_URI']}")

db.init_app(app)

with app.app_context():
    try:
        # Try a simple query using text()
        result = db.session.execute(text('SELECT 1')).fetchone()
        print(f"Database connection successful! Test query result: {result}")
        
        # Check for users table
        from models.user import User
        user_count = User.query.count()
        print(f"Users table exists. User count: {user_count}")
        
        # List all tables
        tables = db.session.execute(text('SHOW TABLES')).fetchall()
        print("Database tables:")
        for table in tables:
            print(f"- {table[0]}")
            
    except Exception as e:
        print(f"Database connection failed: {str(e)}")