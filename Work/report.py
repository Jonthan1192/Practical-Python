# report.py

from pathlib import Path
import csv


def read_portfolio(filename: Path) -> list:
    """
    Convert the csv file data to a list of stocks

    Args:
        filename (Path): Path to the CSV file containing portfolio data.

    Returns:
        list : The result list of stocks
    """
    portfolio = []
    with filename.open('r') as f:
        rows = csv.reader(f)
        # saving the headers row
        headers = next(rows)

        for i, row in enumerate(rows, start=1):
            try:
                stock = dict(zip(headers, row))
                stock = {
                    'name': stock['name'],
                    'shares': int(stock['shares']),
                    'price': float(stock['price'])
                }
                portfolio.append(stock)
            except ValueError:
                print(f"Warning: Wrong format at Line {i} in file {filename}")

    return portfolio


def read_prices(filename: Path) -> dict:
    """
     Convert the csv file data to a dictionary of stocks names and prices

     Args:
         filename (Path): Path to the CSV file containing portfolio data.

     Returns:
         list : The result dictionary of stocks names and prices
     """
    names_and_prices = {}
    with filename.open('r') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            try:
                # row format is: name,price
                names_and_prices[row[0]] = float(row[1])
            except (ValueError, IndexError):
                print(f"Warning: Wrong format at Line {i} in file {filename}")

    return names_and_prices


def make_report(portfolio: list[dict], prices: dict) -> list:
    report = []
    for stock in portfolio:
        name = stock["name"]
        old_price = stock["price"]
        new_price = prices[name]
        change = new_price - old_price

        updated_stock = {
            "name": name,
            "shares": stock["shares"],
            "price": new_price,
            "change": change
        }
        report.append(updated_stock)
    return report


p1 = Path(r"Data\portfolio.csv")
p2 = Path(r"Data\prices.csv")
portfolio = read_portfolio(p1)
prices = read_prices(p2)
report = make_report(portfolio, prices)

headers_string = f"{'Name':<10s} {'Shares':<10s} {'Price':<10s} {'Change':<10s}"
print(headers_string)
print('-'*len(headers_string))
for stock in report:
    print(f"{stock['name']:<10s} {stock['shares']:<10d} {stock['price']:<10.2f} {stock['change']:<10.2f}")
