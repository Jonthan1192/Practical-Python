#!/usr/bin/env python3
# pcost.py

import argparse
from pathlib import Path
from report import read_portfolio
from stock import Stock


def portfolio_cost(filename: Path) -> float:
    portfolio = read_portfolio(filename)
    total_cost = sum([stock.cost for stock in portfolio])
    return total_cost


def main():
    parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
    parser.add_argument("filename", type=Path, help="Path to the input CSV file")
    args = parser.parse_args()

    cost = portfolio_cost(args.filename)
    print("Total cost:", cost)


if __name__ == '__main__':
    main()
