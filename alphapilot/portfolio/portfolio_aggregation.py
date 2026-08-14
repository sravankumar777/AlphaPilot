"""
Portfolio Aggregation Engine for AlphaPilot
"""

from alphapilot.database.transaction_repository import get_all_symbols
from alphapilot.portfolio.portfolio_engine import calculate_portfolio
from alphapilot.market.price_provider import get_current_price

def calculate_all_portfolios():
    """
    Calculate portfolio details for all stock symbols.
    """
    symbols = get_all_symbols()

    portfolios = []
    for symbol in symbols:
        portfolio = calculate_portfolio(symbol)

        if portfolio['holding'] > 0:
            portfolios.append(portfolio)

    return portfolios

def calculate_total_investment():
    """
    Calculate total investment across all open positions.
    """
    portfolios = calculate_all_portfolios()

    total_invesment = sum(
        portfolio['holding'] * portfolio['average_cost']
        for portfolio in portfolios
    )

    return total_invesment

def calculate_market_values():
    """
    Calculate market value for all open portfolio positions.
    """

    portfolios = calculate_all_portfolios()

    for portfolio in portfolios:
        symbol = portfolio['symbol']
        current_price = get_current_price(symbol)

        portfolio['current_price'] = current_price
        portfolio['market_value'] = (
            portfolio['holding'] * current_price
        )
        portfolio["investment_value"] = (
            portfolio["holding"] * portfolio["average_cost"]
        )
        portfolio["unrealized_profit"] = (
            portfolio["market_value"] 
            - portfolio["investment_value"]
        )

    return portfolios

def calculate_total_market_value():
    """
    Calculate total market value of all open positions.
    """

    portfolios = calculate_market_values()

    total_market_value = sum (
        portfolio["market_value"]
        for portfolio in portfolios
    )

    return total_market_value

def calculate_total_unrealized_profit():
    """
    Calculate total unrealized profit or loss.
    """

    portfolios = calculate_market_values()
    total_profit = 0.0

    for portfolio in portfolios:
        investment_value = (
            portfolio["holding"] * portfolio["average_cost"]
        )

        total_profit += (
            portfolio["market_value"] - investment_value
        )
    return total_profit

def calculate_total_return():
    """
    Calculate overall portfolio return percentage.
    """

    total_investment = calculate_total_investment()
    total_profit = calculate_total_unrealized_profit()

    if total_investment <= 0:
        return 0.0

    return (total_profit / total_investment ) * 100