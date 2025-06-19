# stock.py

from pydantic import BaseModel, Field, field_validator


class Stock(BaseModel):
    """
    Represents a stock holding with a name, number of shares, and price per share.
    """
    name: str = Field(min_length=1, description="Stock symbol")
    shares: int = Field(gt=0, description="Number of shares")
    price: float = Field(gt=0.0, description="Price per share")

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, sell_amount: int):
        self.shares -= sell_amount
