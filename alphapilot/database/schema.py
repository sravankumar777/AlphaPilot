"""
Database schema for AlphaPilot
"""

from alphapilot.database.connection import get_database_connection

def create_transactions_table():
    """
    Create transactions table if it does not exists
    """

    connection = get_database_connection()

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            
            transaction_date TEXT NOT NULL,
            
            symbol TEXT NOT NULL,
            
            action TEXT NOT NULL,
            
            quantity INTEGER NOT NULL,
            
            price REAL NOT NULL,
            
            brokerage REAL DEFAULT 0,
            
            remarks TEXT
        );
    """)

    connection.commit()

    connection.close()

    print ("✅ Transactions table created successfully !!!")