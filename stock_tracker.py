

# Hardcoded dictionary of stock prices (in dollars)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def show_available_stocks():
    """Print the stocks the user can choose from."""
    print("\nAvailable stocks and prices:")
    for name, price in stock_prices.items():
        print("  " + name + " : $" + str(price))


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dictionary."""
    portfolio = {}  # stock name -> quantity

    print("\nEnter your stocks one by one.")
    print("Type 'done' when you are finished.")

    while True:
        name = input("\nStock name: ").upper().strip()

        if name == "DONE":
            break

        if name not in stock_prices:
            print("Sorry, '" + name + "' is not in the price list. Try again.")
            continue

        qty_text = input("Quantity of " + name + ": ").strip()

        # Make sure quantity is a positive whole number
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a positive whole number for quantity.")
            continue

        quantity = int(qty_text)

        # If the stock was already entered, add to its quantity
        if name in portfolio:
            portfolio[name] = portfolio[name] + quantity
        else:
            portfolio[name] = quantity

        print("Added " + str(quantity) + " x " + name)

    return portfolio


def calculate_and_display(portfolio):
    """Calculate each stock's value and the total. Returns (lines, total)."""
    lines = []
    total = 0

    lines.append("=" * 40)
    lines.append("       PORTFOLIO SUMMARY")
    lines.append("=" * 40)

    for name, quantity in portfolio.items():
        price = stock_prices[name]
        value = price * quantity
        total = total + value
        lines.append(name + ": " + str(quantity) + " x $" + str(price) + " = $" + str(value))

    lines.append("-" * 40)
    lines.append("TOTAL INVESTMENT: $" + str(total))
    lines.append("=" * 40)

    for line in lines:
        print(line)

    return lines, total


def save_to_file(lines):
    """Save the summary to a .txt file."""
    file = open("portfolio.txt", "w")
    for line in lines:
        file.write(line + "\n")
    file.close()
    print("\nResult saved to portfolio.txt")


def main():
    print("=" * 40)
    print("   STOCK PORTFOLIO TRACKER")
    print("=" * 40)

    show_available_stocks()
    portfolio = get_portfolio()

    if len(portfolio) == 0:
        print("\nNo stocks entered. Goodbye!")
        return

    lines, total = calculate_and_display(portfolio)

    choice = input("\nSave result to a file? (y/n): ").lower().strip()
    if choice == "y":
        save_to_file(lines)

    print("Thanks for using the tracker!")


main()