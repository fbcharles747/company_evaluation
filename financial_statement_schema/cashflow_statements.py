from pydantic import BaseModel


class CashflowStatement(BaseModel):
    date: str
    operating_cash_flow: float
    investing_cash_flow: float
    free_cashflow: float


class CashflowStatements(BaseModel):
    cashflow_statements: list[CashflowStatement]
