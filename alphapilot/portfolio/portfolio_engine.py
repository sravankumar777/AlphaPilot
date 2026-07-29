"""
Portfolio Calculation engine for AlphaPilot.
"""

from alphapilot.database.transaction_repository import get_transactions_by_symbol

print(get_transactions_by_symbol.__module__)
print(get_transactions_by_symbol.__defaults__)

def calculate_portfolio(symbol):
    """
    Calculate portfolio details for a stock.
    """

    holding = 0
    total_buy_quantity = 0
    total_buy_value = 0.0
    totat_sell_quantity = 0
    average_cost = 0.0
    investment_value = 0.0
    
    transactions = get_transactions_by_symbol(symbol, newest_first=False)

    # print("\n" + "=" * 60)
    # print(f"Portfolio Engine - {symbol}")
    # print("=" * 60)
    # print(
    #     f"{'Date':<15}"
    #     f"{'Action':<10}"
    #     f"{'Quantity':>10}"
    #     f"{'Price':>12}"
    # )
    print("-" * 60)
    for transaction in transactions:
        action = transaction['action']
        quantity = transaction['quantity']
        price = transaction['price']

        if action == "BUY":
            holding += quantity
            total_buy_quantity += quantity
            total_buy_value += quantity * price
        elif action == "SELL":
            holding -= quantity
        # print(
        #     f"{transaction['transaction_date']:<15}"
        #     f"{transaction['action']:<10}"
        #     f"{transaction['quantity']:>10}"
        #     f"{transaction['price']:>12,.2f}"
        # )
        average_cost = (
            total_buy_value / total_buy_quantity
            if total_buy_quantity > 0
            else 0.0
        )

        investment_value = holding * average_cost
    
    # print("\n Portfolio Calculations")
    # print("-" * 40)
    # print(f"Holding         :   {holding}")
    # print(f"Buy Quantity    :   {total_buy_quantity}")
    # print(f"Buy Value       :   {total_buy_value:,.2f}")
    # print(f"Average Cost    :   {average_cost:,.2f}")
    # print("-" * 40)

    return {
        "symbol": symbol,
        "holding": holding,
        "average_cost": average_cost,
        "total_buy_quantity": total_buy_quantity,
        "total_buy_value": total_buy_value, 
    }