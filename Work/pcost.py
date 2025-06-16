# pcost.py

import argparse
from pathlib import Path
import csv


def portfolio_cost(filename: Path) -> float:
    total_cost = 0.0
    with filename.open('r') as f:
        rows = csv.reader(f)
        # skipping the headers row
        next(rows)
        for row in rows:
            try:
                # row format is: name,shares,price
                total_cost += float(row[1]) * float(row[2])
            except ValueError:
                print(f"Warning: file {filename} has a bad line")

    return total_cost


parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
parser.add_argument("filename", type=Path, help="Path to the input CSV file")
args = parser.parse_args()

cost = portfolio_cost(args.filename)
print("Total cost:", cost)
