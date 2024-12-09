"""
27

Create a software to evaluate value of a stock portfolio. The main program contains list of stocks, where user can add new items. After adding each item, the software asks "More stocks (y/n)=?"? If user answers y the software asks data of a new stock and inserts the stock into the list. If the user answers n, the software asks expected return of investment-% (roi), and number od years to wait before selling the stocks. 

Create class Stock, which contains properties:
- name
- price (>0, price of one stock)
- quantity (>0, number of stocks)

Class Stock contains methods:
- print_value(roi, years), which prints current value and expected value increase (in this order)
- Static method compute_increase(roi, value), which computes increase of value in one year

In main program, compute expected value of the portfolio with given parametrers.

Example:
% python3 my_code.solution.py
Company name: Nokia
Price: 10
Amount: 1000
More stocks (y/n)? y

Company name: Fortum
Price: 0.9
Amount: 400 
More stocks (y/n)? n

Expected ROI-%: 4
Years: 3

Nokia 1000 10.0
Stock value will be 11248.64, and profit 1248.64

Fortum 400 0.9
Stock value will be 404.95, and profit 44.95

Portfolio value will be 11653.59
"""
#Write class and imports here!

class Stock:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = max(0, price)  # Ensure price is > 0
        self.quantity = max(0, quantity)  # Ensure quantity is > 0

    def print_value(self, roi, years):
        current_value = self.price * self.quantity
        future_value = current_value * ((1 + roi / 100) ** years)
        profit = future_value - current_value
        print(f"{self.name} {self.quantity} {self.price:.1f}")
        print(f"Stock value will be {future_value:.2f}, and profit {profit:.2f}")

    @staticmethod
    def compute_increase(roi, value):
        return value * (roi / 100)

# Main program
if __name__ == "__main__":
    stocks = []

    while True:
        # Get stock data
        name = input("Company name: ")
        price = float(input("Price: "))
        quantity = int(input("Amount: "))
        stocks.append(Stock(name, price, quantity))

        # Check if the user wants to add more stocks
        more_stocks = input("More stocks (y/n)? ").strip().lower()
        if more_stocks != 'y':
            break

    # Get investment parameters
    roi = float(input("Expected ROI-%: "))
    years = int(input("Years: "))

    # Calculate and print stock and portfolio values
    total_value = 0
    for stock in stocks:
        stock.print_value(roi, years)
        current_value = stock.price * stock.quantity
        total_value += current_value * ((1 + roi / 100) ** years)

    print(f"\nPortfolio value will be {total_value:.2f}")

































# if __name__ == "__main__":
#     #Write main program here
