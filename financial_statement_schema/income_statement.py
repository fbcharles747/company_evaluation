from pydantic import BaseModel
from typing import Optional


class IncomeStatement(BaseModel):
    revenue: float
    cost_of_goods_sold: float
    gross_profit: float
    operating_expenses: float
    operating_income: float
    net_income: float
    eps: float
    interest_expense: float
    share_outstanding: Optional[int]  # Number of shares outstanding
    date: str


class IncomeStatements(BaseModel):
    income_statements: list[IncomeStatement]
