# portfolio.py

from .stock import Stock
from pydantic import BaseModel, Field
from . import fileparse
from typing import List, Any


class Portfolio(BaseModel):

    stocks: List[Stock] = Field(description="A list of stocks holding")

    @property
    def total_cost(self):
        return sum([s.cost for s in self.stocks])

    @classmethod
    def from_csv(cls, lines: Any) -> "Portfolio":
        self = cls(stocks=fileparse.parse_csv(lines))
        return self
