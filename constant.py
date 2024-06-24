# this block will be pasted at constant.py at the end of the development
from enum import Enum
class INCOMESTATEMENT(Enum):
    CALENDAR_YEAR='calendarYear'
    PERIOD='period'
    GROSSPROFIT_RATIO='grossProfitRatio'
    NETINCOME_RATIO='netIncomeRatio'
    GROSS_PROFIT='grossProfit'
    RD='researchAndDevelopmentExpenses'
    SGA_EXPENSE='sellingGeneralAndAdministrativeExpenses'
    DEPRECIATION='depreciationAndAmortization'
    OPERATING_INCOME='operatingIncome'
    INTEREST_EXPENSE='interestExpense'
    TAX='incomeTaxExpense'


class BALANCESHEET(Enum):
    CALENDAR_YEAR='calendarYear'
    PERIOD='period'
    LONGTERM_DEBT='longTermDebt'
    TOTAL_LIABILITIES='totalLiabilities'
    TOTAL_STOCKHOLDEREQUITIES='totalStockholdersEquity'
    TOTAL_DEBT='totalDebt'


class BALANCEGROWTH(Enum):
    CALENDAR_YEAR='calendarYear'
    RETAINEDEARNINGS_GROWTH='growthRetainedEarnings'

class INCOMEGROWTH(Enum):
    CALENDAR_YEAR='calendarYear'
    EBITDA_GROWTH='growthEBITDA'
    NET_INCOME_GROWTH='growthNetIncome'


class CASHFLOWSTATEMENT(Enum):
    CALENDAR_YEAR='calendarYear'
    PERIOD='period'
    CAPEX='capitalExpenditure'
    COMMONSTOCK_REPURCHASE='commonStockRepurchased'
    DIVIDEND_PAID='dividendsPaid'
    DEPRECIATION='depreciationAndAmortization'
    CHANGE_WORKING_CAP='changeInWorkingCapital'
    NET_INCOME='netIncome'
    FREE_CASH_FLOW='freeCashFlow'
    

class PERIOD(Enum):
    QUARTER='quarter'
    ANNUAL='annual'

class INTRINSICVALUATION(Enum):
    OPINCOME_AFTER_TAX='operating_income_after_tax'
    NET_CAPEX='net_capex'
    FCFF='free cash flow to firm'
    AUGMENTED_DIVIDEND='augmented dividend'
    RETENTION_RATIO='retention_ratio'
    EXPECTED_GROWTH_FCFE='expected growth in FCFE'
    EXPECTED_GROWTH_FCFF='expected growth in FCFF'
    REINVESTMENT_RATE='reinvestment rate'
    CALCULATE_TERMINAL_VAL='terminal value calculated'
    STOCK_INTRINSIC_VAL='intrinsic value per share'
    

class ADVANCED_DCF(Enum):
    CALENDAR_YEAR='year'
    RISK_FREE_RATE='riskFreeRate'
    WACC='wacc'
    TAX_RATE='taxRate'
    EBIT='ebit'
    LONG_TERM_GROWTH='longTermGrowthRate'
    DILUTED_SHARE_OUTSTANDING='dilutedSharesOutstanding'
    
    

class RATIO(Enum):
    CALENDAR_YEAR='calendarYear'
    PERIOD='period'
    RETURN_ON_EQUITY='returnOnEquity'
    RETURN_ON_CAPITAL='returnOnCapitalEmployed'
    LIABILITY_TO_SHAREHOLDER_EQUITY='liability_shareholder ratio'
    RD_GROSSPROFIT_RATIO='RD_grossProfit_Ratio'
    SGA_GROSSPROFIT_RATIO='SGA_grossProfit_Ratio'
    DEPRECIATION_GROSSPROFIT_RATIO='Depreciation_grossProfit_Ratio'
    INTEREST_EXP_OPINCOME_RATIO='interestExpense_operatingIncome_Ratio'
    DEBT_NETINCOME_RATIO='debt_ netIncome_ratio'
    CAPEX_GROSSPROFIT_RATIO='capex_grossProfit_rario'
    