"""
Main entry point for AlphaPilot
"""

from alphapilot.database.connection import get_database_connection
from alphapilot.database.schema import create_transactions_table
from alphapilot.portfolio.transaction import add_transaction

def main():
    """
    Start AlphaPilot
    """

    connection = get_database_connection()

    print("✅ Successfully connected to AlphaPilot Database!!!")

    connection.close()

    create_transactions_table()

    add_transaction()

    print("👋 Database connection closed.")

if __name__ == "__main__":
    main()