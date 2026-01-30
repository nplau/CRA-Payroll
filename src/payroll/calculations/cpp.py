
# doesnt include CPP2 additional contributions

def calculate_cpp(
        gross_pay: float,
        annual_pay_periods: int,
        cpp_rate: float = 0.0595,
        annual_exemption: float = 3500.0,
) -> float:
    
    if gross_pay <= 0:
            return 0.0

    period_exemption = annual_exemption / annual_pay_periods

    pensionable_earnings = max(0.0, gross_pay - period_exemption)

    cpp = pensionable_earnings * cpp_rate

    return round(cpp, 2)
