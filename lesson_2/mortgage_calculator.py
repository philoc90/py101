def invalid_amount(amount):
    try:
        if float(amount) > 0:
            return False
        return True
    except ValueError:
        return True


def invalid_duration(duration):
    try:
        int(duration)
    except ValueError:
        return True
    if int(duration) % 1 == 0 and int(duration) > 0:
        return False
    return True


print("Welcome to mortgage calculator!")

loan_amount = input("Please input the loan amount:$")
while invalid_amount(loan_amount):
    loan_amount = input("Please input a positive number:$")

apr = input("Please input the APR:%")
while invalid_amount(apr):
    apr = input("Please input a positive APR:%")

number_of_months = input("Please input the loan's duration in months: ")
while invalid_duration(number_of_months):
    number_of_months = input("Please input the duration in months: ")

monthly_rate = (float(apr) / 12) * 0.01
monthly_payment = float(loan_amount) * (
    float(monthly_rate)
    / (1 - (1 + float(monthly_rate)) ** (-float(number_of_months)))
)

print(f"Your monthly payment is {monthly_payment:.2f}.")
