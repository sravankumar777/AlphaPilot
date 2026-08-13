from alphapilot.portfolio.portfolio_engine import calculate_portfolio

def calculate_portfolio_valuation(symbol, current_price):
    """
    Calculation portfolio valuation for a stock.
    """
    portfolio = calculate_portfolio(symbol)

    # holding = portfolio['holding']
    # average_cost = portfolio['average_cost']

    investment_value = portfolio["holding"] * portfolio["average_cost"]

    portfolio["investment_value"] = investment_value
    portfolio["current_price"] = current_price
    portfolio["market_value"] = portfolio["holding"] * current_price
    portfolio["unrealized_profit"] = portfolio["market_value"] - portfolio["investment_value"]

    return_percentage = (
        (portfolio["unrealized_profit"]/portfolio["investment_value"]) * 100
        if portfolio["investment_value"] > 0
        else 0.0
    )
    portfolio["return_percentage"] = return_percentage

    return portfolio