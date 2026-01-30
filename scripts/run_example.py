from payroll.calculations.cpp import calculate_cpp

cpp = calculate_cpp(
    gross_pay=2000.00,
    annual_pay_periods=26,
)

print("CPP deduction:", cpp)

