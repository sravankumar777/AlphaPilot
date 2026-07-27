"""
Transaction module for AlphaPilot, which does addition or deletion of transactions
"""

from datetime import date
from alphapilot.database.transaction_repository import save_transaction

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
