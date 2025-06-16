# pcost.py

import argparse
from pathlib import Path
import csv


def portfolio_cost(filename: Path) -> float:
    total_cost = 0.0
    with filename.open('r') as f:
        rows = csv.reader(f)
        # saving the headers row
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            try:
                row_dict = dict(zip(headers, row))
                total_cost += int(row_dict['shares']) * float(row_dict['price'])
            except ValueError:
                print(f"Warning: Wrong format at Line {i} in file {filename}")

    return total_cost


parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
parser.add_argument("filename", type=Path, help="Path to the input CSV file")
args = parser.parse_args()

cost = portfolio_cost(args.filename)
print("Total cost:", cost)
