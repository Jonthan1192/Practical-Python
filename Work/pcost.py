#!/usr/bin/env python3
# pcost.py

import argparse
from pathlib import Path
from report import read_portfolio
from stock import Stock


def portfolio_cost(filename: Path) -> float:
    portfolio = read_portfolio(filename)
    total_cost = 0.0
    for stock in portfolio:
        total_cost += stock.shares * stock.price
    return total_cost


def main():
    parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
    parser.add_argument("filename", type=Path, help="Path to the input CSV file")
    args = parser.parse_args()

    cost = portfolio_cost(args.filename)
    print("Total cost:", cost)


if __name__ == '__main__':
    main()
