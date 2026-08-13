from alphapilot.portfolio.valuation_engine import (
    calculate_portfolio_valuation,
)

def test_hdfcbank_portfolio_validation():
    portfolio = calculate_portfolio_valuation(
        "HDFCBANK",
        845.00,
    )

    assert portfolio["symbol"] == "HDFCBANK"
    assert portfolio["holding"] == 28
    assert portfolio["total_buy_quantity"] == 30
    assert portfolio["market_value"] == 23660.00
    assert round(portfolio["unrealized_profit"], 2) == 1353.33
    assert round(portfolio["return_percentage"], 2) == 6.07