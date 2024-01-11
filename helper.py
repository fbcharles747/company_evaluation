
import math
def to_percentage(val:float)->str:
    """
    convert decimal number to percentage
    Args:
        val (float): The decimal number grossProfitto convert
    Returns:
        str: percentage str of the data
    """
    return "{number:.2f} %".format(number=val*100)

def discount_terminal_value(fcff:float,
                            wacc:float,
                            risk_free_rate:float,
                            expected_growth_in_n:float,
                            reinvestment_rate:float,
                            n:int=5)->float:

    """
    
    Args:
        fcff (float): Free cash flow to firm, come from EBIT *(1-Tax rate) - capital expenditure - change in working capital
        wacc (float): cost of capital
        risk_free_rate (float): interest rate of risk-free investment
        expected_growth_in_n (float): expected growth within estimated period = return on capital * reinvestment_rate
        reinvestment_rate (float): portion of after tax income that get reinvested = (change in working capital + capital expenditure) / EBIT 

    """
    
    # fcff at year n
    fcff_end_period=fcff*math.pow(1+expected_growth_in_n,n)
    
    # reinvestment rate at stable grow
    reinvest_stable_rate=risk_free_rate/wacc
    # operating income after tax in year n+1
    opIncome_end_period=((fcff_end_period)/(1-reinvestment_rate))*(1+risk_free_rate)
    fcff_over_end=opIncome_end_period*(1-reinvest_stable_rate)



    # terminal value at year n+1
    terminal_val_end_period=(fcff_over_end)/(wacc-risk_free_rate)
    # print(f'reinvestment at stable: {reinvest_stable_rate}')
    # print(f'FCFF at end of the period: {fcff_end_period}')
    # print(f'operating income after tax at year n+1: {opIncome_end_period}')
    # print(f'Terminal value at year n+1 {terminal_val_end_period}')

    # calculate total fcff within the period
    cf_sum=0
    for i in range(1,n+1):
        discounted_rate=math.pow(1+wacc,i)
        growth_rate=math.pow(1+expected_growth_in_n,i)
        discounted_cf=fcff*growth_rate/discounted_rate
        # print(f'FCFF at year {i}: {fcff*growth_rate}')
        cf_sum+=discounted_cf
    
    precent_terminal=terminal_val_end_period/(math.pow(1+wacc,n))
    
    return precent_terminal+cf_sum
    


def reinvestment_rate(operating_income_after_tax:float,net_capex:float,change_in_working_cap:float)->float:
   
    return (net_capex+change_in_working_cap)/operating_income_after_tax