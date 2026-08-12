import customtkinter as ctk
from alphapilot.portfolio.valuation_engine import (
    calculate_portfolio_valuation,
)
from alphapilot.database.transaction_repository import (
    get_all_transactions,
)

def main():
    app = ctk.CTk()

    def show_dashboard():
        heading.configure(text="Portfolio Dashboard")

        transaction_area.pack_forget()
        card.pack(
            fill="x",
            padx=40,
            pady=10,
        )

    def show_holdings():
        portfolio = calculate_portfolio_valuation(
            "HDFCBANK",
            845.00,
        )

        heading.configure(text="Holdings")
        transaction_area.pack_forget()

        card.pack(
            fill="x",
            padx=40,
            pady=10,
        )

        details.configure(
            text=(
                f"Symbol: {portfolio['symbol']}\n"
                f"Holding: {portfolio['holding']}\n"
                f"Average Cost: ₹{portfolio['average_cost']:,.2f}\n"
                f"Market Value: ₹{portfolio['market_value']:,.2f}\n"
                f"Unrealized Profit: ₹{portfolio['unrealized_profit']:,.2f}\n"
                f"Return: {portfolio['return_percentage']:.2f}%"
            )
        )

    def show_transactions():
        heading.configure(text="Transactions")

        # Hide portfolio card
        card.pack_forget()

        # Show transaction area
        transaction_area.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=10,
        )

        # Clear previous transaction widgets
        for widget in transaction_area.winfo_children():
            widget.destroy()

        transactions = get_all_transactions()

        headers = [
            "Date",
            "Symbol",
            "Action",
            "Quantity",
            "Price",
        ]

        column_widths = [140, 120, 100, 100, 140]

        for column, header in enumerate(headers):
            transaction_area.grid_columnconfigure(
                column,
                minsize=column_widths[column],
            )

            label = ctk.CTkLabel(
                transaction_area,
                text=header,
                font=("Arial", 16, "bold"),
            )

            label.grid(
                row=0,
                column=column,
                padx=15,
                pady=10,
                sticky="w",
            )

        for row, transaction in enumerate(transactions, start=1):

            price = float(transaction["price"])

            values = [
                str(transaction["transaction_date"]),
                str(transaction["symbol"]),
                str(transaction["action"]),
                str(transaction["quantity"]),
                f"₹{price:,.2f}",
            ]

            for column, value in enumerate(values):
                label = ctk.CTkLabel(
                    transaction_area,
                    text=value,
                    font=("Arial", 14),
                )

                label.grid(
                    row=row,
                    column=column,
                    padx=15,
                    pady=8,
                    sticky="w",
                )

    app.title("AlphaPilot")
    app.geometry("1100x700")

    # Main Layout
    sidebar = ctk.CTkFrame(app, width=200)
    sidebar.pack(side="left", fill="y", padx=10, pady=10)

    content = ctk.CTkFrame(app)
    content.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(0,10),
        pady=10,
    )

    # Sidebar
    logo = ctk.CTkLabel(
        sidebar,
        text = "🚀 Alpha Pilot",
        font=("Arial", 24, "bold"),
    )
    logo.pack(pady=(40,10))

    subtitle = ctk.CTkLabel(
        sidebar,
        text="Portfolio Assistant",
        font=("Arial", 14),
    )
    subtitle.pack(pady=(0,40))

    dashboard_button = ctk.CTkButton(
        sidebar,
        text = "📊 Dashboard",
        command = show_dashboard,
    )
    dashboard_button.pack(pady=10, padx=20)

    holdings_button = ctk.CTkButton(
        sidebar,
        text = "💰 Holdings",
        command=show_holdings,
    )
    holdings_button.pack(pady=10, padx=20)

    transactions_button = ctk.CTkButton(
        sidebar,
        text = "🧾 Transactions",
        command=show_transactions
    )
    transactions_button.pack(pady=10, padx=20)

    # Content
    heading = ctk.CTkLabel(
        content,
        text = "Portfolio Dashboard",
        font=("Arial", 30, "bold"),
    )
    heading.pack(anchor="w", padx=40, pady=(40,30))

    transaction_area = ctk.CTkScrollableFrame(
        content,
        width=700,
        height=400,
    )
    # transaction_area.pack(
    #     fill="both",
    #     expand=True,
    #     padx=40,
    #     pady=10,
    # )

    portfolio = calculate_portfolio_valuation(
        "HDFCBANK",
        845.00,
    )

    card = ctk.CTkFrame(content)
    card.pack(
        fill="x",
        padx=40,
        pady=10,
    )

    symbol = ctk.CTkLabel(
        card,
        text = portfolio['symbol'],
        font = ("Arial", 26, "bold"),
    )
    symbol.pack(anchor="w", padx=30, pady=(25,15))

    details = ctk.CTkLabel(
        card,
        text = (
            f"Holding: {portfolio['holding']}\n"
            f"Average Cost: ₹{portfolio['average_cost']:,.2f}\n"
            f"Market Value: ₹{portfolio['market_value']:,.2f}\n"
            f"Unrealized Profit: ₹{portfolio['unrealized_profit']:,.2f}\n"
            f"Return: {portfolio['return_percentage']:.2f}%"
        ),
        font=("Arial", 18),
        justify="left",
    )
    details.pack(anchor="w", padx=30, pady=(0, 30))

    # portfolio_label = ctk.CTkLabel(
    #     app,
    #     text=(
    #         f"Symbol: {portfolio['symbol']}\n"
    #         f"Holding: {portfolio['holding']}\n"
    #         f"Average Cost: {portfolio['average_cost']:.2f}\n"
    #         f"Marketing Value: {portfolio['market_value']:.2f}\n"
    #         f"Unrealized Profit: {portfolio['unrealized_profit']:.2f}\n"
    #         f"Return: {portfolio['return_percentage']:.2f}%"
    #     ),
    #     font=("Arial", 20),
    #     justify="left",
    # )
    # portfolio_label.pack(pady=30)

    app.mainloop()

if __name__ == "__main__":
    main()