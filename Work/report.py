#!/usr/bin/env python3
# report.py

import csv
from pathlib import Path
from fileparse import parse_csv


def read_portfolio(filename: Path) -> list:
    """
    Convert the csv file data to a list of stocks

    Args:
        filename (Path): Path to the CSV file containing portfolio data.

    Returns:
        list : The result list of stocks
    """
    with filename.open("r") as f:
        portfolio = parse_csv(lines=f)
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


def make_report(portfolio: list[dict], prices: dict) -> list[dict]:
    """
     Makes a report out of the current prices and a porfolio

     Args:
         portfolio (list[dict]): The list of the stocks. each stock is a dict
         prices (list[tuple]): The names and prices of the stocks. Each stock is a tuple

     Returns:
         list[dict]: The report
     """
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


def print_report(report: list[dict]) -> None:
    """
     Prints a report nicely

     Args:
         report (list[dict]) : The report to print

     Returns:
         None
     """
    headers = ("Name", "Shares", "Price", "Change")
    col_width = 10
    for header in headers:
        print(f"{header:>{col_width}s}", end=' ')
    print()

    headers = [header.lower() for header in headers]
    print((('-' * 10) + ' ') * len(headers))
    for stock in report:
        for header in headers:
            value = stock[header]
            if isinstance(value, int):
                print(f"{value:>{col_width}d}", end=' ')
            elif isinstance(value, float):
                print(f"{value:>{col_width}.2f}", end=' ')
            else:
                print(f"{str(value):>{col_width}s}", end=' ')
        print()


def portfolio_report(portfolio_filename: str, prices_filename: str) -> None:
    portfolio_path = Path(portfolio_filename)
    prices_path = Path(prices_filename)
    portfolio = read_portfolio(portfolio_path)
    prices = read_prices(prices_path)
    report = make_report(portfolio, prices)
    print_report(report)
