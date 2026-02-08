from pydantic import BaseModel

from pydantic import BaseModel
from typing import List, Optional

class BalanceSheet(BaseModel):
    total_asset: float
    total_liability: float
    totalDebt: float  # Total liabilities
    totalEquity: float  # Shareholders' equity
    current_assets: float  # Total assets
    current_liabilities: float  # Total current liabilities
    shareholderEquity: float  # Total shareholder equity
    inventory: float  # Total inventory
    account_receivable: float  # Total account receivable
    account_payable: float  # Total account payable
    date: str  # The calendar year (or report date) for which the balance sheet data is reported

class BalanceSheets(BaseModel):
    balance_sheets: list[BalanceSheet]

