"""
Database operation for transactions
"""

from alphapilot.database.connection import get_database_connection

def save_transaction(
    transaction_date,
    symbol,
    action,
    quantity,
    price,
    brokerage=0,
    remarks=""
):
    """
    Save a transaction into the database.
    """

    connection = get_database_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO transactions (
            transaction_date, 
            symbol,
            action,
            quantity,
            price,
            brokerage,
            remarks
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            transaction_date,
            symbol,
            action,
            quantity,
            price,
            brokerage,
            remarks
        ),
    )

    connection.commit()
    connection.close()

    print("✅ Transaction saved successfully!!!")

def get_all_transactions():
    """
    Retrieve all transactions from the database
    """

    connection = get_database_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * from transactions;
        """)

        transactions = cursor.fetchall()

        connection.close()

        return transactions
    except Exception as error:
        print(f"❌ Error retrieving transactions: {error}")
        return []

def get_transactions_by_symbol(symbol, newest_first=True):
    """
    Retrieve all transactions for a given stock symbol.

    newest_first=True --> Search screen
    newest_first=False --> Portfolio Engine
    """

    connection = get_database_connection()
    order_by = "DESC" if newest_first else "ASC"

    try:
        cursor = connection.cursor()
        query = f"""
            SELECT *
            FROM transactions
            WHERE symbol = ?
            ORDER BY transaction_date {order_by}, id {order_by}
        """
        cursor.execute(query, (symbol,))

        transactions = cursor.fetchall()

        return transactions
    except Exception as error:
        print(f"❌ Error retrieving transactions: {error}")
        return []
    finally:
        connection.close()

def get_all_symbols():
    """
    Retrieve all unique stock symbols from transactions.
    """
    connection = get_database_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT DISTINCT symbol
            FROM transactions
            ORDER BY symbol
            """
        )
        symbols = cursor.fetchall()
        return [row["symbol"] for row in symbols]
    except Exception as error:
        print(f"❌ Error retreiving symbols: {error}")
        return []
    finally:
        connection.close()

def get_portfolio_summary():
    """
    Retrieve the portfolio summary grouped by stock symbol.
    """

    connection = get_database_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT
                symbol, 
                SUM(
                    CASE
                        WHEN action = 'BUY' THEN quantity 
                        WHEN action = 'SELL' THEN -quantity
                    END
                ) AS holding,
                SUM(quantity * price) AS investment
            FROM transactions
            GROUP BY SYMBOL
            ORDER BY SYMBOL;
            """,
        )

        transactions = cursor.fetchall()

        return transactions
    except Exception as error:
        print(f"❌ Error retrieveing portfolio summary: {error}.")
        return []
    finally:
        connection.close()