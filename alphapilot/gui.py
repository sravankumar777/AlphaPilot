import customtkinter as ctk
from alphapilot.portfolio.valuation_engine import (
    calculate_portfolio_valuation,
)
from alphapilot.portfolio.portfolio_aggregation import (
    calculate_all_portfolios,
    calculate_total_investment,
    calculate_total_market_value,
    calculate_total_unrealized_profit,
    calculate_total_return,
    calculate_market_values,
)
from alphapilot.database.transaction_repository import (
    get_all_transactions,
)

def create_summary_card(parent, column, title, value):
    card = ctk.CTkFrame(parent)

    card.grid(
        row=0,
        column=column,
        padx=8,
        pady=10,
        sticky="nsew",
    )
    ctk.CTkLabel(
        card,
        text=title,
        font=("Arial", 14),
    ).pack(pady=(20,5))
    ctk.CTkLabel(
        card,
        text=value,
        font=("Arial", 22, "bold"),
    ).pack(pady=(0,20))

def main():
    app = ctk.CTk()

    def show_dashboard():
        heading.configure(text="Portfolio Dashboard")
        holdings_area.pack_forget()
        transaction_area.pack_forget()
        summary_frame.pack(
            fill="x",
            padx=40,
            pady=10,
        )

    def show_holdings():
        heading.configure(text="Holdings")
        summary_frame.pack_forget()
        transaction_area.pack_forget()

        holdings_area.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=10,
        )

        for widget in holdings_area.winfo_children():
            widget.destroy()

        portfolios = calculate_market_values()

        headers = [
            "Symbol",
            "Holding",
            "Average Cost",
            "Market Price",
            "Market Value",
            "P/L",
        ]

        column_widths = [130, 100, 150, 150, 160, 150]

        for column, header in enumerate(headers):
            holdings_area.grid_columnconfigure(
                column,
                minsize=column_widths[column],
                weight=1,
            )

            label = ctk.CTkLabel(
                holdings_area,
                text=header,
                font=("Arial", 15, "bold"),
            )

            label.grid(
                row=0,
                column=column,
                padx=15,
                pady=10,
                sticky="w",
            )

        for row, portfolio in enumerate(portfolios, start=1):
            values = [
                portfolio["symbol"],
                str(portfolio["holding"]),
                f"₹{portfolio['average_cost']:,.2f}",
                f"₹{portfolio['current_price']:,.2f}",
                f"₹{portfolio['market_value']:,.2f}",
                f"₹{portfolio['unrealized_profit']:,.2f}",
            ]

            for column, value in enumerate(values):
                label = ctk.CTkLabel(
                    holdings_area,
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

    def show_transactions():
        heading.configure(text="Transactions")

        # Hide portfolio card
        summary_frame.pack_forget()
        holdings_area.pack_forget()

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

    holdings_area = ctk.CTkScrollableFrame(
        content,
        width=800,
        height=400,
    )

    portfolios = calculate_all_portfolios()
    total_investment = calculate_total_investment()
    total_market_value = calculate_total_market_value()
    total_profit = calculate_total_unrealized_profit()
    total_return = calculate_total_return()

    summary_frame = ctk.CTkFrame(content)
    summary_frame.pack(
        fill="x",
        padx=40,
        pady=10,
    )
    for column in range(4):
        summary_frame.grid_columnconfigure(
            column, 
            weight=1,
            uniform="summary",
        )

    create_summary_card(
        summary_frame,
        0,
        "Total Investment",
        f"₹{total_investment:,.2f}",
    )
    create_summary_card(
        summary_frame,
        1,
        "Market Value",
        f"₹{total_market_value:,.2f}",
    )
    create_summary_card(
        summary_frame,
        2,
        "Unrealized P/L",
        f"₹{total_profit:,.2f}",
    )
    create_summary_card(
        summary_frame,
        3,
        "Portfolio Return",
        f"{total_return:,.2f}%",
    )

    app.mainloop()

if __name__ == "__main__":
    main()