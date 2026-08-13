"""
Price provider for AlphaPilot.
"""

CURRENT_PRICES = {
    "BSE": 5200.00,
    "GENUSPOWER": 350.00,
    "HDFCBANK": 845.00,
    "INFY": 1500.00,
    "LT": 3800.00,
}

def get_current_price(symbol):
    """
    Return the current price for a stock symbol.
    """
    symbol = symbol.strip().upper()
    return CURRENT_PRICES.get(symbol)