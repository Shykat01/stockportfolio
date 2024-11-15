import yfinance as yf

# Portfolio to store stocks
portfolio = {}

# Function to add a stock to the portfolio
def add_stock(ticker, shares):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    if stock_info:
        portfolio[ticker] = {'name': stock_info['longName'], 'shares': shares}
        print(f"Added {shares} shares of {stock_info['longName']} to your portfolio.")
    else:
        print("Invalid ticker symbol.")

# Function to remove a stock from the portfolio
def remove_stock(ticker):
    if ticker in portfolio:
        removed_stock = portfolio.pop(ticker)
        print(f"Removed {removed_stock['name']} from your portfolio.")
    else:
        print("Stock not found in portfolio.")

# Function to display the portfolio
def display_portfolio():
    if portfolio:
        print("Your portfolio:")
        for ticker, info in portfolio.items():
            stock = yf.Ticker(ticker)
            stock_price = stock.history(period="1d")['Close'][0]
            total_value = stock_price * info['shares']
            print(f"{info['name']} ({ticker}): {info['shares']} shares at ${stock_price:.2f} per share, Total: ${total_value:.2f}")
    else:
        print("Your portfolio is empty.")

# Function to display options
def menu():
    print("""
    Stock Portfolio Tracker
    1. Add a stock
    2. Remove a stock
    3. View portfolio
    4. Exit
    """)

# Main loop for the tracker
def portfolio_tracker():
    while True:
        menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            ticker = input("Enter the stock ticker symbol (e.g., AAPL, TSLA): ").upper()
            shares = int(input("Enter the number of shares: "))
            add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the stock ticker symbol to remove: ").upper()
            remove_stock(ticker)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            print("Exiting portfolio tracker.")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    portfolio_tracker()
