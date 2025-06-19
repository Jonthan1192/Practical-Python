# fileparse.py

import csv
from typing import List, Dict, Any, Callable
import yaml
import logging
log = logging.getLogger(__name__)


def apply_types_functions(types, lst):
    return [func(val) for func, val in zip(types, lst)]


def parse_csv(lines: Any, select: List[str] = None, types: List[Callable] = None, has_headers: bool = True, delimiter: str = ',', silence_errors=False) -> List:
    """
    Parse a CSV file into a list of records as dictionaries.

    Args:
        lines (Path): CSV lines to parse.
        select (List[str]): List of columns to be picked out
        types (List[Callable]): List of functions to apply to each column values
        has_headers (bool): Whether the first line of the file contains column headers
        delimiter (str): The column separator in the file
        silence_errors (bool): If True, error messages will be silenced

    Returns:
        List: A list of stocks represented in the CSV rows.
    """
    if not has_headers and select is not None:
        raise RuntimeError("select argument requires column headers")

    # Set default values to select and types args
    if select is None:
        select = ['name', 'shares', 'price']
    if types is None:
        types = [str, int, float]

    records = []
    start_row = 0

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers
    if has_headers:
        headers = next(rows)

        # Calculate indices
        indices = [headers.index(column) for column in select]
        start_row = 1

    # Read all row
    for i, row in enumerate(rows, start=start_row):
        # Skip empty rows
        if not row:
            continue
        try:
            if has_headers:
                # Remove the unwanted columns, and order the row so it wil match select
                row = [row[index] for index in indices]
                row = apply_types_functions(types, row)

                # Create the record and add it to the list
                record = dict(zip(select, row))
            else:
                row = apply_types_functions(types, row)
                record = row
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                log.warning("Row %d: Couldn't convert %s", i, row)
                log.debug("Row %d: Reason %s", i, e)
            continue

    return records


def parse_yaml(lines: Any) -> Dict[Any, Any]:
    """
    Parses data in YAML format

    Args:
        lines (Any): The YAML data to parse

    Returns: Dict[Any, Any], The parsed data

    """
    return yaml.safe_load(lines)
