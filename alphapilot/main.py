"""
Main entry point for AlphaPilot
"""

from alphapilot.database.connection import get_database_connection
from alphapilot.database.schema import create_transactions_table
from alphapilot.database.transaction_repository import (
    get_all_transactions,
    get_portfolio_summary,
)
from alphapilot.portfolio.transaction import (
    add_transaction,
    display_transactions,
    search_transaction,
    display_portfolio_summary,
)
from alphapilot.portfolio.portfolio_engine import calculate_portfolio
from alphapilot.menu import display_menu

def main():
    """
    Start AlphaPilot
    """

    connection = get_database_connection()

    print("✅ Successfully connected to AlphaPilot Database!!!")

    connection.close()

    create_transactions_table()

    while True:
        choice = display_menu()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            transactions = get_all_transactions()
            display_transactions(transactions)
        elif choice == "3":
            search_transaction()
        elif choice == "4":
            # summary = get_portfolio_summary()
            # display_portfolio_summary(summary)
            symbol = input("Enter a symbol: ").strip().upper()
            calculate_portfolio(symbol)
        elif choice == "5":
            print("Thank you for using AlphaPilot")
            break
        else:
            print("❌ Invalid Option Selected")

    print("👋 Database connection closed.")

if __name__ == "__main__":
    main()