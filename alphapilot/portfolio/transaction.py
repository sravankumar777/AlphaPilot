"""
Transaction module for AlphaPilot, which does addition or deletion of transactions
"""

from datetime import date
from alphapilot.database.transaction_repository import (
    save_transaction,
    get_transactions_by_symbol,
)

def add_transaction():
    """
    Collect transaction details from the user
    """

    print("\n----Add New Transaction---")

    symbol = input("Enter stock symbol: ").strip().upper()

    action = input("Enter action (BUY/SELL): ").strip().upper()
    if action not in ['BUY', 'SELL']:
        print("❌ Invalid action. Please enter BUY or SELL")
        return

    try:
        quantity = int(input("Enter quantity of stock: "))
    except ValueError:
        print("❌ Quantity must be a whole number")
        return
    if quantity <= 0:
        print("❌ Invalid Quantity. Please enter quantiy greater than zero")
        return

    try:
        price = float(input("Enter the price of each stock: "))
    except ValueError:
        print("❌ Price must be a whole number")
        return
    if price <= 0:
        print("❌ Invalid Price. Please enter valid price for the stock greater than zero")
        return

    print("\n Checking input...")
    print("✅ Validation successful!!!")
    
    investment = quantity * price
    transaction_date = date.today().isoformat()

    # print("\n Type for all transaction parameters")
    # print(type(symbol))
    # print(type(action))
    # print(type(quantity))
    # print(type(price))

    print("\n Transaction summary!!!")
    print(f"Symbol  :   {symbol}")
    print(f"Action  :   {action}")
    print(f"Quantity    :   {quantity}")
    print(f"Price   :   {price}")
    print(f"Investment value    :   ₹{investment:,.2f}")
    
    print("\n Saving transaction...")
    save_transaction(
        transaction_date,
        symbol,
        action,
        quantity,
        price,
    )

    print("\n Transaction captured successfully!!!")

def display_transactions(transactions):
    """
    Display transactions in a formatted table.
    """
    print("\n" + "=" * 70)
    print("                    TRANSACTION HISTORY")
    print("=" * 70)

    print(
        f"{'ID':<4}"
        f"{'DATE':<12}"
        f"{'SYMBOL':<15}"
        f"{'ACTION':<8}"
        f"{'QUANTITY':<10}"
        f"{'PRICE':<12}"
        f"{'INVESTMENT':>12}"
    )
    print("-" * 70)

    # print(type(transactions[0]))
    for transaction in transactions:
        transaction_id = transaction["id"]
        transaction_date = transaction["transaction_date"]
        symbol = transaction["symbol"]
        action = transaction["action"]
        quantity = transaction["quantity"]
        price = transaction["price"]
        brokerage = transaction["brokerage"]
        remarks = transaction["remarks"]
        investment = quantity * price

        print(
            f"{transaction_id:<4}"
            f"{transaction_date:<12}"
            f"{symbol:<15}"
            f"{action:<8}"
            f"{quantity:<10}"
            f"₹{price:<12,.2f}"
            f"₹{investment:>12,.2f}"
        )

    print("-" * 70)
    print(f"Total Transactions: {len(transactions)}")

def search_transaction():
    symbol = input("Enter Stock Symbol: ").strip().upper()

    transactions = get_transactions_by_symbol(symbol)

    if len(transactions) == 0:
        print(f"\n ❌ No transactions found for '{symbol}'.")
        return

    display_transactions(transactions)

def display_portfolio_summary(summary):
    """
    Display the portfolio summary.
    """
    print(">>>> display_portfolio_summary() called <<<<")
    print("\n" + "=" * 70)
    print(" " * 22 + "PORTFOLIO SUMMARY")
    print("=" * 70)

    print(
        f"{'SYMBOL':<15}"
        f"{'HOLDING':<10}"
        f"{'INVESTMENT':>15}"
    )

    for row in summary:
        symbol = row["symbol"]
        holding = row["holding"]
        investment = row["investment"]
        print(
            f"{symbol:<15}"
            f"{holding:<10}"
            f"{investment:>14,.2f}"
        )
        # print(row["symbol"])
        # print(row["holding"])
        # print(row["investment"])
        # print("-" * 20)

    print("-" * 70)
    print(f"Total Stocks : {len(summary)}")
    