#!/usr/bin/env python3
# report.py

from pathlib import Path
from fileparse import parse_csv
from collections import namedtuple
from stock import Stock
from tableformat import TableFormatter
import tableformat
import argparse
from portfolio import Portfolio

# Define a namedtuple to represent a stock record
TableRow = namedtuple('TableRow', ['name', 'shares', 'price', 'change'])


def read_portfolio(filename: Path) -> Portfolio:
    """
    Convert the csv file data to a list of stocks

    Args:
        filename (Path): Path to the CSV file containing portfolio data.

    Returns:
        list : The result list of stocks
    """
    with filename.open("r") as f:
        portfolio = Portfolio.from_csv(lines=f)
    return portfolio


def read_prices(filename: Path) -> dict:
    """
     Convert the csv file data to a dictionary of stocks names and prices

     Args:
         filename (Path): Path to the CSV file containing portfolio data.

     Returns:
         list : The result dictionary of stocks names and prices
     """
    with filename.open("r") as f:
        names_and_prices = parse_csv(lines=f, types=[str, float], has_headers=False)
    names_and_prices = dict(names_and_prices)
    return names_and_prices


def make_report(portfolio: Portfolio, prices: dict) -> list[TableRow]:
    """
     Makes a report out of the current prices and a portfolio

     Args:
         portfolio (list[dict]): The list of the stocks. each stock is a dict
         prices (list[tuple]): The names and prices of the stocks. Each stock is a tuple

     Returns:
         list[dict]: The report
     """
    report = []
    for stock in portfolio.stocks:
        name = stock.name
        old_price = stock.price
        new_price = prices[name]
        change = new_price - old_price

        updated_stock = TableRow(name=name, shares=stock.shares, price=new_price, change=change)
        report.append(updated_stock)
    return report


def print_report(report_data: list[TableRow], formatter: TableFormatter) -> None:
    """
    Print a formatted table from a list of TableRow namedtuples.

    Args:
        report_data (List[TableRow]): The data to be printed in table format.
        formatter (TableFormatter): The formatter used to format the table.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report_data:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_path: Path, prices_path: Path, format_name: str) -> None:
    """
    Generate and print a stock performance report from portfolio and price files.

    Args:
        portfolio_path (Path): Path to the CSV file containing portfolio data.
        prices_path (Path): Path to the CSV file containing current stock prices.
        format_name (str): The name of the format the report will be printed with
    """
    portfolio = read_portfolio(portfolio_path)
    prices = read_prices(prices_path)

    # Make report
    report = make_report(portfolio, prices)

    # Print the report
    formatter = tableformat.create_formatter(format_name)
    print_report(report, formatter)


def main():
    parser = argparse.ArgumentParser(description="Prints a report of stocks changes")
    parser.add_argument("stocks_path", type=Path, help="Path to the stocks CSV file")
    parser.add_argument("prices_path", type=Path, help="Path to the prices CSV file")
    parser.add_argument("print_format", type=str, help="The format to print the report")
    args = parser.parse_args()

    portfolio_report(args.stocks_path, args.prices_path, args.print_format)


if __name__ == '__main__':
    main()
