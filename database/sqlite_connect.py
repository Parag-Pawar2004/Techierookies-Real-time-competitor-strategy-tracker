import sqlite3

# database file name
DB_NAME = "competitor_tracker.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    """Create the iphone_data table if it does not exist."""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS iphone_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price TEXT,
            site TEXT,
            scraped_at TEXT
        )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print(" Database and table created successfully.")
