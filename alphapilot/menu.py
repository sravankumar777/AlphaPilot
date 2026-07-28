"""
Menu module for AlphaPilot
"""

def display_menu():
    """
    Display the main menu & return the user's choice.
    """

    print("\n" + "=" * 52)
    print("               AlphaPilot v0.1")
    print("=" * 52)

    print("1. Add Transaction")
    print("2. View Transaction")
    print("3. Search Transactions")
    print("4. Portfolio Summary")
    print("5. Exit")

    choice = input("\n Choose an option: ").strip()

    return choice