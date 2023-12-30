# this block will be pasted at constant.py at the end of the development
from enum import Enum
class INCOMESTATEMENT(Enum):
    CALENDAR_YEAR='calendarYear'
    GROSSPROFIT_RATIO='grossProfitRatio'
    NETINCOME_RATIO='netIncomeRatio'
    GROSS_PROFIT='grossProfit'
    RD='researchAndDevelopmentExpenses'
    SGA_EXPENSE='sellingGeneralAndAdministrativeExpenses'
    DEPRECIATION='depreciationAndAmortization'
    OPERATING_INCOME='operatingIncome'
    INTEREST_EXPENSE='interestExpense'


class BALANCESHEET(Enum):
    CALENDAR_YEAR='calendarYear'
    LONGTERM_DEBT='longTermDebt'
    TOTAL_LIABILITIES='totalLiabilities'
    TOTAL_STOCKHOLDEREQUITIES='totalStockholdersEquity'

class BALANCEGROWTH(Enum):
    CALENDAR_YEAR='calendarYear'
    RETAINEDEARNINGS_GROWTH='growthRetainedEarnings'


class CASHFLOWSTATEMENT(Enum):
    CALENDAR_YEAR='calendarYear'
    CAPEX='capitalExpenditure'