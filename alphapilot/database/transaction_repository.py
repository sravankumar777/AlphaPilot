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