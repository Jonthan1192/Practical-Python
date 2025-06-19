# tableformat.py

from typing import List
from .stock import Stock


class FormatError(Exception):
    pass


class TableFormatter:
    def headings(self, headers: List[str]) -> None:
        """
        Emit the table headings.

        Args:
            headers (List[str]): A list of all the table headers.
        """
        raise NotImplementedError()

    def row(self, rowdata: List[str]) -> None:
        """
        Emit a single row of table data.

        Args:
            rowdata (List[str]): The data of a single table row.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """
    def headings(self, headers: List[str]) -> None:
        print(' '.join([f'{header:>10s}' for header in headers]))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata: List[str]) -> None:
        print(' '.join([f'{data:>10s}' for data in rowdata]))


class CSVTableFormatter(TableFormatter):
    """
    Emit a table in CSV format
    """
    def headings(self, headers: List[str]) -> None:
        print(','.join(headers))

    def row(self, rowdata: List[str]) -> None:
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Emit a table in HTML format
    """
    def headings(self, headers: List[str]) -> None:
        print(f'<tr>{"".join([f"<td>{header}</td>" for header in headers])}</tr>')

    def row(self, rowdata: List[str]) -> None:
        print(f'<tr>{"".join([f"<td>{data}</td>" for data in rowdata])}</tr>')


def create_formatter(name: str) -> TableFormatter:
    if name == 'txt' or name == 'text':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')
    return formatter


def print_table(portfolio: list[Stock], select: list[str], formatter: TableFormatter):
    # Print the headers
    formatter.headings(select)

    # Print the stocks
    for stock in portfolio:
        formatter.row([str(getattr(stock, column_name)) for column_name in select])
