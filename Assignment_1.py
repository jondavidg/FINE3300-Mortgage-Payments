#Define a function for the present value of an annuity (PVA) equation, which takes parameters principal, quoted interest rate, and amortization period
def present_value_annuity(principal, rate, amortization):
    
    #Replicate the present value of an annuity equation, and rearrange it to solve for the payment value
    payment = ((principal * rate) / (1 - ((1 + rate) ** (-amortization))))
    
    #Return the payment
    return payment

#Define a function to execute the mortgage payment calculation, which takes parameters principal, quoted interest rate, and amortization period
def mortgage_payments(principal, rate, amortization):

    #Since the rate is inputted as a percent (e.g., 4.5), divide by 100 for ease of use in later calculations
    rate /= 100

    #Calculate the appropriate periodic rate using the corresponding equations
    monthly_periodic_rate = (((1 + (rate / 2)) ** (2 / 12)) - 1)
    semi_monthly_periodic_rate = (((1 + (rate / 2)) ** (2 / 24)) - 1)
    bi_weekly_periodic_rate = (((1 + (rate / 2)) ** (2 / 26)) - 1)
    weekly_periodic_rate = (((1 + (rate / 2)) ** (2 / 52)) - 1)

    #Calculate the payments by calling the present_value_annuity function (where applicable), inputting the provided parameters, and converting the period (in years) to the respective period values
    monthly_payment = present_value_annuity(principal, monthly_periodic_rate, (amortization * 12))
    semi_monthly_payment = present_value_annuity(principal, semi_monthly_periodic_rate, (amortization * 24))
    bi_weekly_payment = present_value_annuity(principal,  bi_weekly_periodic_rate, (amortization * 26))
    weekly_payment = present_value_annuity(principal,  weekly_periodic_rate, (amortization * 52))
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4

    #Return the payments as a tuple of six values
    return monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment

#Prompt the user to enter the principal amount, quoted interest rate, and amortization period, and convert these inputs to float datatype to be used later as function parameters
principal = float(input("Please enter the principal amount: "))
rate = float(input("Please enter the quoted interest rate as a percent: "))
amortization = float(input("Please enter the amortization period in years: "))

#Call the mortgage_payments function and input the user-provided parameters, then store the resulting tuple of six values from the function (unpack them) into six corresponding variables
monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment = mortgage_payments(principal, rate, amortization)

#Print the payment outputs according to the desired format, rounding to two decimal places and retaining the trailing zero (where applicable)
print(f"Monthly Payment: ${round(monthly_payment,2):.2f}")
print(f"Semi-monthly Payment: ${round(semi_monthly_payment,2):.2f}")
print(f"Bi-weekly Payment: ${round(bi_weekly_payment,2):.2f}")
print(f"Weekly Payment: ${round(weekly_payment,2):.2f}")
print(f"Rapid Bi-weekly Payment: ${round(rapid_bi_weekly_payment,2):.2f}")
print(f"Rapid Weekly Payment: ${round(rapid_weekly_payment,2):.2f}")